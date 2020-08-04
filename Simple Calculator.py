import time
while True:
        print('Questa è una calcolatrice.')
        time.sleep(1)
        print('Ecco le funzioni disponibili...')
        time.sleep(1)
        print('+ Per effettuare un\'Addizione, premi 1;')
        time.sleep(1)
        print('+ Per effettuare una Sottrazione, premi 2;')
        time.sleep(1)
        print('+ Per effettuare una Moltiplicazione, premi 3;')
        time.sleep(1)
        print('+ Per effettuare una Divisione, premi 4;')
        time.sleep(1)
        print('+ Per effettuare un Calcolo esponenziale, premi 5;')
        time.sleep(1)
        print('+ Per uscire dal programma digita \'ESC\';')
        time.sleep(1)
        scelta = input('Inserisci un numero corrispondente all\'azione desiderata ---> ')

        if scelta == "1":
            print('\nHai scelto: Addizione\n')
            a = (float(input('Inserisci il primo numero ---> ')))
            b = (float(input('Inserisci il secondo numero ---> ')))
            print('Il risultato della somma è: ' + str(a + b) + '---> ')
        elif scelta == "2":
            print('\nHai scelto: Sottrazione\n')
            a = (float(input('Inserisci il primo numero ---> ')))
            b = (float(input('Inserisci il secondo numero ---> ')))
            print('Il risultato della sottrazione è: ' + str(a - b) + '---> ')
        elif scelta == "3":
            print('\nHai scelto: Moltiplicazione\n')
            a = (float(input('Inserisci il primo numero ---> ')))
            b = (float(input('Inserisci il secondo numero ---> ')))
            print('Il risultato della moltiplicazione è: ' + str(a * b) + '---> ')
        elif scelta == "4":
            print('\nHai scelto: Divisione\n')
            a = (float(input('Inserisci il primo numero ---> ')))
            b = (float(input('Inserisci il secondo numero ---> ')))
            print('Il risultato della divisione è: ' + str(a / b) + '---> ')
        elif scelta == "5":
            print('\nHai scelto: Calcolo esponenziale\n')
            a = (float(input('Inserisci il primo numero ---> ')))
            b = (float(input('Inserisci il secondo numero ---> ')))
            print('Il risultato del Calcolo esponenziale è: ' + str(a ** b) + '---> ')
        elif scelta == "ESC" or "esc":
            print('\nChiusura applicazione in corso...\n')
            time.sleep(1)
            break
        loop = input('\nVuoi continuare ad usare la calcolatrice? S/N: ')
        if loop == "S" or loop == "s":
            print('''\nTorno al menu principale...

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n''')
            continue
        time.sleep(1)
        
        if loop == "N" or loop == "n":
            print('\nChiusura applicazione in corso...\n')
            time.sleep(1)
            break
        
        

