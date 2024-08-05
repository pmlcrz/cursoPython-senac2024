nome = "Marcio";
cpf = "145.678.910-11";
endereco = "Rua vasco da gama";
taxa = false;

console.log("Olá, " + nome + "!");

if (endereco == "RJ"){
    console.log("Eu, " + nome + ", portador do cpf" + cpf +", residente no endereco" 
    + endereco + ", declaro que as minhas informações são verdadeiras.");

} else {
    if (taxa == true){
        console.log("Eu, " + nome + ", portador do cpf" + cpf +", residente no endereco" 
        + endereco + ", declaro que as minhas informações são verdadeiras.");

    }else{
        console.log("Por favor, pague a taxa");
    }
}
