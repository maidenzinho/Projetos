// Acessar: https://bit.ly/aula05-09-24-1

/* 
Crie uma enumeração chamada Voto que represente diferentes tipos de votos, 
como voto a favor, voto contra e voto em branco. Em seguida, crie uma função
que aceite uma lista de votos representados como uma lista de variantes da
enumeração. Use a correspondência de padrões (pattern matching) para contar
e imprimir o número total de votos a favor, votos contra e votos em branco.
*/

enum Voto {
    Favor,
    Contra,
    Branco
}

fn contar_votos(votos: &Vec<Voto>) -> (u32, u32, u32) {
    let mut votos_a_favor: u32 = 0;
    let mut votos_contra:  u32 = 0;
    let mut votos_branco:  u32 = 0;

    for voto in votos {
        // Equivalente ao if/else para, principalmente, enumerações
        match *voto {
            // Equivalência semântica, porém não funciona
            // if voto == Voto::Favor {
            //      votos_a_favor += 1
            // }
            Voto::Favor => votos_a_favor += 1,
            Voto::Contra => votos_contra += 1,
            Voto::Branco => votos_branco += 1
        }
    }

    (votos_a_favor, votos_contra, votos_branco)
}

fn main() {
    let mut votos: Vec<Voto> = vec![];

    loop {
        let mut buf: String = String::new();

        println!("Digite uma opção: ");
        println!("1. Votar a favor\n2. Votar contra\n3. Votar em Branco\n4. Mostrar votos\n5. Sair");
        std::io::stdin().read_line(&mut buf).expect("Erro ao ler linha");
        
        let opcao: i32 = buf.trim().parse().expect("Erro ao converter");

        match opcao {
            1 => {votos.push(Voto::Favor)},
            2 => {votos.push(Voto::Contra)},
            3 => {votos.push(Voto::Branco)},
            4 => {
                let contagem = contar_votos(&votos);
                println!("Votos a favor {}", contagem.0);
                println!("Votos contra {}", contagem.1);
                println!("Votos em branco {}", contagem.2);
            }
            5 => {break},
            _ => {println!("Opção '{opcao}' não existe")}
        }
    }
}