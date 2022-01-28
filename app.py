import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:7545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/stock.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x3d655c64cd5c960f077EB3507104360164A105eD'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain)
tx_hash = contract.functions.enterstock(10293,40,True).transact()
# print(message)
# # executes setPayload function
# tx_hash = contract.functions.setPayload('abc').transact()
# # waits for the specified transaction (tx_hash) to be confirmed
# # (included in a mined block)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print('tx_hash: {}'.format(tx_hash.hex()))

print(contract.functions.entries().call())