fn main(){

}

//Exemplo 1: Ownership básico
fn ex1() {
    let s1 = String::from("Olá"); // `s1` é o dono da String
    let s2 = s1; // `s1` move a propriedade da String para `s2`

    // println!("{}", s1); // Erro! `s1` não é mais válido.
    println!("{}", s2); // Ok, `s2` agora é o dono da String.
}

//Exemplo 2: Clone (Cópia profunda)
fn ex2() {
    let s1 = String::from("Olá");
    let s2 = s1.clone(); // Faz uma cópia profunda da String

    println!("s1 = {}, s2 = {}", s1, s2); // Ambos funcionam, pois `s1` e `s2` são donos independentes
}

//Exemplo 3: Funções e ownership
fn ex3() {
    let s = String::from("Olá");
    tomar_posse(s); // `s` é movido para a função, perde seu valor no escopo atual
    // println!("{}", s); // Erro! `s` não é mais válido.
}

fn tomar_posse(s: String) {
    println!("{}", s);
}

//Exemplo 4: Borrowing (Empréstimo)
fn ex4() {
    let s = String::from("Olá");
    imprimir(&s); // Empresta `s` sem transferir ownership

    println!("{}", s); // Ok, `s` ainda é válido
}

fn imprimir(s: &String) {
    println!("{}", s); // Usando a referência, mas não tomando a posse
}


//Exemplo 5: Mutabilidade e ownership
fn ex5() {
    let mut s = String::from("Olá");
    alterar(&mut s); // Passa uma referência mutável para `alterar`

    println!("{}", s); // O valor foi alterado
}

fn alterar(s: &mut String) {
    s.push_str(", mundo!");
}
