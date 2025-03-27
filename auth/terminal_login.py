import hashlib
import json

def load_users():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

nomeutente = input("Inserire nome utente: ")
password = input("Inserire password: ")

encrypted_password = hashlib.sha256(password.encode()).hexdigest()

users = load_users()

# Check for matching username and password
login_success = any(
    user['username'] == nomeutente and user['password'] == encrypted_password
    for user in users
)

if login_success:
    print(f"Ciao {nomeutente}")
else:
    print("Username o password errati")