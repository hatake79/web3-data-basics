import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

WALLET = "0xYourWalletAddress"

TOKEN_CONTRACT = "0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"  # USDC example


ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function",
    },
]


def get_balance():

    contract = w3.eth.contract(address=TOKEN_CONTRACT, abi=ERC20_ABI)

    decimals = contract.functions.decimals().call()

    balance = contract.functions.balanceOf(WALLET).call()

    readable_balance = balance / (10 ** decimals)

    return readable_balance


def main():

    balance = get_balance()

    print("Token Balance:", balance)


if __name__ == "__main__":
    main()
