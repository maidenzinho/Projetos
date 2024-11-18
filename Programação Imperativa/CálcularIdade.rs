fn main(){
    let mut buffer: String = String::new();
    let mut buffer2: String = String::new();
    let mut id:i32 = 0;
    let mut idade:i32 = 0;
    let mut ano:i32 = 0;
    println!("Qual seu ano de nascimento?");
    std::io::stdin().read_line(&mut buffer).expect("Erro ao ler");
    let buffer:i32 = buffer.trim().parse::<i32>().expect("Erro ao converter");
    idade = buffer;

    println!("Digite o ano atual?");
    std::io::stdin().read_line(&mut buffer2).expect("Erro ao ler");
    let buffer:i32 = buffer2.trim().parse::<i32>().expect("Erro ao converter");
    ano = buffer;

            if ano == 2024{
                id= ano - idade;

                println!("Sua idade é: {}", id);
            }
}