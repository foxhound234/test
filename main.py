# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import random
import math
import time
import json
import csv
import statistics
a = [["gerard", "bemee", 14], ["cichel", "ret", 45], ["artee", "aerz", 9]]

def list1():
    # Use a breakpoint in the code line below to debug your script.


    random.shuffle(a)
    i=0

    a.sort(key=lambda row: (row[1], row[1]))

    for record in a:
        for j in range(len(a[i])):

            print("prenom",a[j][0],"nom",a[j][1],"age",a[j][2],end=" ")
            print(" ")

        print()




def list2():


    random.shuffle(a)
    i=0

    a.sort(key=lambda row: (row[1], row[1]), reverse=True)

    for record in a:
        for j in range(len(a[i])):

            print("prenom",a[j][0],"nom",a[j][1],"age",a[j][2],end=" ")
            print(" ")

        print()


def list3():
    random.shuffle(a)
    i=0

    a.sort(key=lambda row: (row[1], row[2]))

    for record in a:
        for j in range(len(a[i])):

            print("prenom",a[j][0],"nom",a[j][1],"age",a[j][2],end=" ")
            print(" ")

        print()




def list4():
    random.shuffle(a)
    i=0

    a.sort(key=lambda row: (row[1], row[2]),reverse=True)

    for record in a:
        for j in range(len(a[i])):

            print("prenom",a[j][0],"nom",a[j][1],"age",a[j][2],end=" ")
            print(" ")

        print()



def grouperandom(nbperson):
  random.shuffle(a)
  i = 0
  test=0
  ungroupe=[]
  nbgroupe=0
  for record in a:

      for j in range(len(a[i])):
        test = test + 1
        ungroupe.append([a[j][0],a[j][1],a[j][2]])
        print("prenom", ungroupe[-1][0], "nom", ungroupe[-1][1], "age", ungroupe[-1][2], end=" ")
        print(" ")
        if test==nbperson :
            test=0
            print("le groupe",nbgroupe)
            nbgroupe=nbgroupe+1


def voyelle1(phrase,voyewel):

    phrase.casefold()
    count = {}.fromkeys(voyewel, 0)

    for character in phrase:
        if character in count:
         count[character] += 1
         return len(count)

def voyelle2(phrase,voyewel):

    phrase.casefold()
    count = {}.fromkeys(voyewel, 0)

    for character in phrase:
        if character in count:
         count[character] += 1
         return count


def rayoncercle(circonference):
    return circonference/2*math.pi

def perimètreducercle(rayon):
    return rayon * 2 * math.pi


def justprix():
    statut=""
    i=0
    t=45
    debut=time.time()
    prix=random.randint (0,1000)
    essai=10
    proposition=0
    tempsecoulé=0
    Resultat=[]
    while True:
        n = int(input("donnez une proposition entre 0 et 100 : "))

        if proposition==prix:
            fin=time.time()
            tempsecoulé=debut-fin
            if tempsecoulé>30:

                print("trop tard",tempsecoulé,"s", "nbessai:",essai)
                print("**********")
                Resultat.append([tempsecoulé,essai,False])
                with open('data.txt', 'a') as outfile:
                    outfile.write(json.dumps(Resultat))
                    outfile.write(",")
                    outfile.close()
            else:
                print("Vous avez gagné", tempsecoulé, "s", "nbessai:", essai)
                print("**********")
                Resultat.append([tempsecoulé, essai, True])
                with open('data.txt', 'a') as outfile:
                    outfile.write(json.dumps(Resultat))
                    outfile.write(",")
                    outfile.close()
            break
        elif essai==0:
            fin=time.time()
            tempsecoulé = debut - fin
            print("Vous avez perdu",tempsecoulé,"s","nbessai:",essai)

            print("*************")
            Resultat.append([tempsecoulé, essai, False])

            with open('data.txt', 'a') as outfile:
                outfile.write(json.dumps(Resultat))
                outfile.write(",")
                outfile.close()
            break
        else:
            print("nbessai:",essai-1)
            print("**********")
            essai=essai-1

def  affichetab():
    lesages=[]

    with open('tab2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print("Nom:",row['nom'],"Prenom:",row['prenom'],"Age:",row['age'])
            lesages.append(row['age'])


        print("la moyenne d'age de l'entreprise est :",moyenne(lesages))
def moyenne(age):
    i=0
    age = [int(i) for i in age]

    moyenneage= sum(age) / len(age)
    return moyenneage
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(affichetab())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
