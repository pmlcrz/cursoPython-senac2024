let andarAtual = 0;
let andarDesejado = 22;

while (andarAtual !== andarDesejado) {
  console.log(`Elevador no andar ${andarAtual}`);

  if (andarAtual < andarDesejado) {
    andarAtual++; 
  } else {
    andarAtual--; 
  }
}

console.log(`Elevador chegou ao andar ${andarDesejado}`);

