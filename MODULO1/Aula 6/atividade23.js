let numero = parseInt(prompt("Digite um número:"));

    // Se o número digitado não for par, torná-lo par
    if (numero % 2 !== 0) {
      numero++;
    }

    while (numero <= 100) {
      document.write(numero + '<br>');
      numero += 2;
    }