import json
import os

INPUT_FILE = "data/raw/wallet_transactions.json"
WALLET_ADDRESS = "0xYourWalletAddress"


def load_transactions():
    if not os.path.exists(INPUT_FILE):
        raise Exception("Transaction file not found. Run fetch_transactions.py first.")

    with open(INPUT_FILE, "r") as f:
        return json.load(f)


def scan_wallet(transactions, wallet):
    incoming = 0
    outgoing = 0

    total_in_value = 0
    total_out_value = 0

    for tx in transactions:

        value_eth = int(tx["value"]) / 10**18

        if tx["to"] and tx["to"].lower() == wallet.lower():
            incoming += 1
            total_in_value += value_eth

        if tx["from"].lower() == wallet.lower():
            outgoing += 1
            total_out_value += value_eth

    return {
        "total_transactions": len(transactions),
        "incoming_transactions": incoming,
        "outgoing_transactions": outgoing,
        "total_in_eth": total_in_value,
        "total_out_eth": total_out_value,
        "net_flow_eth": total_in_value - total_out_value,
    }


def main():
    transactions = load_transactions()

    metrics = scan_wallet(transactions, WALLET_ADDRESS)

    print("\nWallet Activity Summary\n")

    for key, value in metrics.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
