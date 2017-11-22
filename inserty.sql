use sop;
#MS10
INSERT INTO klienci VALUES (1, 'Car Mazowsze' , 'Warszawa' , '1231216547');
INSERT INTO klienci VALUES (2, 'Autex', 'Poznań' , '1422335647');
INSERT INTO klienci VALUES (3, 'Bajka' , 'Gołków' , '5326781234');
INSERT INTO klienci VALUES (4, 'Atonaprawa', 'Konin', '6567873241');
INSERT INTO klienci VALUES (5, 'Autotransport', 'Wrocław', '1241215687');


INSERT INTO marka VALUES (1, 'Volvo');
INSERT INTO marka VALUES (2, 'Renult');
INSERT INTO marka VALUES (3, 'Mercedes');
INSERT INTO marka VALUES (4, 'DAF');
INSERT INTO marka VALUES (5, 'MAN');


INSERT INTO pojazdy VALUES (1, 'WPI7PR2', 2 , 3 , 'XPL12345FGD67890TUY' , 2009);
INSERT INTO pojazdy VALUES (2, 'WPI3562', 1 , 2 , 'XPD12336FGD68890HGY' , 2010);
INSERT INTO pojazdy VALUES (3, 'WL45H2', 3 , 4 , 'ZTY12345FFD47890TTR' , 2011);
INSERT INTO pojazdy VALUES (4, 'DWR47Y8', 4 , 5 , 'WAS12345FGD98892OIK', 2012);
INSERT INTO pojazdy VALUES (5, 'WKZ6WD8', 5 , 1 , 'LSA12342EGD67895JMA', 2015 );


INSERT INTO uslugi VALUES (1, '243' , 'przegląd', 800);
INSERT INTO uslugi VALUES (2, '567' , 'wymiana koła' , 100);
INSERT INTO uslugi VALUES (3, '876' , 'programowanie' , 250);
INSERT INTO uslugi VALUES (4, 'LAK' , 'lakierowanie' , 300);
INSERT INTO uslugi VALUES (5, '145' , 'naprawa sprzęgła' , 1200);

INSERT INTO producent VALUES (1, 'VOL' , 'Volvo');
INSERT INTO producent VALUES (2, 'BOS', 'Bosh');
INSERT INTO producent VALUES (3, 'VAT' , 'Vatra');
INSERT INTO producent VALUES (4, 'CEN' , 'Centra');
INSERT INTO producent VALUES (5, 'CAST' , 'Castrol');

INSERT INTO towary VALUES (1, 'sprzęgło' , 1 , 1000 , 'szt');
INSERT INTO towary VALUES (2, 'wycieraczka' , 2 , 100 , 'szt') ;
INSERT INTO towary VALUES (3, 'akumulatorv' , 3 , 500 , 'szt');
INSERT INTO towary VALUES (4, 'akumulatorc', 4 , 350 , 'szt');
INSERT INTO towary VALUES (5, 'olej' , 5 , 90 , 'lt');

INSERT INTO forma_plat VALUES (1, 'gotówka' , 0);
INSERT INTO forma_plat VALUES (2, 'przelwe' , 14);

INSERT INTO logowanie VALUES (1, 'a', 'admin@sop.com', 'haslo123');
INSERT INTO logowanie VALUES (2, 'p', 'jadwiga@sop.com', 'haslo456');
INSERT INTO logowanie VALUES (3, 'k', 'zygmunt@gmail.com', 'haslo789' );

INSERT INTO uzytkownicy VALUES (1, 1 , 'jan' , 'kowalski');
INSERT INTO uzytkownicy VALUES (2, 2 , 'grazyna' , 'nowak');
INSERT INTO uzytkownicy VALUES (3, 2 , 'janusz' , 'naprawski');
INSERT INTO uzytkownicy VALUES (4, 3 , 'kazimierz' , 'piotrowski');
INSERT INTO uzytkownicy VALUES (5, 3 , 'adam' , 'malinowski');

INSERT INTO faktury VALUES (1, 1 , 1 , 'Car Mazowsze' , 'Warszawa' , 'WPI3562' , '2017-11-19' , '2017-11-15' , 2 , 24000 , 1000 , 230 , 1230 , 2);
INSERT INTO faktury VALUES (2, 2 , 5 , 'Autotransport', 'Wrocław' , 'DWR47Y8' , '2017-11-20' , '2017-11-20' , 1 , 120000 , 2000, 460 , 2460 , 2);
INSERT INTO faktury VALUES (3, 2 , 5 , 'Autotransport', 'Wrocław' , 'DWR47Y8' , '2017-11-20' , '2017-11-20' , 1 , 120000 , 2000, 460 , 2460 , 2);


INSERT INTO faktury_det VALUES (1, 1 ,'u' , 'przegląd' , 1 , 800 , 184);
INSERT INTO faktury_det VALUES (2, 1 , 't' , 'wycieraczka' , 2 , 200 , 46);
INSERT INTO faktury_det VALUES (3, 2 , 't' , 'sprzęgło' , 1 , 1000 , 230);
INSERT INTO faktury_det VALUES (4, 2 , 'u' , 'naprawa sprzęgła' , 1 , 1000 , 230);

INSERT INTO historia VALUES (1, 'WPI3562' , 1 , 24000);
INSERT INTO historia VALUES (2, 'DWR47Y8', 2 , 120000);

