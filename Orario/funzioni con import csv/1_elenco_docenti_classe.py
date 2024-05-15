#elenco docenti di una data classe
import csv #import libreria csv

#funzione
def elenco_docenti(classe):
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    file_csv = csv.reader(file) #file in modalità csv
    #campi e ore vengono tirati fuori come liste così da non essere incluse nel ciclo di ricerca
    campi = next(file_csv)
    ore = next(file_csv)
    elenco = [] #elenco docenti vuoto
    for row in file_csv:
        if classe in row:
            elenco.append(row[0]) #se la classe è nella riga viene aggiunto all'elenco il primo elemento della riga (nome docente)
    file.close() #chiusura file
    return elenco

while True: #loop infinito
    #input utente
    in_classe = input('Inserire la classe [solo lettere maiuscole]: ')

    #chiamata funzione
    docenti = elenco_docenti(in_classe)

    #stampa risultato
    print(f'I docenti della classe {in_classe} sono:')
    for elem in docenti:
        print(elem)
