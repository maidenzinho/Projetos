/*
Crie um programa em Rust que recebe como entrada a idade de
um usuário e, se for maior de idade, mostre na tela que ele
é maior de idade. Caso contrário, mostre que ele é menor de
idade.
*/

use std::io::Write; // Necessário para flush()

fn ex1() {
    let mut buffer: String = String::new();

    print!("Digite sua idade: ");
    // Precisa colocar 'use std::io::Write'
    std::io::stdout().flush().expect("Erro ao dar flush");

    // Lê a linha do teclado e armazena o resultado em buffer
    std::io::stdin().read_line(&mut buffer)
        .expect("Erro ao ler linha");

    // Converte idade de String para u8
    let idade: u8 = buffer.trim().parse().expect("Erro ao converter");

    if idade >= 18 {
        println!("Você é maior de idade. Já pode ser preso!");
    } else {
        println!("Você é apenas um bebê.");
    }
}

fn ex2() {
    println!("Digite seu usuário: ");

    let mut nome_usuario = String::new();
    std::io::stdin().read_line(&mut nome_usuario)
        .expect("Erro ao ler linha");

    // "ola mundo"               -> &str (string estática)
    // String::from("ola mundo") -> String (string dinamica)
    //             (String) ->  (&str) ->  (String)
    nome_usuario = nome_usuario.trim().to_string();

    println!("Digite sua senha: ");
    let mut senha_usuario = String::new();
    std::io::stdin().read_line(&mut senha_usuario)
        .expect("Erro ao ler senha");

    // "ola mundo"               -> &str (string estática)
    // String::from("ola mundo") -> String (string dinamica)
    //             (String) ->  (&str) ->  (String)
    senha_usuario = senha_usuario.trim().to_string();

    if nome_usuario.eq("admin") && senha_usuario.eq("@dm1n") {
        println!("Deu certo");
    } else {
        println!("Deu errado!")
    }
}


fn main() {
    // ex1();
    ex2();

}
