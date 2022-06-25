from encript import encrypt
from decript import decrypt

option = int(input('encrypt (1) or decrypt (2). Enter option number: '))
while option:
    if option == 1:
        data = input('\nData who want to encrypt -> ')
        result = encrypt(data)
        print(f'Your data is encrypted: {result}')
        break
    elif option == 2:
        decrypt()
        break
    else:
        print('Inconrrect option. Select 1 or 2\n')
        option = int(input('encrypt (1) or decrypt (2). Enter option number: '))
