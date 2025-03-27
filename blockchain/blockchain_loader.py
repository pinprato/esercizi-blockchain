# blockchain_loader.py
import hashlib
import json
import os
from datetime import datetime

BLOCKCHAIN_FILE = "blockchain.json"

def load_or_create_blockchain():
    # If the file exists, load the blockchain
    if os.path.exists(BLOCKCHAIN_FILE):
        with open(BLOCKCHAIN_FILE, "r") as file:
            blockchain = json.load(file)
    else:
        # Create the genesis block
        indice = 0
        hash_precedente = "0"
        utente = "Genesi"
        dato = "Blocco Genesi"
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        
        # Combine the block properties to create a unique string for the hash
        contenuto = str(indice) + timestamp + utente + dato + hash_precedente
        hash_blocco = hashlib.sha256(contenuto.encode()).hexdigest()
        
        # Create the blockchain with the genesis block
        blockchain = [{
            "indice": indice,
            "timestamp": timestamp,
            "utente": utente,
            "dato": dato,
            "hash_precedente": hash_precedente,
            "hash": hash_blocco
        }]
        
        # Save the blockchain to the JSON file
        with open(BLOCKCHAIN_FILE, "w") as file:
            json.dump(blockchain, file, indent=4)
    
    return blockchain
