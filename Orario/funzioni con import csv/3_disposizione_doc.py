#orario di un determinato docente e numero totale delle ore del docente
import csv #import libreria csv

#funzione
def disposizione_docente(docente):
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    file_csv = csv.reader(file) #file in modalità csv
    #campi e ore vengono tirati fuori come liste così da non essere incluse nel ciclo di ricerca
    campi = next(file_csv)
    ore = next(file_csv)
    for row in file_csv:
        if docente in row[0]: #prende in considerazione solo la riga che contiene il nome del docente
            cont = 0 #contatore per ore a disposizione
            for ora in row:
                if ' D' in ora: #evita di prendere in considerazione le cassi che hanno D dentro mettendo uno spazio davanti
                    cont += 1
            disposizione = [docente,cont]  #lista con nome docente e ore a disposizione
            break #evita che vengano prese in considerazione altre righe inutilmente
    file.close() #chiusura file
    return disposizione

while True: #loop infinito
    #input utente
    in_docente = input('Inserire il docente [tutto in maiuscolo]: ') 

    #chiamata funzione
    disp = disposizione_docente(in_docente)

    #stampa risultato
    print(disp[0] + "\nOre a disposizione: " + str(disp[1]) )
