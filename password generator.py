import random

print('Welcome To Your Passowrd Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(),.?'

number = input('Amount of passwords to generate: ')
number = int(number)


length = input('Input your Password length: ')
length = int(length)


print('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)

