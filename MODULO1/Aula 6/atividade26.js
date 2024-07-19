let numero = parseInt(prompt("Digite um número:"));

// Contagem regressiva
document.write("Contagem regressiva:<br>");
let i = numero;
while (i >= 0) {
  document.write(i + '<br>');
  i--;
}

// Contagem progressiva
document.write("<br>Contagem progressiva:<br>");
let j = 0;
while (j <= numero) {
  document.write(j + '<br>');
  j++;
}