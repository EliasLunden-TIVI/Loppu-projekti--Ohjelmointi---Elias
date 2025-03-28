#// Aloitettu 8:05 / 28.3.2025
#// Perustaa kirjaston random
import random

#//Perustetaan Listat
chosenletters = []
ranlowerletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"] #Ascii pienent kirjaimet - Default valinta. Pakollinen.
ranupperletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"] #Ascii isot kirjaimet 
rannumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #Ascii numerot 
rannordics = ["ä", "Ä", "ö", "Ö", "å", "Å"] #Ascii ääkköset 
ranspecial = ["!", "#", "¤", "%", "&", "/", "=", "+", "-"] #Ascii erikoismerkit
#//Tervetuloviesti//#
print("Tervetuloa satunnais-salasanan luojaan")

#//Valitse toivotut merkit ja kirjaimet.
print("Aloitetaan mukautus:")

#// Pienet kirjaimet
lowers = input("Haluatko pieniä kirjaimia salasanaan? 0 = Ei 1 = Kyllä: ")

if lowers == str(0): #// Ei
    print("Ei pieniä kirjaimia")
elif lowers == str(1): #// Kyllä
    print("Sisältää pieniä krijaimia")
    chosenletters = chosenletters + ranlowerletters
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")
#// Isot kirjaimet 
uppers = input("Haluatko isoja kirjaimia salasanaan? 0 = Ei 1 = Kyllä: ")

if uppers == str(0): #// Ei
    print("Ei isoja kirjaimia")
elif uppers == str(1): #// Kyllä
    print("Lisätään isoja kirjaimia")
    chosenletters = chosenletters + ranupperletters
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")

#// Numero kirjaimet
numbers = input("Add numbers 0-9 to generation? 0 = No 1 = Yes: ")

if numbers == str(0): #// Ei
    print("Ei numeroita")
elif numbers == str(1): #// Kyllä
    print("Lisätään numeroita")
    chosenletters = chosenletters + rannumbers
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")

#//Erikois merkit
specials = input("Add special charecters? #, !, %: 0 = No 1 = Yes: ")

if specials == str(0): #// Ei
    print("Ei erikoismerkkejä")
elif numbers == str(1): #// Kyllä
    print("Lisätään erikoismerkkejä")
    chosenletters = chosenletters + ranspecial
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")

nordics = input("Haluatko Pohjoismaan kirjaimet (ÄÄKÖSET)? Ä, Ö, Å: 0 = No 1 = Yes: ")

if nordics == str(0): #// Ei
    print("Ei ÄÄKKÖ:siä.")
elif numbers == str(1): #// Kyllä
    print("Lisätään ÄÄKKÖ:set")
    chosenletters = chosenletters + rannordics
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")

#// Salasanan pituus

print("DEBUG! Valitut kirjaimet" , chosenletters)

passwordLength = int(input("Input desired lenght : "))

password = "".join(random.choice(chosenletters) for _ in range(passwordLength)) #// Syöttää muuttujaan password satunnaisen kirjainsarjan, ja leikkaa sen sopivan pituiseksi Password-lenght parametrilla."

print("Salasanasi on:" , password) #//Tulostaa salasanan käyttäjälle.

