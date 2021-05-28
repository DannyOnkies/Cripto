"""
CIFRATURA MONOALFABETICA CASUALE
CRIPTARE UNA PAROLA (pag 451)
======================================
# DATI RICHIESTI SULLA RIGA DI COMANDO
# 1 - nome script   - argv[0]
# 2 - modalità      - argv[1]
# 3 - 1° parametro  - argv[2]
# 4 - 2° parametro  - argv[3]
======================================
['K', 'E', 'Y', 'W', 'O', 'R', 'D']

['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

['D', 'A', 'N', 'I', 'E', 'L', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'M', 'K', 'J', 'H', 'G', 'F', 'C', 'B']

[ 0    1    2    3    4    5    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24]
"""

import sys
from sys import argv

error = ['Dati insufficenti', 'Dati non richiesti', 'Errore! Modalità non riconosciuta']


# MESSAGGI PER L'UTENTE
def extradata():
    print("Sulla riga di comando ci sono dati ")
    print("che non verranno utilizzati")


def usoprg():
    print("uso  : py cripto.py modo [-enc][-dec],  chiave,  nome")
    print("help : py cripto.py -h")


def helpme():
    testo = open("help.txt", 'r')
    print(testo.read())
    testo.close()


# RESTITUISCE L'ALFABETO MAIUSCOLO
def alphabet(start, end):
    # creo la lista con l'alfabeto maiuscolo
    ab = []
    for i in range(start, end, 1):
        ab.append(chr(i))
    return ab


# ELIMINO LE LETTERE DUPLICATE DALLA CHIAVE FORNITA
def erasedouble(chiave):
    wordkey = []
    # conversione in caratteri maiuscoli
    chiave_up = chiave.upper()
    for lettera in chiave_up:
        if lettera not in wordkey:
            wordkey.append(lettera)
    return wordkey


# ELIMINO DALL'ALFABETO LE LETTERE PRESENTI
# NELLA CHIAVE E POI ROVESCIO LA LISTA
def eliminachiave(key, alfabeto):
    dup = []
    for lett in alfabeto:
        if lett not in key:
            dup.append(lett)
    dup.reverse()
    return dup


# IL CICLO PRENDE UN CARATTERE DALLA
# PAROLA E LO CONVERTE NEL CORRISPONDENTE
# CARATTERE CRIPTATO
def encrypt(finale, alfabeto, parola):
    criptata = []
    word = parola.upper()
    for x in range(len(word)):
        for y in range(len(alfabeto)):
            if word[x] == alfabeto[y]:
                criptata.append(finale[y])
            elif word[x] == "'":
                criptata.append('+')
                break
            elif word[x] == '.':
                criptata.append('-')
                break
            elif word[x] == '@':
                criptata.append('*')
                break
            elif word[x] == '-':
                criptata.append('.')
                break
            elif word[x] == '_':
                criptata.append('=')
                break
    criptata = "".join(criptata)
    return criptata


# IL CICLO PRENDE UN CARATTERE DALLA PAROLA
# CRIPTATA E LO CONVERTE NEL CORRISPONDENTE
# CARATTERE ALFABETICO
def decrypt(finale, alfabeto, parola):
    criptata = []
    word = parola.upper()
    for x in range(len(word)):
        for y in range(len(finale)):
            if word[x] == finale[y]:
                criptata.append(alfabeto[y])
            elif word[x] == '+':
                criptata.append("'")
                break
            elif word[x] == '-':
                criptata.append('.')
                break
            elif word[x] == '*':
                criptata.append('@')
                break
            elif word[x] == '.':
                criptata.append('-')
                break
            elif word[x] == '=':
                criptata.append('-')
                break
    criptata = "".join(criptata)
    return criptata


# CRIPTA I CARATTERI DELLA 'PAROLA'
# PASSATA UTILIZZANDO LA 'CHIAVE'
def cripto(mode, chiave, parola):
    alfabeto = alphabet(65, 91)
    key = erasedouble(chiave)
    copia = eliminachiave(key, alfabeto)
    finale = key + copia

    if mode == '-enc' or mode == '-etxt':
        cripted = encrypt(finale, alfabeto, parola)
        return cripted
    elif mode == '-dec' or mode == '-dtxt':
        decripted = decrypt(finale, alfabeto, parola)
        return decripted
    else:
        print(error[2])
        sys.exit()


# QUESTA FUNZIONE SI OCCUPA DI CRIPTARE
# E DECRIPTARE I FILE
def cripto_txt(mode, chiave, namefile):
    fin = open(namefile, 'r')
    fout = open('mod_' + namefile, 'w')
    # LEGGO E COPIO LE LINEE IN UNA LISTA
    uno = fin.readlines()
    for i in range(len(uno)):
        rigauno = uno[i]
        wordlist = rigauno.split()
        for word in wordlist:
            wordencript = cripto(mode, chiave, word)
            fout.write(wordencript + ' ')  # AGGIUNGO UNO SPAZIO TRA LE PAROLE
        fout.write('\n')
    fout.close()
    fin.close()
    print(" File di testo salvato",fout.name)

def main():
    # IL NUMERO DI PARAMETRI PASSATI SULLA RIGA DI COMANDO DEVE ESSERE 4
    # SE E' INFERIORE A 4 MA VIENE RICHIESTO L'HELP ENTRO QUI
    if len(argv) < 4:
        if len(argv) == 2 and (argv[1] == '-h' or argv[1] == '-H'):
            helpme()
        # ALTRIMENTI VIENE AVVISATO L'UTENTE DELL'ERRORE
        else:
            print(error[0])
            usoprg()
            sys.exit()
    # SE IL NUMERO DEI PARAMETRI E' MAGGIORE DI 4 L'UTENTE VIENE AVVISATO
    elif len(argv) > 4:
        print(error[1])
        extradata()
        print(">>", cripto(argv[1], argv[2], argv[3]))
    # SE IL NUMERO DEGLI ARGOMENTI E' 4 ENTRO QUI
    else:
        if argv[1] == '-etxt' or argv[1] == '-dtxt':
            cripto_txt(argv[1], argv[2], argv[3])
        else:
            print(">>", cripto(argv[1], argv[2], argv[3]))
            # print(sys.argv)


if __name__ == '__main__':
    main()
