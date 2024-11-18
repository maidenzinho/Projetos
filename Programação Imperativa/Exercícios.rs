enum Direcao{
    Frente,
    Tras,
    Esquerda,
    Direita,
}

fn lado_escolhido(lado: Direcao){
    match lado{
        Direcao::Direita => println!("Você está indo para a Direita"),
        Direcao::Esquerda => println!("Você está indo para a Esquerda"),
        Direcao::Frente => println!("Você está indo para Frente"),
        Direcao::Tras => println!("Você está indo para Tras"),
    }
}

fn main(){
    let lado = Direcao::Frente;
    lado_escolhido(lado);
}