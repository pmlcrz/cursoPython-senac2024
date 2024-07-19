let a = 0, b = 1;
let fibonacci = '';

while (a <= 2000) {
  fibonacci += a + ', ';
  let temp = a + b;
  a = b;
  b = temp;
}

document.write(fibonacci.slice(0, -2)); // Remover a última vírgula e espaço