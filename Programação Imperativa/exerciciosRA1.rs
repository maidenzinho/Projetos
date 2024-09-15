fn main() {
}
fn ex1(){
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
fn ex2(){
    let mut maior:u32 = 0;
    let mut menor:u32 = 0;

    let vet: [u32; 4] = [5,4,8,6];

    for i in vet {
        if i > maior{
            maior = i;
        }else {
            menor = i;
        }
    }
    println!("O maior número é {} e o menor número é {}", maior, menor);
}