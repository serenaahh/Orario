from fun_1_no_csv import elenco_docenti
from fun_2_no_csv import orario_docente
from fun_3_no_csv import disposizione_docente
from fun_4_no_csv import docenti_lezione

funzioni = [elenco_docenti, orario_docente, disposizione_docente, docenti_lezione]

#richiesta per entrata menu
x=input("Desidera accedere al menu? [s/n]: ")
#ciclo per quando l'utente da un input errato e quindi può rimetterlo
while (x!="s" and x!="S" and x!="n" and x!="N"):
    print("Input errato per l'accesso.")
    x=input("Desidera tornare al menu? [s/n]: ")
#ciclo per accedere al menu
while (x=="s" or x=="S"):
    print(f"\nMENU \nDigitare 0 per uscire dal menu \nDigitare 1 per accedere alla funzione elenco_docenti \nDigitare 2 per accedere alla funzione orario_docente \nDigitare 3 per accedere alla funzione disposizione_docente \nDigitare 4 per accedere alla funzione docenti_lezione")
    #input per scegliere una funzione del menu 
    a = int(input(">> "))
    #condizione per uscire dal menu
    if (a == 0):
        print("Arrivederci :P.")
        break
    #condizione per funzioni non esistenti
    elif (a>len(funzioni)):
        print("Funzione non esistente.")
    #condizione per entrare nel modulo menu e nella funzione main
    elif (a == 1):
        #input utente
        in_classe = input('Inserire la classe : ').upper()

        #chiamata funzione
        docenti = elenco_docenti(in_classe)

        #stampa risultato
        print(f'I docenti della classe {in_classe} sono:')
        for elem in docenti:
            print(elem)

    elif (a == 2):
        #input utente
        in_docente = input('Inserire il docente desiderato: ').upper()

        #chiamata funzione
        orario = orario_docente(in_docente)

        #ho un problema con il print dell'orario
        orario_stampa = orario #non prendo in considerazione le ore totali
        for parte in orario: #loop stampa
            if parte is orario[3]:
                continue
            else:
                print(parte)
        #print ore totali
        print(f'ore totali di {in_docente}: {orario[3]}')
        
    elif (a == 3):
        #input utente
        in_docente = input('Inserire il docente desiderato: ').upper()

        #chiamata funzione
        disp = disposizione_docente(in_docente)

        #stampa risultato
        print(disp[0] + "\nOre a disposizione: " + str(disp[1]) )

    elif (a == 4):
        #input utente
        in_ora = int(input('Inserire ora scelta: '))
        in_giorno = input('Inserire le prime 3 lettere del giorno scelto: ').lower()
        
        #chiamata funzione
        docenti = docenti_lezione(in_ora, in_giorno)

        #stampa risultato
        print(f'I docenti che hanno lezione alla {in_ora} ora il {in_giorno} sono:')
        for elem in docenti:
            print(elem)
        
    x=input("Desidera tornare al menu? [s/n]: ")
#condizione per uscire dal menu
if(x=="n" or x=="N"):
    print("Arrivederci :D.")