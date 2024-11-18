/*
Escreva um programa em Rust para mostrar a sequência de Fibonacci
até n termos. Em seguida, some os termos pares da sequência e,
ao final, mostre a soma
*/

fn fibonacci() {
    // Cria região de memória chamada buffer, do tipo String, que armazenará a linha que digitamos do teclado
    let mut buffer = String::new();

    println!("Digite a quantidade de termos:");

    // Leio a linha do teclado e armazeno na variável 'buffer'
    std::io::stdin().read_line(&mut buffer).expect("Erro ao ler linha");

    // Do meu buffer, vou remover as quebras de linha (chamada .trim())
    // Vou converter (chamada .parse()) para o tipo especificado da variável (u32)
    let n: u32 = buffer.trim().parse().expect("Erro ao converter");

    // Variáveis de controle do fibonacci
    let mut a = 1;
    let mut b = 1;
    let mut soma = 0;

    // Para cada número i, de 0 a n, faça:
    for i in 0..n {
        let c = a + b;
        a = b;
        b = c;

        // Se c for par, então some
        if c % 2 == 0 {
            soma = soma + c;
            // soma += c;
        }
        println!("Termo {i} de Fibonacci é {c}");
    }
    println!("Soma dos termos pares de Fibonacci: {soma}");
}

// Escreva um programa em Rust que calcule a soma dos números
// ímpares em um intervalo de 0 até 100
fn soma_impares() {
    let mut soma = 0;

    // Para cada número i, de 0 a 100, faça:
    for i in 0..100 {
        // Verifica se o resto da divisão por 2 é 1, ou seja, ímpar
        if i % 2 == 1 {
            soma = soma + i;
        }
    }

    println!("A soma dos termos ímpares entre 0 e 100 é {soma}");
}

/*
Escreva um programa em Rust que leia números inteiros do teclado.
Quando digitado o valor 0, o programa deverá encerrar e mostrar a
média dos números fornecidos de entrada.
*/

fn media_dados_teclado() {
    // Cria região de memória chamada buffer, do tipo String, que armazenará a linha que digitamos do teclado
    let mut buffer: String = String::new();

    // Armazenará a soma dos números que forneceremos pelo teclado
    let mut soma = 0;

    // Armazenará a quantidade de números que entraremos pelo teclado
    let mut numero_de_termos = 0;

    // Execute infinitamente até que seja especificado uma parada
    loop {
        println!("Digite um número:");

        // Leio a linha do teclado e armazeno na variável 'buffer'
        std::io::stdin()
                .read_line(&mut buffer)
                .expect("Erro ao ler linha");

        // Do meu buffer, vou remover as quebras de linha (chamada .trim())
        // Vou converter (chamada .parse()) para o tipo especificado da variável (i32)
        let n: i32 = buffer
                    .trim()
                    .parse()
                    .expect("Erro ao converter");

        // Se for 0, pare a execução
        if n == 0 {
            break;
        }

        // Some o valor de 'soma' a si mesmo + n
        soma = soma + n;
        // Incrementa 'numero_de_termos' em 1
        numero_de_termos = numero_de_termos + 1;

        // Limpa variável que armazena o texto do teclado
        // Aqui ficam alguns caracteres que impedem que convertamos novamente
        // uma nova variável
        buffer = String::new();
    }

    println!("Soma {soma}");
    println!("Quantidade de termos {numero_de_termos}");

    // Calcula média aritmética e converte números para float32 (as f32)
    println!("Média {}", soma as f32 / numero_de_termos as f32);
}


fn main() {
    // fibonacci();
    // soma_impares();
    // media_dados_teclado();
}


