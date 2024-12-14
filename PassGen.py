import random 

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 
password = " "
x = int(input("Jumlah password: "))

for i in range(x):
    password += random.choice(char) 
print("Your Password is: ", password)
