create database compravenda;

use compravenda;

CREATE TABLE cliente(
codcliente int (11) not null primary key auto_increment,
nome varchar(40) not null,
endereco varchar(70) not null,
cpf varchar(14) not null);

CREATE TABLE produto(
codproduto int not null primary key auto_increment,
nomeproduto varchar(30) not null,
qtd int not null,
valor float not null
);

CREATE TABLE funcionario(
codfuncionario int (11) not null primary key auto_increment,
nome varchar(60) not null,
cpf varchar(14) not null,
endereco varchar (60) not null,
datanasc date not null
);


create table pedido(
	codpedido int not null primary key auto_increment,
    qtd int not null,
    total float not null,
    formaspagamento varchar(40) not null,
    codcliente int,
    foreign key (codcliente) references cliente(codcliente),
    codproduto int,
	foreign key (codproduto) references produto(codproduto),
    codfuncionario int,
    foreign key (codfuncionario) references funcionario(codfuncionario)
    );

drop table pedido;





