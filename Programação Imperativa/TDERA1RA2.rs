struct Arquivo{
    nome: String,
    tamanho: u64,
    permissoes: (Permissao, Permissao, Permissao),
    usuario: Usuario,
    grupo: Grupo,
}
struct Permissao{
    leitura: bool,
    escrita: bool,
    execucao: bool,
}
struct Diretorio{
    nome: String,
    arquivos: Vec<Arquivo>,
    permissoes: (Permissao, Permissao, Permissao),
    dono: Usuario,
}
struct Usuario{
    nome: String,
    uid: u16,
    grupo: Grupo,
}
struct Grupo{
    nome: String,
    gid: u16,
    membros: Vec<Usuario>,
}
impl Arquivo{
    fn new(nome: String, tamanho: u64, uid: u16, gid: u16) -> Arquivo{
        Arquivo{nome, tamanho, uid, gid}
    }
    fn alterar_permissao(&self, Permissao){
    }
    fn stat(&self){
        println!("Arquivo: {}", self.nome);
        println!("Tamanho: {}", self.tamanho);
        println!("Permissões: {}{}{}", self.permissoes.0.octal(), self.permissoes.1.octal(), self.permissoes.2.octal());
        println!("Uid: {}", self.uid);
        println!("Gid: {}", self.gid);
    }
}
impl Permissao{
    fn new(leitura: u8, escrita: u8, execucao: u8) -> Permissao{
        Permissao{leitura, escrita, execucao}
    }
    fn octal(&self) -> u8{
        let a: u8 = self.leitura;
        let b: u8 = self.escrita;
        let c: u8 = self.execucao;
    }
}
impl Diretorio{
    fn new(nome: String, permissao: bool, dono: Usuario) -> Diretorio{
        Diretorio{nome, permissao, dono}
    }
    fn adiciona_arquivo(nome: String){
    }
    fn remove_arquivo(nome: String){
    }
    fn listar_conteudo(){
    }
}
impl Usuario{
    fn new(nome: String, uid: u16, grupo: Grupo) -> Usuario{
        Usuario{nome, uid, grupo}
    }
    fn adiciona_grupo(grupo: Grupo){
    }
    fn remove_grupo(grupo: Grupo){
    }
    fn listar_grupos(){
    }
}
impl Grupo{
    fn new(nome: String, gid: u16) -> Grupo{
        Grupo{nome, gid}
    }
    fn adiciona_membro(usuario: Usuario){
    }
    fn remove_membro(usuario: Usuario){
    }
    fn listar_membro(){
    }
}

fn main(){

}