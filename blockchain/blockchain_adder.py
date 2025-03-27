# blockchain_adder.py
import hashlib
import json
import os
from datetime import datetime

BLOCKCHAIN_FILE = "blockchain.json"

def add_block(blockchain):
    while True:
        nome_utente = input("Inserisci il tuo nome (oppure digita 'exit' per uscire): ").strip()
        if nome_utente.lower() == 'exit':
            break
        if not nome_utente:
            print("Nome non valido. Riprova.")
            continue

        dato_utente = input("Inserisci il dato per il nuovo blocco: ").strip()
        if not dato_utente:
            print("Dato non valido. Riprova.")
            continue

        ultimo_blocco = blockchain[-1]
        indice = ultimo_blocco["indice"] + 1  # New block's index is the previous index + 1
        hash_precedente = ultimo_blocco["hash"]  # Use the previous block's hash

        # Create a timestamp for the new block
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        
        # Combine block data to generate a unique hash string
        contenuto = str(indice) + timestamp + nome_utente + dato_utente + hash_precedente
        hash_blocco = hashlib.sha256(contenuto.encode()).hexdigest()

        nuovo_blocco = {
            "indice": indice,
            "timestamp": timestamp,
            "utente": nome_utente,
            "dato": dato_utente,
            "hash_precedente": hash_precedente,
            "hash": hash_blocco
        }
        
        blockchain.append(nuovo_blocco)
        
        # Save the updated blockchain to the file
        with open(BLOCKCHAIN_FILE, "w") as file:
            json.dump(blockchain, file, indent=4)
        
        print("Nuovo blocco aggiunto:")
        print(nuovo_blocco)
