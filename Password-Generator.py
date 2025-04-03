#// Aloitettu 8:05 / 28.3.2025
#// Perustaa kirjaston random
import random

#//Perustetaan Listat
chosenletters = ""  # Valitut merkit tallentuu tähän. Käytetään rivillä 84.
ranlowerletters = "abcdefghijklmnopqrstuvwxyz"  # Ascii pienet kirjaimet - Default valinta. Pakollinen.
ranupperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Ascii isot kirjaimet 
rannumbers = "0123456789"  # Ascii numerot 
rannordics = "äÄöÖåÅ"  # Ascii ääkköset 
ranspecial = "!#¤%&/=+-@"  # Ascii erikoismerkit
ransentence = [
    "Iloinen", "Surullinen", "Panda", "Kettu", "Orava", "Kissa", "Koira", "Possu",
    "Lehmä", "Lammas", "Punainen", "Sininen", "Keltainen", "Vihreä", "Oranssi",
    "Pinkki", "Musta", "Valkoinen"
]
#//Tervetuloviesti//#
print("Tervetuloa satunnais-salasanan luojaan")

#//Valitse toivotut merkit ja kirjaimet.
print("Aloitetaan mukautus:")

#//Alustaa kysymis funktion, joka palauttaa arvon kyllä / ei. Joka taas päättää lisätäänkö esitetty merkkijono listaan.//#
def kysy_ja_lisaa(viesti, merkkijoukko):
    vastaus = input(viesti + " 0 = Ei 1 = Kyllä: ") #Kysymys dialoogi
    if vastaus == "1":
        print(f"Lisätään" , {viesti})
        return merkkijoukko
    elif vastaus == "0":
        print(f"Ei" , {viesti})
        return ""
    else:
        print("Ei hyväksytty syöte. Palautetaan valinta: EI.") #Failsafe
        return ""

#//Alustaa listan josta merkit poimitaan//#
chosenletters = ""

#//Kysymis funktiot//#
chosenletters += kysy_ja_lisaa("pieniä kirjaimia", ranlowerletters)
chosenletters += kysy_ja_lisaa("isoja kirjaimia", ranupperletters)
chosenletters += kysy_ja_lisaa("numeroita", rannumbers)
chosenletters += kysy_ja_lisaa("erikoismerkkejä", ranspecial)
chosenletters += kysy_ja_lisaa("pohjoismaisia kirjaimia (Ä, Ö, Å)", rannordics)

#// Kysyy erikseen toivooko käyttäjä satunnaisia lauseita salasanaan

ransentenceKYS = input("Haluatko satunnaisia sanoja salasanaan? (Kettu, Punainen)" )
if ransentenceKYS == "1":
    print(f"Lisätään satunnaisia sanoja")
    chosenletters
elif ransentenceKYS == "0":
    print(f"Ei lisätä satunnaisia sanoja")
else:
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.") #Failsafe
    ransentenceKYS == "0"

#// Salasanan pituus

print("DEBUG! Valitut kirjaimet" , chosenletters)
if ransentence == "1":
    print(ransentence)
jatkaminen = True #//valmistaa Boolean lauseen.

#//Jatkamis looppi
while jatkaminen == True:

    passwordLength = int(input("Syötä toivottu pituus salasanalle: "))
    if passwordLength <= 0:
        print("Arvo pienempi kuin nolla tunnistettu syötteessä. Asetetaan sopivaan arvoon: 10")
        passwordLength = 10

    password = "".join(random.choice(chosenletters) for _ in range(passwordLength)) #// Syöttää muuttujaan password satunnaisen kirjainsarjan, ja leikkaa sen sopivan pituiseksi Password-lenght parametrilla."

    #// Lisää satunnaisen sanan 
    if ransentenceKYS == "1":
        ranWord = random.choice(ransentence)
        insert_position = random.randint(0, len(password))  #//Valitsee kohdan sanan lisäämiseen salasanan indeksistä.
        password = password[:insert_position] + ranWord + password[insert_position:]
    else:
        print("Ei lisätä sanoja:")

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