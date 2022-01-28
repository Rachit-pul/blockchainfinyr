from flask_cors import CORS
from flask import Flask, request, redirect, Response ,jsonify
import  json
from web3 import Web3, HTTPProvider
from flask import render_template

def getContract():
    blockchain_address = 'http://127.0.0.1:7545'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'build/contracts/stock.json'
    deployed_contract_address = '0x3d655c64cd5c960f077EB3507104360164A105eD'
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']
    contr = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    return contr


app = Flask(__name__)
CORS(app)

@app.route('/add',methods = ['POST','GET'])
def adding():
    result = request.args.to_dict()
    if len(result) == 0:
        return render_template('form.html')
    print("I AM HERE")
    if result['condition'] == 'on':
        result['condition'] = True
    else:
        result['condition'] = False
    print((result))
    contract = getContract()
    tx_hash = contract.functions.enterstock(int(result['id']),int(result['amount']),result['condition']).transact()
    return render_template('hash.html', hash = str(tx_hash))

@app.route('/', methods = ['POST','GET'])
def worker():
    contract = getContract()
    totalentries = contract.functions.entries().call()
    good_condition_amt = 0
    print(totalentries)
    for i in range(0,int(totalentries)):
        stockentry = contract.functions.return_data(i).call()
        if(stockentry[2]):
            good_condition_amt += stockentry[1]
    index_data = {
        'total':totalentries,
        'good': good_condition_amt,
    },
    print(good_condition_amt)
    return render_template('index.html',total = totalentries,good = good_condition_amt)

if __name__ == '__main__':
	# run!
	app.run()