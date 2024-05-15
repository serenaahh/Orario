#funzione
def orario_docente(docente):
    '''
    Ritorna l'orario di un determinato docente e numero totale delle ore del docente.

    Args:
        docente (string): docente cercato dall'utente
        
    Returns:
        campi : prima riga di stampa
        ore : seconda riga di stampa
        riga : orario docente
        cont : conteggio ore totali del docente
    '''
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    #campi e ore vengono tirati fuori come liste così da non essere incluse nel ciclo di ricerca
    campi = next(file)
    ore = next(file)
    cont = 0
    for row in file:
        if docente in row:
            riga = row.split(",")
            riga.pop(0)
            for elem in riga:
                if elem != '  ':
                    cont += 1
        continue
    file.close() #chiusura file
    return campi, ore, riga, cont