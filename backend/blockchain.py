import json
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Absolute path to ABI file
ABI_PATH = os.path.join(os.path.dirname(__file__), "CertificateRegistry.json")

with open(ABI_PATH) as f:
    artifact = json.load(f)
    abi = artifact["abi"]  # FIX: Load only ABI list

RPC_URL = os.getenv("AMOY_RPC") or os.getenv("SEPOLIA_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

# Connect to blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))

if not web3.is_connected():
    raise Exception("❌ Web3 connection failed")

# Load contract object
contract = web3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=abi
)
