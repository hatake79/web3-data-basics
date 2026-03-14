import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ETHERSCAN_API_KEY")

WALLET_ADDRESS = "0xYourWalletAddress"

OUTPUT_FILE = "data/processed/token_transfers.csv"


def fetch_token_transfers(address):

    url = "https://api.etherscan.io/api"

    params = {
        "module": "account",
        "action": "tokentx",
        "address": address,
        "sort": "asc",
        "apikey": API_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "1":
        raise Exception("Error fetching token transfers")

    return data["result"]


def build_dataset(transfers):

    rows = []

    for tx in transfers:

        value = int(tx["value"]) / (10 ** int(tx["tokenDecimal"]))

        rows.append(
            {
                "token": tx["tokenSymbol"],
                "from": tx["from"],
                "to": tx["to"],
                "value": value,
                "timestamp": tx["timeStamp"],
                "hash": tx["hash"],
            }
        )

    return pd.DataFrame(rows)


def main():

    print("Fetching token transfers...")

    transfers = fetch_token_transfers(WALLET_ADDRESS)

    df = build_dataset(transfers)

    os.makedirs("data/processed", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved {len(df)} transfers to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
