import pickle
import webbrowser
from cryptography.fernet import Fernet

#Writing out some information for the user to the console window
print("This is a menu based password manager that enrypts, decrypts and stores passwords\n \
Passwords are encrypted and decrypted using the fernet cryptography module\n \
Encrypted passwords are stored in a binary file and passwords will be copied to the clipboard\n \
in the format b'password' due to byte conversion\n")

#writing functions for reading and writing 

def write(username, website, password):
    #Creating a file/file object
    file = open("data.dat", "ab")

    #Generating a key for encryption
    key = Fernet.generate_key()
    f = Fernet(key)

    #Converting password into binary for fernet encryption
    passwordByt = bytes(password, "utf-8")

    #Encrypting the password
    encryptedPassword = f.encrypt(passwordByt)

    #Dumping data into a binary file
    record = (username, website, encryptedPassword, key)
    pickle.dump(record, file)
    file.close()


def read():
    file = open("data.dat", "rb")
    try:
        data = pickle.load(file)

        #Checking which password it is that is to be copied
        username = input("enter your username here: ")
        website = input("enter the website account here: ")

        if (data[0] == username and data[1] == website) :

            #Loading key used for encryption
            key = data[3]
            f = Fernet(key)

            #Decrypting using the same key
            decrypted_password = f.decrypt(data[2])
            print(f"the password is : {decrypted_password}")

            #Loading the website using the webbrowser module
            webbrowser.open(f"https://{website}.com")


    except EOFError:
        file.close()


#Menu-driven options here
print("1. Do you wish to view passwords here? ")
print("2. Do you wish to save a password here? ")

#Main body of the program
while True:
    choice = int(input("Enter your choice here: "))

    if choice == 2:
        username = input("Enter username here: ")
        website = input("Enter website name here: ")
        password = input("Enter password here: ")

        write(username, website, password)

    elif choice == 1:
        read()

    else:
        print("valid choice not selected, please try again")

    #Creating check condition to terminate infinite loop
    guess = input("do you wish to continue(y/N)")
    if guess == "n" or guess == "N":
        break
            


