#elenco docenti di una data classe
import csv #import libreria csv

#funzione
def docenti_lezione(ora,giorno):
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    file_csv = csv.Dictreader(file) #file in modalità csv
    
    file.close() #chiusura file
    return elenco

while True: #loop infinito
    #input utente
    in_ora = input('Inserire ora: ')
    in_giorno = input('Inserire giorno: ')
    
    #chiamata funzione
    docenti = docenti_lezione(in_ora, in_giorno)

    #stampa risultato
    print(f'I docenti che hanno lezione alla {in_ora} ora il {in_giorno} sono:')
    for elem in docenti:
        print(elem)
