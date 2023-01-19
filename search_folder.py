from tkinter import Tk
from tkinter.filedialog import askdirectory
import os


path = askdirectory(title='Select Folder') 

print("Pretraga fajlova u folderu")
print("\n")
print("Dobrodošli")
print("\n")

def choose():
    print("1. Ispis svih fajlova")
    print("2. Pretraga po ekstenziji")
    print("3. Pretraga po nazivu")
    print("0. Kraj")
    print("\n")
    return int(input("Vaš izbor: "))


def countFiles():
    list = os.listdir(path)
    number_files = len(list)
    return print ("Ukupan broj fajlova u direktorijumu: " + str(number_files))


def findFiles(filename, path):
    result = []
    
    for root, dir_, files in os.walk(path):
        for file in files:
            if filename in file:
                result.append(file)
    return result


def openFiles():
    fileToRead = str(input("Unesite naziv fajla za čitanje: "))
    fNameAndLocation = path + "/" + fileToRead
    if fileToRead.endswith(".txt"):
        with open(fNameAndLocation, mode="r", encoding='utf-8') as f:
            data = f.read()
            print(data)
    else:
        print("Nije moguće pročitati fajl.")
    #return f

def readFile():
    print("a. Da")
    print("b. Ne")
    selectToRead = str(input("Da li želite da otvorite neki fajl za čitanje?"))
    if selectToRead == "a":
        openFiles()
    elif selectToRead == "b":
        print("U redu.")
    else:
        print("Niste izabrali validnu opciju.")


while True:
    choice = choose()

    if choice == 1:
        print("Ispis svih fajlova")
        countFiles()
        for root, dir_, files in os.walk(path):
            for file in files:
                print(file)
        print("\n")     

    elif choice == 2:
        print("Pretraga po ekstenziji")
        fileEnd = str(input("Unesite eksteziju koju želite da pretražite: " ))
        countFiles()

        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(fileEnd):
                    print(str(file))
        
            readFile()

    elif choice == 3:
        print("Pretraga po nazivu")
        countFiles()
        name = str(input("Unesite reč za pretragu: "))
        print(findFiles(name, path))
        readFile()
            
    elif choice == 0:
        print("Kraj programa.")
        break
    else:
        print("Nepostojeća opcija.")