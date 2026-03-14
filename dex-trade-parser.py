import json

INPUT_FILE = "data/raw/wallet_transactions.json"


def detect_swaps():

    with open(INPUT_FILE) as f:
        txs = json.load(f)

    swaps = []

    for tx in txs:

        if tx["input"] != "0x":

            swaps.append(tx)

    return swaps


def main():

    swaps = detect_swaps()

    print("Potential DEX swaps:", len(swaps))


if __name__ == "__main__":
    main()
