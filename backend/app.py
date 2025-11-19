from blockchain import contract, web3

@app.route("/verify/<cert_id>", methods=["GET"])
def verify(cert_id):
    stored_hash, timestamp, issuer = contract.functions.getCertificate(cert_id).call()

    if timestamp == 0:
        return jsonify({"valid": False, "reason": "Certificate not found"})

    return jsonify({
        "valid": True,
        "hash": stored_hash,
        "timestamp": timestamp,
        "issuer": issuer
    })
