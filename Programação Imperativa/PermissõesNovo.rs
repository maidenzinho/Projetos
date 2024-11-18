struct Arquivo{
    nome: String,
    tamanho: u64,
    permissoes: (Permissao, Permissao, Permissao),
    uid: u16,
    gid: u16,
}
struct Permissao{
    leitura: u8,
    escrita: u8,
    execucao: u8,
}
impl Arquivo{
    fn new(nome: String, tamanho: u64, permissoes: (Permissao, Permissao, Permissao), uid: u16, gid: u16) -> Arquivo{
        Arquivo{nome, tamanho, permissoes, uid, gid}
    }
    fn stat(&self){
        println!("Arquivo: {}", self.nome);
        println!("Tamanho: {}", self.tamanho);
        println!("Permissões: {}/{}{}{}",format! ("{}{}{}",self.permissoes.0.octal(), self.permissoes.1.octal(), self.permissoes.2.octal()),self.permissoes.0.rwx(), self.permissoes.1.rwx(), self.permissoes.2.rwx());
        println!("Uid: {}", self.uid);
        println!("Gid: {}", self.gid);

    }
}
impl Permissao{
    fn new(leitura: u8, escrita: u8, execucao: u8) -> Permissao{
        Permissao{leitura, escrita, execucao}
    }
    fn rwx(&self) -> String{
        let leitura = if self.leitura == 1 {'r'} else {'-'};
        let escrita = if self.escrita == 1 {'w'} else {'-'};
        let execucao = if self.execucao == 1 {'x'} else {'-'};

        format!("{}{}{}", leitura, escrita, execucao)
    }
    fn octal(&self) -> u8{
        let a: u8 = self.leitura;
        let b: u8 = self.escrita;
        let c: u8 = self.execucao;

        match (a, b, c) {
            (0, 0, 0) => 0,
            (0, 0, 1) => 1,
            (0, 1, 0) => 2,
            (0, 1, 1) => 3,
            (1, 0, 0) => 4,
            (1, 0, 1) => 5,
            (1, 1, 0) => 6,
            (1, 1, 1) => 7,
            _ => 0,

        }
    }
}


fn main() {
    let permissao_usuario = Permissao::new(1, 1, 0);
    let permissao_grupo = Permissao::new(1, 1, 1);
    let permissao_outros = Permissao::new(0, 0, 0);

    let arquivo = Arquivo::new(
        String::from("meu_arquivo.txt"),
        1024,
        (permissao_usuario, permissao_grupo, permissao_outros),
        1000,
        1000,
    );

    arquivo.stat();
}