/*
/*Implemente uma estrutura chamada Pessoa e que esteja de acordo com a seguinte especificação:
- Possui três campos: nome, do tipo String; idade, do tipo u8 e altura, do tipo f32.
- Uma função estática new, que retorna uma estrutura Pessoa, com os seguintes parâmetros: nome, idade e altura. Ao final, retorne uma instância de Pessoa
inicializada com esses parâmetros.
- Crie uma função associada a estrutura Pessoa chamada falar, com um parâmetro
mensagem do tipo String e sem retorno, que mostre na tela “A pessoa <NOME>
disse <MENSAGEM>”, substituindo NOME pelo campo nome e MENSAGEM pelo
parâmetro mensagem.
- Crie uma função main para criar uma pessoa através do método new e chamar a
função falar fornecendo uma mensagem arbitrária como parâmetro.
*/
struct Pessoa{
    nome: String,
    idade: u8,
    altura: f32
}
impl Pessoa {
    fn new(nome: String, idade: u8, altura: f32) -> Pessoa {
        Pessoa{nome, idade, altura}
    }
    fn falar(&self, mensagem: String){
        println!("{} disse: {}, tenho: {} e {} de altura", self.nome, mensagem, self.idade, self.altura);
    }
}

fn main(){
    let pessoa: Pessoa = Pessoa::new(String::from("Luis"), 25, 1.80);
    pessoa.falar(String::from("Prazer".to_string()));
}
*/
//----------------------------------------------------------------------------------------------------------------------------------------------

/*
Implemente uma estrutura chamada Permissao com três campos booleanos: escrita, leitura e execução
- Crie uma função estática new, que retorna uma estrutura Permissao, com os seguintes parâmetros: escrita, leitura e execucao. Ao final, retorne uma instância
de Permissao inicializada com esses parâmetros.
-No mesmo código, implemente outra estrutura chamada Arquivo com três campos: permissao (Permissao), nome (String) e tamanho (usize).
- Crie uma função estática new, que retorna uma estrutura Arquivo, inicializando seus campos. Ao final, retorne uma instância de Arquivo inicializada.
-Na função main, crie quatro arquivos a partir das funções criadas.
*/
/*
struct Permissao{
    escrita,
    leitura,
    execucao
}
struct Arquivo{
    permissao: Permissao,
    nome: String,
    tamanho: usize
}
impl Permissao{
    fn new(escrita: bool, leitura: bool, execucao: bool) -> Permissao{
        Permissao{escrita, leitura, execucao}
    }
}
impl Arquivo{
    fn new(permissao: Permissao, nome: String, tamanho: usize) -> Arquivo{
        Arquivo{permissao, nome, tamanho}
    }
}
fn main(){
    let arquivo1 = Arquivo::new(Permissao::new(true, true, false), String::from("arquivo1.txt"), 1024);
    let arquivo2 = Arquivo::new(Permissao::new(false, true, true), String::from("arquivo2.txt"), 2048);
    let arquivo3 = Arquivo::new(Permissao::new(true, false, true), String::from("arquivo3.txt"), 512);
    let arquivo4 = Arquivo::new(Permissao::new(true, true, true), String::from("arquivo4.txt"), 4096);

    println!("Arquivo: {}, Tamanho: {} bytes", arquivo1.nome, arquivo1.tamanho);
    println!("Arquivo: {}, Tamanho: {} bytes", arquivo2.nome, arquivo2.tamanho);
    println!("Arquivo: {}, Tamanho: {} bytes", arquivo3.nome, arquivo3.tamanho);
    println!("Arquivo: {}, Tamanho: {} bytes", arquivo4.nome, arquivo4.tamanho);
}
*/
//----------------------------------------------------------------------------------------------------------------------------------------------
/*
Crie uma função que recebe uma string como parâmetro e retorne um usize que representa o tamanho dela. (Não pode utilizar funções nativas do Rust)
Crie uma função que, a partir de um parâmetro que é uma referência à uma variável do tipo String, mostre o seu endereço na memória
*/
/*
fn recebe(s: String) -> usize{
    let tamanho = s.len();
    tamanho
}
fn main(){
    let s = String::from("hello");
    let tamanho = recebe(s);
    println!("Tamanho: {}",tamanho);
}
*/
/*
fn mostrar_endereco(s: &String) {
    let endereco = s as *const String as usize;

    println!("O endereço da variável é: 0x{:x}", endereco);
}

fn main() {
    let minha_string = String::from("Olá, Rust!");
    mostrar_endereco(&minha_string);
}
*/