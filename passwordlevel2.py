#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
str=[]
print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
for n in range(0,int(nr_letters)): 
  str.append(random.choice(letters))


nr_symbols = int(input(f"How many symbols would you like?\n"))
for n in range(0,int(nr_symbols)): 
  str.append(random.choice(symbols))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for n in range(0,int(nr_numbers)): 
  str.append(random.choice(numbers))
random.shuffle(str)
password=""
for eachchar in str:
  password+=eachchar

print(f"You can use    {password}     as your strong  password")
