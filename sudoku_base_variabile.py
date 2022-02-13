import numpy as np
import math
import os

baseValida=False
approvato=False
corretto=False
base=0

def valido(riga, colonna, candidato):
    bloccoX=riga//blocco
    bloccoY=colonna//blocco
    for i in range(base):
        if sudoku[riga][i] == candidato:
            return False
    for i in range(base):
        if sudoku[i][colonna] == candidato:
            return False
    for i in range(bloccoX*blocco, bloccoX*blocco+blocco):
        for j in range(bloccoY*blocco, bloccoY*blocco+blocco):
            if sudoku[i][j] == candidato:
                return False
    return True

def soluzione():
    for riga in range(base):
        for colonna in range(base):
            if sudoku[riga][colonna] == 0:
                for candidato in range(1, base+1):
                    if valido(riga, colonna, candidato):
                        sudoku[riga][colonna] = candidato
                        soluzione()
                        sudoku[riga][colonna] = 0                
                return
    print(f"Soluzione: \n{np.matrix(sudoku)}")

def creaSudoku():
    riga=0
    colonna=0
    while riga<base:
        print(f"Riga: {riga+1}")
        while colonna<base:
            if colonna%blocco==0:
                print(f"Blocco: {colonna//blocco+1}")
            try:
                x=int(input())
                if x<=base and x>=0:
                    sudoku[riga][colonna]=x
                    colonna+=1
                else:
                    print(f"Hai inserito un numero minore di 0 o superiore al limite consentito (che è uguale alla base),\nreinserisci un valore consentito nella casella in riga {riga+1}, colonna {colonna+1}, blocco {colonna//blocco+1}: ")
            except Exception:
                print(f"Qualcosa è andato storto, reinserisci il valore per la casella in riga {riga+1}, colonna {colonna+1}, blocco {colonna//blocco+1}: ")
        riga+=1
        colonna=0

def possibile():
    for riga in range(base):
        for colonna in range(base):
            if sudoku[riga][colonna]!=0:
                temp=sudoku[riga][colonna]
                sudoku[riga][colonna]=0
                if not valido(riga, colonna, temp):
                    sudoku[riga][colonna]=temp
                    return False
                sudoku[riga][colonna]=temp
    return True

def correzione(n):
    global corretto
    if n<=base**2:
        i=0
        while i<n:
            print(f"Casella da cambiare numero {n}")
            try:
                riga=int(input("In quale riga è la casella da cambiare? "))
                colonna=int(input("In quale colonna è la casella da cambiare? "))
                if riga<=base and colonna<=base:
                    temp=int(input(f"Inserisci il nuovo valore della casella in riga {riga}, colonna {colonna}: "))
                    if temp>base or temp<0:
                        print("Hai inserito un numero che non rispetta le regole del gioco!")
                    else:
                        sudoku[riga-1][colonna-1]=temp
                    i+=1
                else:
                    print(f"Hai inserito una coordinata impossibile, reinserisci le coordinate della casella da cambiare numero {n}")
            except Exception:
                print("Ops, qualcosa è andato storto...")
                return
    else:
        print("Vuoi cambiare più caselle di quante ce ne siano!")
        corretto=True
        return

print("Benvenuto nel risolutore di sudoku a base variabile.\nSe sbagli un valore, alla fine della prima creazione del sudoku potrai decidere di cambiare quanti valori vuoi.")
while not baseValida:
    try:
        base=float(input("Inserisci una base che sia un quadrato perfetto diverso da 0 e 1: "))  #float per evitare errore
        if math.sqrt(base)-int(math.sqrt(base)) == 0 and base!=0 and base!=1:
            baseValida = True
            base=int(base)                                                                      #riportato a int
        else:
            print("La base deve essere un quadrato perfetto maggiore diverso da 0 e 1")
    except Exception:
        print("Ops, qualcosa è andato storto...")
blocco=int(math.sqrt(base))
sudoku = [ [0] * base for i in range(base)]

creaSudoku()

while not approvato:
    approv=""
    if possibile():
        print(f"Il sudoku inserito è:\n{np.matrix(sudoku)}")
        approv=input("Sei sicuro dei tuoi inserimenti? (S/N) ")
    else:
        print(f"Attenzione, hai inserito un sudoku che non rispetta le regole del gioco:\n{np.matrix(sudoku)}")
        approv="n"
    if approv=="s":
        soluzione()
        approvato=True
    elif approv=="n":
        try:
            n=int(input("Quante caselle vuoi cambiare? "))      
        except Exception:
            print("Ops, qualcosa è andato storto...")
        correzione(n)
    else:
        print("Pefavore inserisci S per confermare o N per correggere")
os.system("pause")