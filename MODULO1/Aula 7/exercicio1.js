/* faça um programa em javascript que faça o seguinte:

 DIGA "olá [nome da pessoa]!" E escreva o seguinte texto:

 "Eu, [nome da pessoa]. portador do cpf [cpf], residente no endereço [endereço], declaro que as informações são verdadeiras."

 Se o endereço dela for fora do RJ, ela deve pagar uma taxa de R$50,00 para emitir o texto. */ 

 
 function emitirDeclaracao(nome, cpf, endereco, estado) {

    if (estado !== "RJ") {
        console.log(`Olá, ${nome}!`);
        console.log(`Eu, ${nome}, portador do CPF ${cpf}, residente no endereço ${endereco}, declaro que as informações são verdadeiras.`);
        console.log("Taxa de R$50,00 aplicada para emissão do texto.");
    } else {
        console.log(`Olá, ${nome}!`);
        console.log(`Eu, ${nome}, portador do CPF ${cpf}, residente no endereço ${endereco}, declaro que as informações são verdadeiras.`);
    }
}

emitirDeclaracao("Fulana de tal", "123.456.789-00", "Rua Santa luzia, 123", "RJ");
