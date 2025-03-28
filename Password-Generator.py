#// Aloitettu 8:05 / 28.3.2025
#// Prewarm the libraries
import random

#//Prewarm the lists
ranletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
ranupperletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
rannumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
rannordics = ["ä", "Ä", "ö", "Ö", "å", "Å"]
ranspecial = ["!", "#", "¤", "%", "&", "/", "=", "+", "-"]
#//Welcome message//#
print("Welcome to the password generator!")



#//Choose the avaivable letters
print("Starting configuration:")

uppers = input("Add uppercase lettters to generation? 0 = No 1 = Yes: ")

if uppers == str(0): #// If no numbers
    print("No uppercase")
if uppers == str(1): #// If Yes numbers
    print("Adding Uppercaseletters")
    ranletters.append(ranupperletters)


numbers = input("Add numbers 0-9 to generation? 0 = No 1 = Yes: ")

if numbers == str(0): #// If no numbers
    print("No numbers")
if numbers == str(1): #// If Yes numbers
    print("Adding numbers")
    ranletters.append(rannumbers)
    
else: #// Backup-Failsafe (Allways defaults to 0 / no numbers)
    print("Invalid input. Defaulting to no numbers.")

nordics = input("Add nordic lettering? Ä, Ö, Å: 0 = No 1 = Yes: ")

if nordics == str(0): #// If No
    print("No nordic lettering.")
if numbers == str(1): #// If Yes
    print("Adding numbers")
    ranletters.append(rannordics)





print(ranletters)
