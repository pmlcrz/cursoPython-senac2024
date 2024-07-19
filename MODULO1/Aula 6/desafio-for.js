const notas = [8, 7, 10, 6, 9];
let soma = 0;
let contador = 0;
let notaMinima = 7;

for (let i = 0; i < notas.length; i++) {
  if (notas[i] >= notaMinima) {
    soma += notas[i];
    contador++;
  }
}

if (contador > 0) {
  const media = soma / contador;
  console.log(`A média das notas acima de ${notaMinima} é: ${media}`);
} else {
  console.log(`Nenhuma nota foi encontrada acima de ${notaMinima}`);
}