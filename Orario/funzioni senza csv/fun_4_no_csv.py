#funzione
def docenti_lezione(ora,giorno):
    '''
    Ritorna l'elenco dei docenti attivi l'ora e il giorno dati dall'utente.


    Args:
        ora (integer): ora data dall'utente (da 1 a 8)
        giorno (string): prime 3 lettere del giorno dato dall'utente
        
    Returns:
        elenco (list): lista nomi docenti che hanno lezione il dato giorno alla data ora
    '''

    giorni = ('lun','mar','mer','gio','ven')
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    campi = next(file)
    ore = next(file)
    elenco = []
    if giorno in giorni:
        numero_iniziale = 5*giorni.index(giorno)
    else:
        print('Errore')
    cell = numero_iniziale + ora #posizione dell'elemento da scansionare
    for row in file: #scansione
        row = row.split(',')
        try:
            if  '  ' in row[cell]: #se la cella è vuota il docente non ha lezione
                continue
            else:
                nome_docente = row.pop(0)
                elenco.append(nome_docente)
        except IndexError: #quando il valore della variabile 'cell' arriva ad essere maggiore dell'indice della lista
            continue
    file.close() #chiusura file
    return elenco

