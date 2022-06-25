from cryptography.fernet import Fernet

def decrypt():
    key = (input("Enter encription key: "))
    object_key = Fernet(bytes(key,'utf-8'))
    data = input("Enter data encrypted: ")
    result = object_key.decrypt(bytes(data,'utf-8'))

    print(f"Data decrypted: {result}")

