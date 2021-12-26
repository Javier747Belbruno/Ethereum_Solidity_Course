from solcx import compile_standard, install_solc
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()
import os


with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    print(simple_storage_file)

install_solc("0.6.0")
# Compile the source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}},
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Search on json for bitcode and abi
# get bitcode
bitcode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]
# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Connect to local testrpc
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# get chain id from testrpc
chain_id = w3.eth.chainId
# chain_id = 1337
my_address = "0x79cB714b7fD466D435B61feC38D8DaCD04cc1b4f"
# sign transaction - add 0x to the address
# private_key = "0x306ceae369a8d3154433c267bab9ced2fbc79c2a05cf460e623b1294c4bcc093"
private_key = os.environ.get("private_key")

# 1.Build the contract deployment transaction
contract = w3.eth.contract(abi=abi, bytecode=bitcode)
# 2.Create the transaction
#   a. Get the nonce (from latest transaction)
nonce = w3.eth.getTransactionCount(my_address)
#   b. Build the transaction
txn = contract.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
        "chainId": chain_id,
    }
)
# 3. Sign the transaction
signed = w3.eth.account.signTransaction(txn, private_key)

#   c. Send the transaction to the network
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)

#  d. Wait for the transaction to be mined
receipt = w3.eth.waitForTransactionReceipt(tx_hash)

#  e. Print the transaction hash
print("tx_hash:", tx_hash.hex())

# Work with the contract
# We need the contract address to interact with the contract
# and contract ABI to decode the events
simple_contract = w3.eth.contract(
    address=receipt.contractAddress,
    abi=abi,
)
print(abi)
# Transact or Call
print(simple_contract.functions.retrieve().call())
# print(simple_contract.functions.store(42).transact())

store_tx = simple_contract.functions.store(42).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1,
        "chainId": chain_id,
    }
)
signed_store_tx = w3.eth.account.signTransaction(store_tx, private_key)
send_tx = w3.eth.sendRawTransaction(signed_store_tx.rawTransaction)
# wait for the transaction to be mined
receipt_tx = w3.eth.waitForTransactionReceipt(send_tx)
print(simple_contract.functions.retrieve().call())
