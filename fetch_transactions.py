import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

# Target wallet
WALLET_ADDRESS = "0xYourWalletAddress"

# Output path
OUTPUT_FILE = "data/raw/wallet_transactions.json"


def fetch_transactions(address):
    """
    Fetch transaction history for a wallet using Etherscan API
    """

    url = "https://api.etherscan.io/api"

    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": ETHERSCAN_API_KEY,
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch transactions")

    data = response.json()

    if data["status"] != "1":
        raise Exception("API returned error: " + data["message"])

    return data["result"]


def save_transactions(transactions):
    """
    Save transactions to JSON file
    """

    os.makedirs("data/raw", exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(transactions, f, indent=2)

    print(f"Saved {len(transactions)} transactions to {OUTPUT_FILE}")


def main():
    print("Fetching transactions...")

    transactions = fetch_transactions(WALLET_ADDRESS)

    print("Total transactions:", len(transactions))

    save_transactions(transactions)


if __name__ == "__main__":
    main()
