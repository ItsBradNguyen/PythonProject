from cryptography.fernet import Fernet

def load_key():
    file = open("D:\Productivity\PythonProject\Beginner Project\key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("D:\Productivity\PythonProject\Beginner Project\password.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()} \n")


def view():
    with open("D:\Productivity\PythonProject\Beginner Project\password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print(user, passw)
            #print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())

while True:
    mode = input("Would you like to add a new password or view existing ones (add/view)? Press q to quit! ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode!")
        continue