let numero = parseInt(prompt("Digite um número para ver a tabuada:"));

for (let i = 1; i <= 10; i++) {
  document.write(numero + ' x ' + i + ' = ' + (numero * i) + '<br>');
}