import hashlib
import json
import random
from time import time
from replit import db

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Own a sword for manor defence, since that's what the Magna Carta intended", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

#Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, time):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'time': time,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
      
  
    def new_user(self):
        new = random.randrange(00000000000000000000000000000, 90000000000000000000000000000)
        return new
#make a random user numer
blockchain = Blockchain()
value1 = db["user1"]
value2 = db["user2"]
value3 = db["user3"]
value4 = db["user4"]
#Store new user number here 
t1 = blockchain.new_transaction(value1, value2, '5')
t2 = blockchain.new_transaction(value2 , value1, '1')
t3 = blockchain.new_transaction(value3, value4, '5')
blockchain.new_block(random.randrange(12345, 90000))

t4 = blockchain.new_transaction(value1, value4, '1')
t5 = blockchain.new_transaction(value3, value2, '0.5')
t6 = blockchain.new_transaction(value2, value1, '0.5')
blockchain.new_block((random.randrange(12345, 90000)))

t7 = blockchain.new_transaction(value1, value4, '1')
t8 = blockchain.new_transaction(value3, value2, '0.5')
t9 = blockchain.new_transaction(value2, value1, '0.5')
blockchain.new_block((random.randrange(12345, 90000)))
print(blockchain.chain)



