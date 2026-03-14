# Web3 Data Basics

A foundational toolkit for exploring **on-chain data** across EVM-compatible blockchains.
This repository focuses on the **core primitives of blockchain analytics**: fetching transactions, scanning wallet activity, and parsing token transfer events.

The goal is to build a **minimal research toolkit** that helps developers and analysts understand how raw blockchain data works before building more advanced analytics tools.

---

## Overview

Blockchain data is public but often difficult to work with directly.
This project demonstrates how to access and analyze on-chain data using Python.

Key capabilities included in this repository:

* Fetch wallet transaction history
* Scan wallet activity (incoming vs outgoing transactions)
* Parse ERC-20 token transfer events
* Retrieve token balances from smart contracts
* Export structured datasets for analysis

These components form the **foundation for more advanced Web3 analytics tools**, such as:

* whale trackers
* wallet profit analyzers
* DeFi analytics dashboards
* DEX trading behavior analysis

---

## Repository Structure

```
web3-data-basics
│
├── fetch_transactions.py        # Fetch transaction history for a wallet
├── scan_wallet.py               # Analyze wallet activity
├── parse_token_transfers.py     # Extract ERC20 transfer events
├── token_balance_checker.py     # Check token balances
│
├── data
│   ├── raw                      # Raw API responses
│   └── processed                # Structured datasets
│
└── README.md
```

---

## Requirements

Python 3.9+

Install dependencies:

```
pip install -r requirements.txt
```

Example dependencies:

```
web3
requests
pandas
python-dotenv
```

---

## Setup

Create a `.env` file with your API credentials.

Example:

```
RPC_URL=https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY
ETHERSCAN_API_KEY=YOUR_API_KEY
```

---

## Usage

### 1. Fetch Wallet Transactions

Retrieve the transaction history of a wallet.

```
python fetch_transactions.py
```

Output:

```
data/raw/wallet_transactions.json
```

---

### 2. Scan Wallet Activity

Analyze wallet activity metrics such as:

* total transactions
* incoming transactions
* outgoing transactions

Run:

```
python scan_wallet.py
```

---

### 3. Parse Token Transfers

Extract ERC-20 transfer events from transaction logs.

```
python parse_token_transfers.py
```

Output dataset:

```
data/processed/token_transfers.csv
```

Fields:

* token symbol
* sender
* receiver
* transfer amount
* timestamp

---

### 4. Check Token Balances

Query token balances directly from smart contracts.

```
python token_balance_checker.py
```

Output:

```
token balance
contract address
wallet address
```

---

## Example Use Cases

This toolkit can be extended to build more advanced Web3 analytics tools.

Examples:

* Whale transaction monitoring
* Wallet portfolio trackers
* DeFi trading analysis
* Token flow analytics

---

## Learning Objectives

By working through this repository you will learn:

* how blockchain transactions are structured
* how ERC-20 token transfers are recorded
* how to interact with blockchain RPC endpoints
* how to convert raw on-chain data into structured datasets

---

## Future Extensions

Planned improvements:

* multi-chain support
* automated whale detection
* DEX trade parsing
* wallet profit & loss analytics

---

## License

MIT License

---

## Author

Built for developers and researchers exploring **on-chain data analytics in Web3**.
