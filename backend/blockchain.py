from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

RPC = os.getenv("AMOY_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

web3 = Web3(Web3.HTTPProvider(RPC))

with open("CertificateRegistry.json") as f:
    abi = json.load(f)

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

def store_certificate_on_chain(cert_id, hash_hex):
    account = web3.eth.account.from_key(PRIVATE_KEY)

    tx = contract.functions.storeCertificate(
        cert_id,
        hash_hex,
        "example.com"
    ).build_transaction({
        "from": account.address,
        "nonce": web3.eth.get_transaction_count(account.address),
        "gas": 300000,
        "gasPrice": web3.eth.gas_price
    })

    signed = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)

    return web3.to_hex(tx_hash)
