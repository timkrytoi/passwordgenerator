import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

num = input('Amount of passwords to generate:')
num = int(num)

lenght = input(' Input Your password lenght')
lenght = int(lenght)

print('\nhere your password:')

for pwd in range(num):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)
