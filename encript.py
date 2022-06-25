from cryptography.fernet import Fernet

def encrypt(data):
    key = Fernet.generate_key()
    answer = input('You are going to see encryption key. Y to see, N to skip: ')
    if answer.upper == 'Y' or answer == 'y':
        print(f'\n-- Store securely --\nThe key to decrypt data is: {key} \n-- Store securely --\n')
    object_key = Fernet(key)
    value = bytes(data,'utf-8')
    data_encrypted = object_key.encrypt(value)
    return data_encrypted
