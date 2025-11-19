from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from blockchain import contract, web3
from certificate_template import generate_certificate
import os
from dotenv import load_dotenv
import random
import string

def generate_certificate_id(name):
    prefix = ''.join([c for c in name.upper() if c.isalpha()][:3]) 
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{prefix}-{random_part}"


load_dotenv()

app = Flask(__name__)
CORS(app)

#blockchain
@app.route("/generate", methods=["POST"])
def generate_certificate_route():
    data = request.json

    name = data["name"]
    course = data["course"]
    grade = data["grade"]
    date = data["date"]

    # Create certificate ID
    certificate_id = generate_certificate_id(name)




    # PDF output path
    folder = "generated"
    if not os.path.exists(folder):
        os.makedirs(folder)

    output_file = f"{folder}/{certificate_id}.pdf"

    # Generate certificate PDF with QR
    generate_certificate(
        name=name,
        course=course,
        grade=grade,
        date=date,
        certificate_id=certificate_id,
        output_file=output_file
    )

    # Hash certificate contents
    cert_data_string = name + course + grade + date
    hash_bytes = web3.keccak(text=cert_data_string)

    # Blockchain write transaction
    account = web3.eth.account.from_key(os.getenv("PRIVATE_KEY"))

    txn = contract.functions.storeCertificate(
        certificate_id,
        hash_bytes,
        "example.com"
    ).build_transaction({
        "from": account.address,
        "nonce": web3.eth.get_transaction_count(account.address),
        "gas": 300000,
        "gasPrice": web3.eth.gas_price
    })

  
    signed_tx = account.sign_transaction(txn)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction).hex()
   

    return jsonify({
        "certificate_id": certificate_id,
        "tx_hash": tx_hash,
        "download_url": f"http://localhost:5000/download/{certificate_id}"
    })



# Download certificate PDF

@app.route("/download/<certificate_id>", methods=["GET"])
def download_certificate(certificate_id):
    pdf_path = f"generated/{certificate_id}.pdf"
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    return jsonify({"error": "Certificate not found"})



# Verify certificate using blockchain

@app.route("/verify/<certificate_id>", methods=["GET"])
def verify_certificate(certificate_id):
    (hash_bytes, timestamp, issuer) = contract.functions.getCertificate(certificate_id).call()

    if timestamp == 0:
        return jsonify({"valid": False, "reason": "Certificate not found"})

    return jsonify({
        "valid": True,
        "hash": hash_bytes.hex(),
        "timestamp": timestamp,
        "issuer": issuer
    })


if __name__ == "__main__":
    app.run(debug=True)
