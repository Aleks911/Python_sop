create database sop;
use sop;

create table klienci (
id int primary key auto_increment,
nazwa varchar(100),
adres varchar(100),
nip varchar(11));



create table pojazdy (
id int primary key auto_increment,
nr_rej char(10) not null,
id_kl int,
marka char(15),
vin char(19) not null,
rok_prod year,
foreign key (id_kl) references klienci (id));

create table uslugi (
id int primary key auto_increment,
kod_us varchar(5),
nazwa_us varchar(50),
cena float);


create table towary (
id int primary key auto_increment,
nazwa varchar(50),
cena float,
jednostka_miary char(5));

alter table logowanie add column nip varchar(11);


create table forma_plat (
id int primary key auto_increment,
typ char(10),
dni int);

select * from logowanie;

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
nazwa_kl varchar(100),
adres varchar(100),
nr_rej char(10),
data_fak date not null,
data_sprz date not null,
forma_plat int,
przebieg int,
netto float,
vat float,
brutto float,
wystawca int,
foreign key (id_kl) references klienci(id),
foreign key (forma_plat) references forma_plat(id),
foreign key (wystawca) references uzytkownicy (id)); 

update logowanie set nip = '1241215687' where id = 5;
select* from logowanie;
delete from logowanie;
drop trigger historia_add;
select f.nr_fak, f.nr_rej, f.przebieg, f.data_fak from klienci as k, faktury as f where k.nip = "1241215687" and f.id_kl = k.id; 

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

show lastrowid(faktury);

create trigger historia_add
before insert on 
faktury
for each row 
insert into historia (nr_rej, id_faktury, przebieg) values (new.nr_rej, new.nr_fak, new.przebieg);

select * from logowanie where email = "admin@sop.com" and haslo = "haslo123";

insert into faktury (nr_fak, id_kl, nazwa_kl, adres, nr_rej, data_fak, data_sprz, forma_plat, przebieg, netto, brutto, vat, wystawca) values (1,1,"","","","2000-01-01","2000-01-01",1,1,1,1,1,1);