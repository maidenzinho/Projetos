/*
1. Escreva uma função que receba dois valores (qualquer tipo),
que sejam mutáveis e troque seus valores. Utilize referências
para realizar a troca.
*/

fn swap(x: &mut i32, y: &mut i32) {
    // temp = x  -> temp será uma referência
    // temp = *x -> receberá o valor da referência
    let temp: i32 = *x;
    *x = *y;
    *y = temp;
}

fn testa_swap() {
    let mut a: i32 = 10;
    let mut b: i32 = -7;

    println!("a = {a}, b = {b}");
    swap(&mut a, &mut b);
    println!("a = {a}, b = {b}");
}

/*
2. Escreva uma função que calcule a média de um vetor de números
inteiros. A função deve receber uma referência (&) ao vetor como
parâmetro e retornar a média.
*/

fn media_referencia(vetor: &[i32; 4]) -> f64 {
    let mut soma: f64 = 0.0;
    for valor in vetor {
        soma = soma + (*valor as f64);
    }

    soma / vetor.len() as f64
}

fn testa_media() {
    let v1: [i32; 4] = [1, 2, 3, 4];
    let media1: f64 = media_referencia(&v1);
    println!("Média 1 = {media1}");

    let v2: [i32; 4] = [-5, 0, -1, 3];
    let media2: f64 = media_referencia(&v2);
    println!("Média 2 = {media2}");
}

/*
3. Crie uma função que verifique se uma palavra é um palíndromo,
ou seja, ela é a mesma quando é lida de trás para frente.
A função deve receber uma referência à uma string como parâmetro
e retornar um booleano indicando se é um palíndromo ou não.
*/

// natan
// ana
// ovo
// abba
// baab
// subinoonibus

fn is_palindromo(texto: &String) -> bool {
    let texto_reverso: String = texto.clone();

    for (c1, c2) in texto.chars().zip(texto_reverso.chars().rev()) {
        println!("c1 = {c1}, c2 = {c2}");
        if c1 != c2 {
            return false
        }
    }

    true
}

fn testa_palindromo() {
    let texto1 = String::from("teste");
    println!("{texto1} é palíndromo? {}", is_palindromo(&texto1));

    let texto2 = String::from("subinooniibus");
    println!("{texto2} é palíndromo? {}", is_palindromo(&texto2));
}

fn main() {
    testa_swap();
    testa_media();
    testa_palindromo();
}
