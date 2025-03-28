#// Aloitettu 8:05 / 28.3.2025
#// Prewarm the libraries
import random

#//
ranletters = ["a", "b", "c", "d", "e", "f", "g"]

#//Welcome message//#
print("Welcome to the password generator!")



#//Choose the avaivable letters
numbers = input("Add numbers 0-9 to generation? 0 = No 1 = Yes")

if numbers == 0: #// If no numbers
    print("No numbers")
if numbers == 1: #// If Yes numbers
    print("Adding numbers")
    ranletters.append("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    
else: #// Backup-Failsafe (Allways defaults to 0 / no numbers)
    print("Invalid input. Defaulting to no numbers.")

nordics = input("Add nordic lettering? Ä, Ö, Å: 0 = No 1 = Yes")

if nordics == 0: #// If No
    print("No nordic lettering.")
if numbers == 1: #// If Yes
    print("Adding numbers")
    ranletters.append("ä", "Ä", "ö", "Ö", "å", "Å")


    print(ranletters)
