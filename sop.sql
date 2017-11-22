create database sop;
use sop;

create table klienci (
id int primary key auto_increment,
nazwa varchar(100),
adres varchar(100),
nip varchar(11));

select * from klienci;



create table marka (
id int primary key auto_increment,
marka char(15) not null);

create table pojazdy (
id int primary key auto_increment,
nr_rej char(10) not null,
id_kl int,
id_marka int,
vin char(19) not null,
rok_prod year,
foreign key (id_kl) references klienci (id),
foreign key (id_marka) references marka (id));

create table uslugi (
id int primary key auto_increment,
kod_us varchar(5),
nazwa_us varchar(50),
cena float);

create table producent (
id int primary key auto_increment,
kod_prod char(5),
nazwa varchar(20));

create table towary (
id int primary key auto_increment,
nazwa varchar(50),
id_prod int,
cena float,
jednostka_miary char(5),
foreign key (id_prod) references producent(id));


create table forma_plat (
id int primary key auto_increment,
typ char(10),
dni int);


create table logowanie (
id int primary key auto_increment,
email varchar(100),
haslo varchar(50),
kod_upr char(5));

create table uzytkownicy (
id int primary key auto_increment,
id_log int,
imie text,
nazwisko text,
foreign key (id_log) references logowanie (id));

create table faktury (
id int primary key auto_increment,
nr_fak int,
id_kl int,
foreign key (id_kl) references klienci(id),
nazwa_kl varchar(100),
adres varchar(100),
nr_rej char(10),
data_fak date not null,
data_sprz date not null,
forma_plat int,
foreign key (forma_plat) references forma_plat(id),
przebieg int,
netto float,
vat float,
brutto float,
wystawca int,
foreign key (wystawca) references uzytkownicy (id)); 

create table faktury_det (
id int primary key auto_increment,
id_faktury int,
typ char(1),
nazwa varchar(50),
ilosc int,
cena float,
vat float,
foreign key (id_faktury) references faktury (id));

create table historia (
id int primary key auto_increment,
nr_rej char(10),
id_faktury int,
przebieg int,
foreign key (id_faktury) references faktury (id));


create trigger historia_add
before insert on 
faktury
for each row 
insert into historia (nr_rej, id_faktury, przebieg) values (new.nr_rej, new.nr_fak, new.przebieg);

