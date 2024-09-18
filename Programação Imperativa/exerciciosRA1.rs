fn main() {
}
fn ex1(){
    //Solicita números ao usuário e faz todas as operações
    let mut buffer = String::new();
    let mut buffer2 = String::new();
    println!("Digite o primeiro número: ");
    std::io::stdin().read_line(&mut buffer).expect("Erro!");
    println!("Digite o segundo número: ");
    std::io::stdin().read_line(&mut buffer2).expect("Erro!");
    let num1: i32 = buffer.trim().parse().expect("Erro!");
    let num2: i32 = buffer2.trim().parse().expect("Erro!");

    let soma = num1+num2;
    let subtracao = num1-num2;
    let divisao = num2/num2;
    let multiplicacao = num1*num2;

    println!("A soma é {}, a subtração é {}, a divisão é {} e a multiplicação é {}", soma, subtracao, divisao, multiplicacao);

}
fn ex2e3(){
    //Maior e o Menor números de um vetor
    let mut maior:u32 = 0;
    let mut menor:u32 = 0;

    let vet: [u32; 4] = [5,4,8,6];

    for i in vet {
        if i > maior{
            maior = i;
        }else{
            menor = i;
        }
    }
    println!("O maior número é {} e o menor é {}", maior, menor);
}
fn ex4(){
    //Solicita 3 números ao usuário e verifica qual o tipo de triângulo
    //Equilatero: todos iguais
    //Isoceles 2 iguais
    //Escaleno todos diferentes
    let mut num1 = String::new();
    let mut num2 = String::new();
    let mut num3 = String::new();

    println!("Digite o primeiro número:");
    std::io::stdin().read_line(&mut num1).expect("Erro ao ler a linha 1");

    println!("Digite o segundo número:");
    std::io::stdin().read_line(&mut num2).expect("Erro ao ler a linha 2");

    println!("Digite o terceiro número:");
    std::io::stdin().read_line(&mut num3).expect("Erro ao ler linha 3");

    if num1 == num2 && num2 == num3{
        println!("Seu triâgulo é Equilatero");
    }else if num1 == num2 || num2 == num3 || num1 == num3{
        println!("Seu triângulo é Isoceles");
    }else{
        println!("Seu triângulo é Escaleno");
    }
}
fn ex5(){
    
}