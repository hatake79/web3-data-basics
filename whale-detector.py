import pandas as pd

INPUT_FILE = "data/processed/token_transfers.csv"

WHALE_THRESHOLD = 100000


def detect_whales():

    df = pd.read_csv(INPUT_FILE)

    whales = df[df["value"] > WHALE_THRESHOLD]

    return whales


def main():

    whales = detect_whales()

    print("\nWhale Transfers\n")

    print(whales.head())


if __name__ == "__main__":
    main()
