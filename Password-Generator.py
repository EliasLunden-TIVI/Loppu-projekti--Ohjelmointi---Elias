#// Aloitettu 8:05 / 28.3.2025
#// Prewarm the libraries
import random

#//Prewarm the lists
ranletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"] #Ascii lowercase - Default
ranupperletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"] #Ascii Uppercase 
rannumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #Ascii numbers 
rannordics = ["ä", "Ä", "ö", "Ö", "å", "Å"] #Ascii nordics 
ranspecial = ["!", "#", "¤", "%", "&", "/", "=", "+", "-"] #Ascii special
#//Welcome message//#
print("Welcome to the password generator!")



#//Choose the avaivable letters
print("Starting configuration:")

#// Uppercase letters
uppers = input("Add uppercase lettters to generation? 0 = No 1 = Yes: ")

if uppers == str(0): #// If no uppercase
    print("No uppercase")
if uppers == str(1): #// If Yes uppercase
    print("Adding Uppercaseletters")
    ranletters.append(ranupperletters)

else: #// Backup-Failsafe (Allways defaults to 0 / no uppercase)
    print("Invalid input. Defaulting to no uppercase.")

#// Number letters
numbers = input("Add numbers 0-9 to generation? 0 = No 1 = Yes: ")

if numbers == str(0): #// If no numbers
    print("No numbers")
if numbers == str(1): #// If Yes numbers
    print("Adding numbers")
    ranletters.append(rannumbers)

else: #// Backup-Failsafe (Allways defaults to 0 / no numbers)
    print("Invalid input. Defaulting to no numbers.")

#//Specials
specials = input("Add special charecters? #, !, %: 0 = No 1 = Yes: ")

if specials == str(0): #// If No
    print("No special charecters.")
if numbers == str(1): #// If Yes
    print("Adding special charecters")
    ranletters.append(rannordics)

else: #// Backup-Failsafe (Allways defaults to 0 / no special charecters)
    print("Invalid input. Defaulting to no special charecters.")

nordics = input("Add nordic lettering? Ä, Ö, Å: 0 = No 1 = Yes: ")

if nordics == str(0): #// If No
    print("No nordic lettering.")
if numbers == str(1): #// If Yes
    print("Adding numbers")
    ranletters.append(rannordics)

else: #// Backup-Failsafe (Allways defaults to 0 / no nordics)
    print("Invalid input. Defaulting to no nordics.")


#// Pasword lenght
passwordLenght = input("Enter number value for password lenght: ")


print(ranletters)
