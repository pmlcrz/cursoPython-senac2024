select cliente.nome, produto.nomeproduto, produto.qtd, produto.valor, 
pedido.formaspagamento from cliente inner join pedido on pedido.codcliente = cliente.codcliente inner join 
produto on pedido.codproduto = produto.codproduto inner join funcionario on pedido.codfuncionario = funcionario.codfuncionario;



select * from cliente

inner join pedido on pedido.codcliente = cliente.codcliente
inner join produto on pedido.codproduto = produto.codproduto
inner join funcionario on pedido.codfuncionario = funcionario.codfuncionario;