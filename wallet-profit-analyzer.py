import pandas as pd

INPUT_FILE = "data/processed/token_transfers.csv"


def calculate_profit():

    df = pd.read_csv(INPUT_FILE)

    inflow = df[df["to"] == "WALLET"]
    outflow = df[df["from"] == "WALLET"]

    inflow_total = inflow.groupby("token")["value"].sum()
    outflow_total = outflow.groupby("token")["value"].sum()

    profit = inflow_total - outflow_total

    return profit


def main():

    profit = calculate_profit()

    print("\nWallet Token Net Flow\n")
    print(profit)


if __name__ == "__main__":
    main()
