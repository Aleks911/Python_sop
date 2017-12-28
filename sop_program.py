# -*-coding:UTF-8 -*-

import pymysql
from password import *

class DBconn:
    def __init__(self):
        self.conn = pymysql.connect(host,conntype,password,database)
        self.cursor = self.conn.cursor()
        print("Połączenie z BD ustanowione")  
        
        self.welcome()       

    def welcome(self):
        print ("""
 _______  _______  _______                  
(  ____ \(  ___  )(  ____ )        |\     /|
| (    \/| (   ) || (    )|        | )   ( |
| (_____ | |   | || (____)|        | |   | |
(_____  )| |   | ||  _____)        | |   | |
      ) || |   | || (              | |   | |
/\____) || (___) || )              | (___) |
\_______)(_______)|/               (_______)
                                            
 _______ _________ _______  _______  _______  _______ 
(       )\__   __/(  ____ )(  ___  )(  ____ \(  ___  )
| () () |   ) (   | (    )|| (   ) || (    \/| (   ) |
| || || |   | |   | (____)|| (___) || (_____ | (___) |
| |(_)| |   | |   |     __)|  ___  |(_____  )|  ___  |
| |   | |   | |   | (\ (   | (   ) |      ) || (   ) |
| )   ( |___) (___| ) \ \__| )   ( |/\____) || )   ( |
|/     \|\_______/|/   \__/|/     \|\_______)|/     \|
                                                      
         __________________ _______  _ 
|\     /|\__   __/\__   __/(  ___  )( )
| )   ( |   ) (      ) (   | (   ) || |
| | _ | |   | |      | |   | (___) || |
| |( )| |   | |      | |   |  ___  || |
| || || |   | |      | |   | (   ) |(_)
| () () |___) (___   | |   | )   ( | _ 
(_______)\_______/   )_(   |/     \|(_) 
""")
        
        while True:
                    
            login = input("Aby się zalogować, podaj email: ")
            haslo1 = input("Podaj hasło: ")     
            # albo '%s' , albo %r
            self.cursor.execute("SELECT * FROM logowanie where email = %r and haslo = %r;" % (login, haslo1))
            result = self.cursor.fetchall()
            if (result):
                print('%3s|%15s|%15s|%12s|%10s' % ('id','email','haslo','nip','kod_upr\n'))        
                for row in result:
                    id = row[0]
                    email = row[1]
                    haslo = row[2]
                    self.nip = row[4]
                    uprawnienie = row[3]
                    print('%3i|%15s|%15s|%12s|%10s|' % (id,email,haslo,self.nip,uprawnienie))
        
                     
                    while (result): 
                        if (uprawnienie == 'k'):
                            c = input("Menu: \n(W)yświetl faktury \n(Q)uit\n")
                            if(c.upper() == 'W'):
                                self.fakturyk()                        
                            elif(c.upper() == 'Q'):
                                self.welcome()
                            
                            else:
                                print('Błędny wybór')
                                break
                            
                        elif (uprawnienie == 'p'):
                            ad = input("Menu: \n(F)akturowanie \n(K)lienci \n(P)ojazdy \n(Q)uit\n")
                            if(ad.upper() == 'F'):
                                fw = input("Menu: \n(U)twórz fakturę \n(E)dytuj fakturę \n(W)yświetl faktury \n(P)owrót\n")
                                if (fw.upper() == 'U'):
                                    mw = input("(N)agłówek \n(D)etale\n")
                                    if (mw.upper() =='N'):
                                        self.fnag()
                                    #elif (mw.upper() =='D'):
                                        
                                        
                                elif (fw.upper() == 'W'):
                                    self.fakd()
                                elif(fw.upper() == 'P'):
                                    break
                                
                            elif(ad.upper() == 'P'):
                                poj = input("(D)odaj\n (E)dytuj\n (U)suń\n (W)yświetl\n (P)owrót\n")
                                
                                if (poj.upper() == "W"):
                                    self.pojazdyW()                                
                                
                                if (poj.upper() == "D"):
                                    self.pojazdyD()
                                    
                                if (poj.upper() == "E"):
                                    self.pojazdyE()
                                
                                if (poj.upper() == "U"):
                                    self.pojazdyU()
                                    
                                if (poj.upper() == "P"):
                                    break                                    
                                    
                            elif(ad.upper() == 'Q'):                                
                                self.welcome()                                
                                        
                                           
                            elif(ad.upper() == 'K'):
                                kl = input("Menu: \n(W)yświetl \n(D)odaj \n(E)dytuj \n(U)suń \n(P)owrót\n")
                                if (kl.upper() == "W"):
                                    self.kwys()
                                  
                                    continue
                                else:
                                    print("Błędny wybór")
                            elif(ad.upper() == 'P'):
                                break
                                
            else:
                print("Błędny login lub hasło")
                self.welcome() 
                
                                    
    def fakturyk (self): #wyświtlanie faktur klient
        self.cursor.execute("select f.nr_fak, f.nr_rej, f.przebieg, f.data_fak from klienci as k, faktury as f where k.nip ='" +str(self.nip)+"'")
        resultk = self.cursor.fetchall()                         
        print('%10s|%10s|%10s|%12s' % ('nr_fak','nr_rej','przebieg','data_fak\n'))
        for row in resultk:
            nr_fak = row[0]
            nr_rej = row[1]
            przebieg = row[2]
            data_fak = row[3]                        
            print('%10i|%10s|%10i|%12s' % (nr_fak,nr_rej,przebieg,data_fak))                    
        
    def kwys (self): #wyświtlanie danych klienta
        idk = input("Podaj id klienta\n")
        print("----------------------------------------------------------------------")
        self.cursor.execute('SELECT * FROM klienci where id = ' + "'" + idk + "';")
        result = self.cursor.fetchall()
        print("----------------------------------------------------------------------")
        print('%10s|%20s|%20s|%12s' % ('id','nazwa','adres', 'NIP'))
        for row in result:
            id = row[0]
            nazwa = row[1]
            adres = row[2]
            nip = row[3]
            print('%10i|%20s|%20s|%12s' % (id,nazwa,adres,nip))
            print("------------------------------------------------------------------")        
    
    def pojazdyW (self): #wyświetlanie pojazdów po nr. rej
        nrej = input("Wpisz numer rejestracyjny\n")        
        self.cursor.execute('SELECT * FROM pojazdy WHERE nr_rej = ' + "'" + nrej + "';")
        result = self.cursor.fetchall()        
        print('%10s|%11s|%11s|%11s|%20s|%14s' % ('id','NUMER REJ.','ID KLIENTA', 'MARKA','NUMER VIN','ROK PRODUKCJI'))
        print("----------------------------------------------------------------------------------")
        for row in result:
            id = row[0]
            nr_rej = row[1]
            id_kl = row[2]
            marka = row[3]
            vin = row[4]
            rok_prod = row[5]
            print('%10i|%11s|%11i|%11s|%20s|%14s' % (id,nr_rej,id_kl,marka,vin,rok_prod))
            print("----------------------------------------------------------------------------------")
    
    def pojazdyD (self):
        nrej = input("Podaj numer rejestracyjny\n")
        idk = input("Podaj ID klienta\n")
        mar = input("Wpisz markę\n")
        nvin = input("Wpisz numer VIN\n")
        rprod = input("Wpisz rok produkcji\n")
        self.cursor.execute("INSERT INTO pojazdy (nr_rej, id_kl, marka, vin, rok_prod) VALUES (%r,%s, %r, %r, %r)" % (nrej.upper(), idk ,mar.upper(), nvin, rprod))
        self.conn.commit()
        print("Dodano pojazd do klienta o ID: "+ idk+"\n")
    
    def pojazdyE (self):
        ide = input("Podaj ID pojazdu do edycji\n")
        idk = input("Podaj aktualne ID klienta\n")
        nrej = input("Podaj aktualny numer rejestracyjny\n")
        mar = input("Wpisz aktualną markę\n")
        nvin = input("Wpisz właściwy numer VIN\n")
        rprod = input("Wpisz właściwy rok produkcji\n")
        self.cursor.execute('UPDATE pojazdy SET '+'id_kl' + ' = "' + idk + '",'
                                                 + 'nr_rej' + '= "' + nrej + '",'  
                                                 + 'marka' + '= "' + mar + '",'
                                                 + 'vin' + '= "' + nvin + '",'
                                                 + 'rok_prod' + '= "' + rprod + '" '
                                                 + ' WHERE id = ' + "'" + ide + "';")
        self.conn.commit()
        print("Edytowano pojazd o ID: "+ide+"\n")
        
    #def pojazdyU (self):    
    
    def fnag (self): #dodawanie rekordów do faktur
        nr = input("Podaj numer faktury\n") #podanie nr_fak
        idk = input("Podaj id klienta\n") #podanie id_kl
        naz = input("Podaj nazwę klienta\n") #podanie nazwa_kl
        adr = input("Podaj adres klienta\n") #podanie adres
        nrr = input("Podaj numer rejestracyjny\n") #podanie nr_rej
        dw = input("Podaj datę wystawienia faktury\n") #podanie data_fak
        ds = input("Podaj datę sprzedaży\n") #podanie data_sprz
        fp = input("Podaj formę płatności\n") #podanie forma_plat
        prz = input("Podaj przebieg\n") #podanie przebieg
        netto = 0 #wstępne netto do aktualizacji przy drukowaniu
        brutto = 0 #wstępne brutto do aktualizacji przy drukowaniu
        vat = 0 #wstępny vat do aktualizacji przy drukowaniu
        wys = input("Wpisz wystawcę faktury\n") #podanie wystawca                                    
        self.cursor.execute('insert into faktury (nr_fak, id_kl, nazwa_kl, adres, nr_rej, data_fak, data_sprz, forma_plat, przebieg, netto, brutto, vat, wystawca) values ('+str(nr)+','+str(idk)+',"'+naz+'","'+adr+'","'+nrr+'","'+dw+'","'+ds+'",'+str(fp)+','+str(prz)+','+str(netto)+','+str(brutto)+','+str(vat)+','+str(wys)+')')
        self.conn.commit()        
        
        while True:
            decyzja = input("Czy chcesz wydrukować fakturę? (T)ak / (N)ie\n")
            if (decyzja.upper() == 'T'):
                self.cursor.execute('select * from faktury ;') 
                result1 = self.cursor.fetchall()
                idf = result1[len(result1)-1][0]
                self.cursor.execute('select * from faktury where id =' + str(idf)+ ';') 
                resultFaktury = self.cursor.fetchall()
                for row in resultFaktury:
                    idf - row[0]
                    nr = row[1]
                    idk = row[2]
                    naz=row[3]
                    adr=row[4]
                    nrr=row[5]
                    dw=row[6]
                    ds=row[7]
                    fp=row[8]
                    prz=row[9]
                    netto=row[10]
                    brutto=row[11]
                    vat=row[12]
                    wys = row[13]
                    print('%5s|%10s|%10s|%15s|%15s|%10s|%10s|%10s|%10s|%10s|%8s|%8s|%5s|%10s|' % ('ID','Numer FV','ID klienta','Nazwa','Adres','nr. rej','Data wys.','Data sprz.','Forma pl.','Przebieg','Netto','Brutto','VAT','Wystawca'))
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print('%5i|%10i|%10i|%15s|%15s|%10s|%10s|%10s|%10i|%10i|%8.2f|%8.2f|%5.2f|%10i|' % (idf,nr,idk,naz,adr,nrr,dw,ds,fp,prz,netto,brutto,round(vat,2),wys))
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            elif (decyzja.upper() == 'N'):
                break
    def fakd (self): #wyświetlanie faktury po numerze        
        nrf = input("Podaj numer faktury do wyświetlenia\n") #podanie nr_fak do wyświetlenia
        self.cursor.execute('select * from faktury where nr_fak =' + nrf + ';')             
        resultFaktury = self.cursor.fetchall()
        idf = resultFaktury[len(resultFaktury)-1][1]
        for row in resultFaktury:
            idf - row[0]
            nr = row[1]
            idk = row[2]
            naz=row[3]
            adr=row[4]
            nrr=row[5]
            dw=row[6]
            ds=row[7]
            fp=row[8]
            prz=row[9]
            netto=row[10]
            brutto=row[11]
            vat=row[12]
            wys = row[13]
            print('%5s|%10s|%10s|%15s|%15s|%10s|%10s|%10s|%10s|%10s|%8s|%8s|%5s|%10s|' % ('ID','Numer FV','ID klienta','Nazwa','Adres','nr. rej','Data wys.','Data sprz.','Forma pl.','Przebieg','Netto','Brutto','VAT','Wystawca'))
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            print('%5i|%10i|%10i|%15s|%15s|%10s|%10s|%10s|%10i|%10i|%8.2f|%8.2f|%5.2f|%10i|' % (idf,nr,idk,naz,adr,nrr,dw,ds,fp,prz,netto,brutto,round(vat,2),wys))
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        
            
        
      
 
db1 = DBconn()


     



       