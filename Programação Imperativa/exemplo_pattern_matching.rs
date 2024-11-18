// Acessar: https://bit.ly/aula05-09-24

enum Animal {
    Cachorro,
    Cobra(bool),
    Passaro{raca: String}
}

fn formatar_animal(animal: Animal) -> String {
    match animal {
        Animal::Cachorro => format!("É um cachorro!"),
        Animal::Cobra(trocou_pele) => {
            let mut sim_nao = "sim";
            if !trocou_pele {sim_nao = "não"};
            format!("É uma cobra. Trocou de pele? {sim_nao}")
        },
        Animal::Passaro{raca} => {
            format!("É um pássaro da raça {raca}")
        }
    }
}

fn main() {
    let mut animais: Vec<Animal> = vec![];

    animais.push(Animal::Cachorro);
    animais.push(Animal::Passaro{raca: "sabiá".to_string()});
    animais.push(Animal::Passaro{raca: "joão-de-barro".to_string()});
    animais.push(Animal::Cobra(false));
    animais.push(Animal::Cobra(true));

    for animal in animais {
        println!("{}", formatar_animal(animal));
    }
}

