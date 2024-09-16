use compravenda;

select * from cliente;
select * from produto;
select * from funcionario;
select * from pedido;

insert into cliente values
(null, 'Ana','Rua 123', '00044458900'),
(null, 'Ana', 'Rua abc', '11144458910'),
(null, 'Ana', 'Rua 987', '22244458902'),
(null, 'Ana', 'Rua xyz', '33344458930'),
(null, 'Ana', 'Rua 0A', '44444458904')
;

insert into produto values
(null, 'Laptop', 100 , 6000.00),
(null, 'Cadeira gamer', 80 , 800.00),
(null, 'Kit gamer', 60 , 350.00),
(null, 'USB drive 14GB', 75 , 65.00),
(null, 'Fone bluetooth', 15 , 90.00),
(null, 'Cabo HDMI', 10 , 30.00)
;

insert into funcionario values
(null, 'Maria', '00044458900', 'Avenida 123', '2002-10-05'),
(null, 'Fulana', '11144458910', 'Avenida abc', '1992-11-25'),
(null, 'Pedro', '22244458902', 'Avenida 987', '1999-09-07'),
(null, 'Ana', '44444458904', 'Avenida 0A', '2000-04-22')
;


insert into pedido values
(null, '3', 300.00 , 'pix', 3, 2, 1),
(null, '1', 200.00 , 'dinheiro', 1, 3, 1),
(null, '3', 300.00 , 'débito', 3, 2, 1),
(null, '3', 300.00 , 'crédito', 1, 3, 2),
(null, '3', 300.00 , 'pix', 2, 3, 1)
;





INSERT INTO produto (nomeproduto, qtd, valor) VALUES ('Notebook XYZ', 10, 2999.99);
