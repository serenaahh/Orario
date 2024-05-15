#funzione
def disposizione_docente(docente):
    '''
    Ritorna il numero totale di ore di disposizione del docente dato.


    Args:
        docente (string): docente cercato dall'utente
        
    Returns:
        disposizione (integer): conteggio ore disposizione del docente 
    '''
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    #campi e ore vengono tirati fuori come liste così da non essere incluse nel ciclo di ricerca
    campi = next(file)
    ore = next(file)
    for row in file:
        if docente in row: #prende in considerazione solo la riga che contiene il nome del docente
            cont = 0 #contatore per ore a disposizione
            for ora in row:
                if ora == 'D': #evita di prendere in considerazione le cassi che hanno D dentro mettendo uno spazio davanti
                    cont += 1
            disposizione = [docente,cont]  #lista con nome docente e ore a disposizione
            break #evita che vengano prese in considerazione altre righe inutilmente
    file.close() #chiusura file
    return disposizione