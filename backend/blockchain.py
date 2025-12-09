import json
import os
from web3 import Web3
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

load_dotenv()

# Absolute path to ABI file
ABI_PATH = os.path.join(os.path.dirname(__file__), "CertificateRegistry.json")

with open(ABI_PATH) as f:
    artifact = json.load(f)
    abi = artifact["abi"]

RPC_URL = os.getenv("AMOY_RPC") or os.getenv("SEPOLIA_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")

# --- NEW: Robust Connection Logic ---
session = requests.Session()
retries = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["POST"]
)
session.mount('https://', HTTPAdapter(max_retries=retries))
session.mount('http://', HTTPAdapter(max_retries=retries))

# Connect to blockchain using the robust session
web3 = Web3(Web3.HTTPProvider(RPC_URL, session=session))

if not web3.is_connected():
    raise Exception("❌ Web3 connection failed")

# Load contract object
contract = web3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=abi
)