/* MÁQUINA DE CAFÉ:
    1º Pedir o número do produto
    2º Valor do produto
    3º Inserir o cartão
    4º Senha do cartão
    5º Entregar o produto
*/

// Produtos disponíveis
produtos = ['Café', 'Capuccino', 'Café com Leite', 'Chocolate']
// Senha do cartão do usuário
senhaCorreta = 1234;

function pagamento(){
    // Insira o cartão
    alert('Insira o cartão');
    // Conferindo a senha
    senha = prompt("Digite sua senha: ")
        if (senha == senhaCorreta){
            alert('Senha confirmada. Espere a entrega do produto.');
        } else {
            alert('Senha incorreta, por favor tente novamente');
            menuprincipal();
        }    
}

// INÍCIO DA FUNÇÃO MENU PRINCIPAL
function menuprincipal(){
    opcao = prompt('Menu: 1. Café (R$ 2,00) | 2. Capuccino (R$ 3,50) | 3. Café com Leite (R$ 3,00) | 4. Chocolate (R$ 4,00) | 5. Sair | Digite o número do produto: ');

    if (opcao == '1') {
    //opção 1. Café
    alert('Você escolheu: ' + produtos[0]);
    alert(produtos[0] + ' R$ 2,00');
    pagamento();
    
    } else if(opcao == '2'){
        //opção 2. Capuccino
        alert('Você escolheu: ' + produtos[1]);
        alert(produtos[1] + ' R$ 3,50');
        pagamento();

    } else if(opcao == '3'){
        //opção 3. Café com Leite
        alert('Você escolheu: ' + produtos[2]);
        alert(produtos[2] + ' R$ 3,00');
        pagamento();
    } else if(opcao == '4'){
        //opção 4. Chocolate
        alert('Você escolheu: ' + produtos[3]);
        alert(produtos[3] + ' R$ 4,00');
        pagamento();
    } else if(opcao == 5){
        alert("Obrigado pela preferência");
        exit();
    } else {
        alert('Você digitou uma opção inválida. Por favor, tente novamente.');
        menuprincipal();
    }
} // AQUI É O FIM DA FUNÇÃO

menuprincipal();/* MÁQUINA DE CAFÉ:
    1º Pedir o número do produto
    2º Valor do produto
    3º Inserir o cartão
    4º Senha do cartão
    5º Entregar o produto
*/

// Produtos disponíveis
produtos = ['Café', 'Capuccino', 'Café com Leite', 'Chocolate']
// Senha do cartão do usuário
senhaCorreta = 1234;

function pagamento(){
    // Insira o cartão
    alert('Insira o cartão');
    // Conferindo a senha
    senha = prompt("Digite sua senha: ")
        if (senha == senhaCorreta){
            alert('Senha confirmada. Espere a entrega do produto.');
        } else {
            alert('Senha incorreta, por favor tente novamente');
            menuprincipal();
        }    
}

// INÍCIO DA FUNÇÃO MENU PRINCIPAL
function menuprincipal(){
    opcao = prompt('Menu: 1. Café (R$ 2,00) | 2. Capuccino (R$ 3,50) | 3. Café com Leite (R$ 3,00) | 4. Chocolate (R$ 4,00) | 5. Sair | Digite o número do produto: ');

    if (opcao == '1') {
    //opção 1. Café
    alert('Você escolheu: ' + produtos[0]);
    alert(produtos[0] + ' R$ 2,00');
    pagamento();
    
    } else if(opcao == '2'){
        //opção 2. Capuccino
        alert('Você escolheu: ' + produtos[1]);
        alert(produtos[1] + ' R$ 3,50');
        pagamento();

    } else if(opcao == '3'){
        //opção 3. Café com Leite
        alert('Você escolheu: ' + produtos[2]);
        alert(produtos[2] + ' R$ 3,00');
        pagamento();
    } else if(opcao == '4'){
        //opção 4. Chocolate
        alert('Você escolheu: ' + produtos[3]);
        alert(produtos[3] + ' R$ 4,00');
        pagamento();
    } else if(opcao == 5){
        alert("Obrigado pela preferência");
        exit();
    } else {
        alert('Você digitou uma opção inválida. Por favor, tente novamente.');
        menuprincipal();
    }
} // AQUI É O FIM DA FUNÇÃO

menuprincipal();