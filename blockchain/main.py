# main.py
from blockchain_loader import load_or_create_blockchain
from blockchain_viewer import display_blockchain
from blockchain_adder import add_block

def main():
    blockchain = load_or_create_blockchain()
    display_blockchain(blockchain)
    add_block(blockchain)

if __name__ == "__main__":
    main()
