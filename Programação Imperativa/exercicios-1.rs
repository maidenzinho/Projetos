fn main(){
//Exercício 1
fn calculadora(){
    let mut n: String = String::new();
    println!("Digite alguns números:");
    std::io::stdin().read_line(&mut n);
    let mut num: i32 = n.trim().parse().expect("");
    
    let mut n: String = String::new();
    println!("Digite alguns números:");
    std::io::stdin().read_line(&mut n);
    let mut num2: i32 = n.trim().parse().expect("");
    println!("Soma {}", num + num2);
    println!("Subtração {}", num - num2);
    println!("Multiplicação {}", num * num2);
    println!("Divisão {}", num / num2);
}
//Exercício 2
fn maior(){
    let nums = vec![5,6,8,9,3,2,7,1];
    let mut mai: i32 = nums[1];
    
    for n in nums{
        if mai < n{
            mai = n;
        }
    }
    println!("Maior número é {}", mai);
    
}
//Exercício 3
fn menor(){
    let nums = vec![5,6,8,9,3,2,7,1];
    let mut men: i32 = nums[1];
    
    for n in nums{
        if men > n{
            men = n;
        }
    }
    println!("Maior número é {}", men);
    
}
//Exercício 4
fn triangulo(){
    let mut buffer: String = String::new();
    println!("Digite um número:");
    std::io::stdin().read_line(&mut buffer);
    let mut num1: i32 = buffer.trim().parse().expect("");

    let mut buffer: String = String::new();
    println!("Digite um número:");
    std::io::stdin().read_line(&mut buffer);
    let mut num2: i32 = buffer.trim().parse().expect("");

    let mut buffer: String = String::new();
    println!("Digite um número:");
    std::io::stdin().read_line(&mut buffer);
    let mut num3: i32 = buffer.trim().parse().expect("");
    
    if num1 == num2 && num2 == num3{
        println!("O triangulo é equilatero.");
    }else if num1 == num2 || num2 == num3 || num1 == num3{
        println!("O triangulo é isoceles.");
    }else{
        println!("O triangulo é escaleno.")
    }
}
}