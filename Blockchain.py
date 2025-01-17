//Work in progress

import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

        #make the genesis block
        self.newBlock(previousHash = 1, proof = 100)

    def proofOfWork(self,lastProof): ## find a number p', such that hash(pp') contains 4 zeros, where p is the previous p'
        proof = 0
        while self.validProof(lastProof, proof) is False:
            proof += 1
        return proof

    def validProof(lastProof, proof): ##validates whether hash contains 4 leading zeroes
        guess = f'{lastProof}{proof}'.encode()
        guessHash = hashlib.sha256(guess).hexdigest()
        return guessHash[:4] == "0000"

    def newBlock(self, proof, previousHash = None): #creates a new block and adds to chain

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.currentTransactions,
            'proof': proof,
            'previousHash': previousHash or self.hash(self.chain[-1]),
        }
        # reset the current list of transactions
        self.currentTransactions = []

        self.chain.append(block)
        return block


    def newTransactions(self, sender, recipient, amount): # adds a new transaction to list of transactions
         values = request.get_json()
         required = ['sender', 'recipient', 'amount']

         if not all(k in values for k in required):
             return 'Missing Values', 400

         index = blockchain.new_transaction(values['sender'], values['recipient'], values ['amount'])

         response = {'message': f'Transaction will be added to block {index}'}

         return jsonify(response), 201


    

    def hash (block): # hashes a block
        pass

    def lastBlock(self): # returns last block in chain
        return self.chain[-1]

#instansiate node
app = Flask(__name__)

#generate a globally unique address for node
nodeIdentifier = str(uuid4()).replace("-","")

#instantiate blockchain
blockchain = Blockchain()

def mine():
    lastBlock = blockchain.lastBlock
    lastProof = lastBlock['proof']
    proof = blockchain.proofOfWork(lastProof)

    #the sender is "0" to show this node has  mined a new coin

    blockchain.newTransaction(
        sender = '0',
        recipient = nodeIdentifier,
        amount = 1,
    )

    previousHash = blockchain.hash(lastBlock)
    block = blockchain.newBlock(proof, previousHash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


def newTransactions():
    return "We will add a new transaction"

def fullChain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
