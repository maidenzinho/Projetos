use std::io::Write;

fn main() {
    // ex1();
    // ex2();
    ex3();
}

// Escreva um algoritmo em Rust para calcular a idade de alguém,
// sabendo seu ano de nascimento
fn ex1() {
    print!("Digite seu ano de nascimento: ");
    std::io::stdout().flush().expect("Erro ao dar flush no terminal");

    let mut buffer: String = String::new();

    // Lê dados do teclado e armazena eles na variável mutável buffer
    std::io::stdin().read_line(&mut buffer).expect("Erro ao ler linha");

    // Remove quebra de linha (.trim()) e converte para u16 (.parse())
    let ano_nascimento: u16 = buffer.trim().parse().expect("erro ao converter");
    let ano_corrente: u16 = 2024;

    println!("Sua idade é {}", ano_corrente - ano_nascimento);
}

fn ex2() {
    let mut buffer: String = String::new();
    let diaria: f32 = 100.0;
    let numero_dias: f32;

    print!("Digite a quantidade de dias: ");
    std::io::stdout().flush().expect("Erro ao dar flush no terminal");

    // Lê dados do teclado e armazena eles na variável mutável buffer
    std::io::stdin().read_line(&mut buffer).expect("Erro ao ler linha");

    // Remove quebra de linha (.trim()) e converte para u16 (.parse())
    numero_dias = buffer.trim().parse().expect("Erro ao converter valor para float32");

    println!("Você pagará R${:.2}", diaria * numero_dias);
}

// Leia a temperatura do teclado em Celsius e imprima o
// equivalente em Fahrenheit
fn ex3() {
    let mut buffer: String = String::new();

    // Mostra o texto na tela e força atualização do terminal
    print!("Digite a temperatura em Fahrenheit: ");
    std::io::stdout().flush().expect("Erro ao dar flush no terminal");

    // Leitura dos dados do teclado (resultado armazenado em buffer)
    std::io::stdin().read_line(&mut buffer).expect("Erro ao ler linha");

    // Converte String para f32
    let fahrenheit: f32 = buffer.trim().parse().expect("Erro ao converter");

    // Converte de fahrenheit para celsius
    let celsius: f32 = (fahrenheit - 32.0) * 5.0 / 9.0;

    // Mostra o valor que está na variável 'celsius' com duas casas decimais
    println!("Temperatura em Celsius é {celsius:.2}");
}