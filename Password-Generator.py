#// Aloitettu 8:05 / 28.3.2025
#// Perustaa kirjaston random
import random

#//Perustetaan Listat
chosenletters = ""  # Valitut merkit tallentuu tähän. Käytetään rivillä 84.
ranlowerletters = "abcdefghijklmnopqrstuvwxyz"  # Ascii pienet kirjaimet - Default valinta. Pakollinen.
ranupperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Ascii isot kirjaimet 
rannumbers = "0123456789"  # Ascii numerot 
rannordics = "äÄöÖåÅ"  # Ascii ääkköset 
ranspecial = r"""!"#$%&*+-/:;<=>?@\^_~"""  # Ascii erikoismerkit - Lähde chatGPT (Erikoismerkit aiheuttaa konflikteja vaikka ne olisi merkkijonossa STR muodossa:)
ransentence = [
    "Iloinen", "Surullinen", "Panda", "Kettu", "Orava", "Kissa", "Koira", "Possu",
    "Lehmä", "Lammas", "Punainen", "Sininen", "Keltainen", "Vihreä", "Oranssi",
    "Pinkki", "Musta", "Valkoinen"
]
#//Tervetuloviesti//#
print("Tervetuloa satunnais-salasanan luojaan")

#//Automaattisen salasanan luoja 100% automaattinen
autojatkaminen = input("Haluatko autoomaattisesti luoda salasanan: Ei = 0 Kyllä = 1: ") #//Kysymys haluaako käyttää käyttää automaattiluojaa.
if autojatkaminen == "1":
    while autojatkaminen == "1": #//While looppi joka toistuu kunnes käyttäjä pystäyttää sen rivillä 28
        chosenletters += random.choice([str(ranlowerletters), str(rannumbers), str(rannordics), str(ransentence), str(ranspecial)]) #// Valitsee satunnaisia merkkilistoja satunnaiseen salasanaan
        ranpituus = random.randrange(8, 12) #Asettaa pituuden 8-12 välille
        password = "".join(random.choice(chosenletters) for _ in range(ranpituus)) #// Syöttää muuttujaan password satunnaisen kirjainsarjan, ja leikkaa sen sopivan pituiseksi Password-lenght parametrilla."
        print("Satunnais salasanasi on: " , password)
        autojatkaminen = input("Haluatko luoda toisen automaatti-salasanan?: Ei = 0 Kyllä = 1: ")
elif autojatkaminen == "0":
    print("Ei käytetä automaattiluojaa.")
else: 
    autojatkaminen == "0" #Failsafe
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.")
#//Valitse toivotut merkit ja kirjaimet.
print("Aloitetaan mukautus:")

#//Alustaa kysymis funktion, joka palauttaa arvon kyllä / ei. Joka taas päättää lisätäänkö esitetty merkkijono listaan.//#
def kysy_ja_lisaa(viesti, merkkijoukko):
    vastaus = input(viesti + " 0 = Ei 1 = Kyllä: ") #Kysymys dialoogi
    if vastaus == "1":
        print(f"Lisätään" , {viesti}) # < F mahdollistaa helpomman muutujien kiinitykset merkkijonoihin
        return merkkijoukko
    elif vastaus == "0":
        print(f"Ei" , {viesti}) # < F mahdollistaa helpomman muutujien kiinitykset merkkijonoihin
        return ""
    else:
        print("Ei hyväksytty syöte. Palautetaan valinta: EI.") #Failsafe
        return ""

#//Alustaa listan josta merkit poimitaan//#
chosenletters = ""

#//Kysymis funktiot//#
chosenletters += kysy_ja_lisaa("pieniä kirjaimia", ranlowerletters) #Pienet kirjaimet
chosenletters += kysy_ja_lisaa("isoja kirjaimia", ranupperletters) #Isot kirjaimet
chosenletters += kysy_ja_lisaa("numeroita", rannumbers) #Numerot
chosenletters += kysy_ja_lisaa("erikoismerkkejä", ranspecial) #Erikoismerkit
chosenletters += kysy_ja_lisaa("pohjoismaisia kirjaimia (Ä, Ö, Å)", rannordics) #Ääkköset

#//Samalle periaatteella voi lisätä lisää kenttiä tarpeen mukaan

#// Kysyy erikseen toivooko käyttäjä satunnaisia lauseita salasanaan

ransentenceKYS = input("Haluatko satunnaisia sanoja salasanaan? (Kettu, Punainen) 0 = Ei 1 = Kyllä: ")
if ransentenceKYS == "1":
    print(f"Lisätään satunnaisia sanoja")
    chosenletters
elif ransentenceKYS == "0":
    print(f"Ei lisätä satunnaisia sanoja")
else:
    print("Ei hyväksytty syöte. Palautetaan valinta: EI.") #Failsafe
    ransentenceKYS == "0"

#// Salasanan pituus

#print("DEBUG! Valitut kirjaimet" , chosenletters) #Kehitystä varten DEBUG työkalu.Aktivoi poistamalla "Hash" "#" merkki.
if ransentence == "1":
    print(ransentence)
jatkaminen = True #//valmistaa Boolean lauseen.

#//Jatkamis looppi

passwordLength = int(input("Anna salasanan pituus: ")) # Ohjelma tarkistaa syötetyn arvon. Jos arvo on numero ja yli 0 ohjelma hyväksyy arvon.
if passwordLength <= 0:
        print("Arvo pienempi kuin nolla tunnistettu syötteessä. Asetetaan sopivaan arvoon: 10")
        passwordLength = 10
else:
    print("Virheellinen syöte (ei numero). Asetetaan oletuspituus: 10")
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
       
    elif contgen == str(1): #//Kyllä: jatkaa toistoa riviltä 77
        jatkaminen == True
        print("Toistetaan luominen...")
    else: 
        print("Syötettä ei tunnistettu. Palautetaan arvo 0 / Ei") #// Failsafe-Arvo: Palauttaa nolla / ei jos syöte ei ole 0 tai 1
        jatkaminen == False
        

print("Kiitos ohjelman käytöstä ja tervetuloa uudelleen!") #// Bye bye viesti :)