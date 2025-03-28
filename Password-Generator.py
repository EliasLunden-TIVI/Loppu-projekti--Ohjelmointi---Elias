#// Aloitettu 8:05 / 28.3.2025
#// Perustaa kirjaston random
import random

#//Perustetaan Listat
chosenletters = [] #// Valitut merkit tallentuu tähän. Käytetään rivillä 84.
ranlowerletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"] #Ascii pienent kirjaimet - Default valinta. Pakollinen.
ranupperletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"] #Ascii isot kirjaimet 
rannumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] #Ascii numerot 
rannordics = ["ä", "Ä", "ö", "Ö", "å", "Å"] #Ascii ääkköset 
ranspecial = ["!", "#", "¤", "%", "&", "/", "=", "+", "-", "@"] #Ascii erikoismerkit
ransentence = ["Iloinen", "Surullinen", "Panda", "Kettu", "Orava", "Kissa", "Koira", "Possu", "Lehmä", "Lammas", "Punainen", "Sininen", "Keltainen", "Vihreä", "Oranssi", "Pinkki", "Musta", "Valkoinen", ""] #Lauselista
#//Tervetuloviesti//#
print("Tervetuloa satunnais-salasanan luojaan")

#//Valitse toivotut merkit ja kirjaimet.
print("Aloitetaan mukautus:")

#// Pienet kirjaimet
lowers = input("Haluatko pieniä kirjaimia salasanaan? 0 = Ei 1 = Kyllä: ")
#//If-else
if lowers == str(0): #// Ei
    print("Ei pieniä kirjaimia")
elif lowers == str(1): #// Kyllä
    print("Sisältää pieniä krijaimia")
    chosenletters = chosenletters + ranlowerletters
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")
#// Isot kirjaimet 
uppers = input("Haluatko isoja kirjaimia salasanaan? 0 = Ei 1 = Kyllä: ")
#//If-else
if uppers == str(0): #// Ei
    print("Ei isoja kirjaimia")
elif uppers == str(1): #// Kyllä
    print("Lisätään isoja kirjaimia")
    chosenletters = chosenletters + ranupperletters
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")

#// Numero kirjaimet
numbers = input("Haluatko numeroita 0 - 9 salasanaan? 0 = Ei 1 = Kyllä: ")
#//If-else
if numbers == str(0): #// Ei
    print("Ei numeroita")
elif numbers == str(1): #// Kyllä
    print("Lisätään numeroita")
    chosenletters = chosenletters + rannumbers
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")

#//Erikois merkit
specials = input("Haluatko erikoismerkkejä salaasnaan? #, !, %: 0 = Ei 1 = Kyllä: ")
#//If-else
if specials == str(0): #// Ei
    print("Ei erikoismerkkejä")
elif numbers == str(1): #// Kyllä
    print("Lisätään erikoismerkkejä")
    chosenletters = chosenletters + ranspecial
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")
#//ÄÄKÖSET
nordics = input("Haluatko Pohjoismaan kirjaimet (ÄÄKÖSET)? Ä, Ö, Å: 0 = Ei 1 = Kyllä: ")
#//If-else
if nordics == str(0): #// Ei
    print("Ei ÄÄKKÖ:siä")
elif numbers == str(1): #// Kyllä
    print("Lisätään ÄÄKKÖ:set")
    chosenletters = chosenletters + rannordics
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")
#//SANAT
sanat = input("Haluatko salasanaan satunnaisia sanoja? Kissa, Koira: 0 = Ei 1 = Kyllä: ")
#//If-else
if sanat == str(0): #// Ei
    print("Ei sanoja")
elif sanat == str(1): #// Kyllä
    print("Lisätään sanoja")
    chosenletters = chosenletters + ransentence
else: #// Backup-Failsafe (Palauttaa aina nolla / ei)
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")

#// Salasanan pituus

print("DEBUG! Valitut kirjaimet" , chosenletters)
jatkaminen = True #//valmistaa Boolean lauseen.

#//Jatkamis looppi
while jatkaminen == True:

    passwordLength = int(input("Syötä toivottu pituus salasanalle: "))
    if passwordLength <= 0:
        print("Arvo pienempi kuin nolla tunnistettu syötteessä. Asetetaan sopivaan arvoon: 10")
        passwordLength = 10

    password = "".join(random.choice(chosenletters) for _ in range(passwordLength)) #// Syöttää muuttujaan password satunnaisen kirjainsarjan, ja leikkaa sen sopivan pituiseksi Password-lenght parametrilla."

    print("Salasanasi on:" , password) #//Tulostaa salasanan käyttäjälle.

    #// Jatkamis pyyntö

    contgen = input("Haluatko luoda uuden salasanan samoilla kriteereillä?: 0 = Ei 1 = Kyllä: ") #//ContGEN = Continiue Generation

    if contgen == str(0): #// Ei: Lopettaa toiston ja ohjelman
        jatkaminen == False
        break
    elif contgen == str(1): #//Kyllä: jatkaa toistoa riviltä 77
        jatkaminen == True
        print("Toistetaan luominen...")
    else: 
        print("Syötettä ei tunnistettu. Palautetaan arvo 0 / Ei") #// Failsafe-Arvo: Palauttaa nolla / ei jos syöte ei ole 0 tai 1
        jatkaminen == False
        break

print("Kiitos ohjelman käytöstä ja tervetuloa uudelleen!") #// Bye bye viesti :)