import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W',
         'X','Y','Z']

symbols=['!','@','#','$','%','^','&','*','(',')']
numbers=['1','2','3','4','5','6','7','8','9','0']

print("Welcome to password generator")
no_letters=int(input("How many letters you want in your password:"))
no_symbols=int(input("How many symbols you want in your password:"))
no_numbers=int(input("How many numbers you want in your password:"))

password_list=[]

for i in range(1,no_letters+1):
    char=random.choice(letters)
    password_list+=char
    
for i in range(1,no_symbols+1):
    sym=random.choice(symbols)
    password_list+=sym

for i in range(1,no_numbers+1):
    num=random.choice(numbers)
    password_list+=num

random.shuffle(password_list)
password='' 
for char in password_list:
    password+=char

print("your password is",password)
