CREATE DATABASE LOJA;

USE LOJA;

CREATE TABLE Pessoa (
  id_pessoa INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  nome_completo VARCHAR(255) NOT NULL,
  CPF INT(11) UNIQUE NOT NULL,
  RG INT(9) UNIQUE NOT NULL,
  data_nascimento DATE NOT NULL,
  email VARCHAR(45) NOT NULL UNIQUE,
  telefone VARCHAR(20) NOT NULL,
  endereco VARCHAR(255) NOT NULL,
  data_de_cadastro DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE Cliente (
  id_cliente INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  data_de_cadastro DATE NOT NULL DEFAULT CURRENT_DATE,
  status_do_cliente INT(1) NOT NULL,
  tipo_de_cliente VARCHAR(45) NOT NULL
);

CREATE TABLE Funcionario (
  ID_Funcionario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  matricula INT NOT NULL UNIQUE,
  Data_de_Admissão DATE NOT NULL DEFAULT CURRENT_DATE,
  Cargo VARCHAR(45) NOT NULL,
  Salário DECIMAL(10,2) NOT NULL,
  departamento VARCHAR(45) NOT NULL,
  Supervisor VARCHAR(45) NOT NULL,
  Horário_de_Trabalho DATETIME NOT NULL,
  Data_de_Demissão DATE,
  Status_do_Funcionário INT(1) NOT NULL
);

CREATE TABLE Produto (
  ID_Produto INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  Descrição VARCHAR(255) NOT NULL,
  Categoria VARCHAR(45) NOT NULL,
  preco DECIMAL(10,2) NOT NULL,
  Quantidade_em_Estoque INT NOT NULL
);

CREATE TABLE Carrinho (
  ID_Carrinho INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  data_de_criacao DATE NOT NULL,
  Data_de_Atualizacao DATE NOT NULL,
  Status INT(1) NOT NULL
);

CREATE TABLE Pedido (
  id_pedido INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  id_pessoa INT NOT NULL,
  FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id_pessoa),
  data_do_pedido DATE NOT NULL DEFAULT CURRENT_DATE,
  total_do_pedido DECIMAL(10,2) NOT NULL,
  metodo_de_pagamento VARCHAR(45) NOT NULL,
  obsevações VARCHAR(45) NOT NULL
);

CREATE TABLE StatusEntrega (
  aguardando_pagamento INT(1) NOT NULL,
  em_processamento VARCHAR(45) NOT NULL,
  enviado INT(1) NOT NULL,
  entregue INT(1) NOT NULL
);

CREATE TABLE avaliacao (
    id_avaliacao INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data_avaliacao DATE NOT NULL DEFAULT CURRENT_DATE,
    nota INT(1) NOT NULL,
    comentario VARCHAR(255) NOT NULL
);

CREATE TABLE cobranca (
    id_cobranca INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data_de_emissao DATE NOT NULL DEFAULT CURRENT_DATE,
    data_vencimento DATE NOT NULL DEFAULT CURRENT_DATE,
    status_da_cobranca INT(1) NOT NULL,
    valor_da_cobranca DECIMAL(10,2) NOT NULL,
    metodo_de_pagamento VARCHAR(45) NOT NULL,
    data_de_pagamento DATE NOT NULL DEFAULT CURRENT_DATE
);

CREATE TABLE entrega (
    id_entrega INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    data_de_saida DATE NOT NULL,
    data_de_estimada_de_entrega DATE NOT NULL,
    data_de_entrega_real DATE DEFAULT CURRENT_DATE,
    metodo_de_envio VARCHAR(45) NOT NULL,
    rastreamento INT NOT NULL
);
CREATE TABLE forma_de_pagamento (
    id_formapagamento INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(45) NOT NULL,
    taxa_de_trasacao DECIMAL(10,2) NOT NULL,
    prazo_de_compensacao DATE NOT NULL,
    status_da_forma INT NOT NULL
);

INSERT INTO forma_de_pagamento (descricao, taxa_de_trasacao, prazo_de_compensacao, status_da_forma) VALUES
('Cartão de Crédito', 2.5, '2023-10-01', 1),
('Cartão de Débito', 1.5, '2023-10-01', 1),
('Boleto Bancário', 0.0, '2023-10-05', 1),
('Transferência Bancária', 0.5, '2023-10-01', 1),
('PayPal', 3.0, '2023-10-01', 1),
('Pix', 0.0, '2023-10-01', 1),
('Dinheiro', 0.0, '2023-10-01', 1),
('Cheque', 0.0, '2023-10-10', 1),
('Financiamento', 5.0, '2023-10-01', 1),
('Consórcio', 2.0, '2023-10-01', 1),
('Crédito Direto', 4.0, '2023-10-01', 1),
('Débito Automático', 1.0, '2023-10-01', 1);

DELIMITER $$

CREATE PROCEDURE AdicionarFuncionario (
    IN p_nome_completo VARCHAR(255),
    IN p_CPF VARCHAR(11),
    IN p_RG VARCHAR(9),
    IN p_data_nascimento DATE,
    IN p_email VARCHAR(45),
    IN p_telefone VARCHAR(20),
    IN p_endereco VARCHAR(255),
    IN p_data_admissao DATE,
    IN p_cargo VARCHAR(45),
    IN p_salario DECIMAL(10,2),
    IN p_departamento VARCHAR(45),
    IN p_supervisor VARCHAR(45),
    IN p_horario_de_trabalho DATETIME,
    IN p_status_do_funcionario INT
)
BEGIN
    DECLARE v_primeiro_digito INT;
    DECLARE v_segundo_digito INT;
    DECLARE v_valido BOOLEAN DEFAULT TRUE;
    DECLARE v_soma INT;
    DECLARE v_resto INT;
    DECLARE v_matricula VARCHAR(20);

    SET v_matricula = CONCAT(DATE_FORMAT(p_data_admissao, '%y%m%d'), DATE_FORMAT(p_horario_de_trabalho, '%H%i'), p_supervisor);

    SET v_soma = (CAST(SUBSTRING(p_CPF, 1, 1) AS UNSIGNED) * 10) +
                  (CAST(SUBSTRING(p_CPF, 2, 1) AS UNSIGNED) * 9) +
                  (CAST(SUBSTRING(p_CPF, 3, 1) AS UNSIGNED) * 8) +
                  (CAST(SUBSTRING(p_CPF, 4, 1) AS UNSIGNED) * 7) +
                  (CAST(SUBSTRING(p_CPF, 5, 1) AS UNSIGNED) * 6) +
                  (CAST(SUBSTRING(p_CPF, 6, 1) AS UNSIGNED) * 5) +
                  (CAST(SUBSTRING(p_CPF, 7, 1) AS UNSIGNED) * 4) +
                  (CAST(SUBSTRING(p_CPF, 8, 1) AS UNSIGNED) * 3) +
                  (CAST(SUBSTRING(p_CPF, 9, 1) AS UNSIGNED) * 2);
    
    SET v_resto = (v_soma * 10) % 11;
    SET v_primeiro_digito = IF(v_resto = 10, 0, v_resto);

    IF v_primeiro_digito != CAST(SUBSTRING(p_CPF, 10, 1) AS UNSIGNED) THEN
        SET v_valido = FALSE;
    END IF;

    IF v_valido THEN
        SET v_soma = (CAST(SUBSTRING(p_CPF, 1, 1) AS UNSIGNED) * 11) +
                      (CAST(SUBSTRING(p_CPF, 2, 1) AS UNSIGNED) * 10) +
                      (CAST(SUBSTRING(p_CPF, 3, 1) AS UNSIGNED) * 9) +
                      (CAST(SUBSTRING(p_CPF, 4, 1) AS UNSIGNED) * 8) +
                      (CAST(SUBSTRING(p_CPF, 5, 1) AS UNSIGNED) * 7) +
                      (CAST(SUBSTRING(p_CPF, 6, 1) AS UNSIGNED) * 6) +
                      (CAST(SUBSTRING(p_CPF, 7, 1) AS UNSIGNED) * 5) +
                      (CAST(SUBSTRING(p_CPF, 8, 1) AS UNSIGNED) * 4) +
                      (CAST(SUBSTRING(p_CPF, 9, 1) AS UNSIGNED) * 3) +
                      (v_primeiro_digito * 2);
        
        SET v_resto = (v_soma * 10) % 11;
        SET v_segundo_digito = IF(v_resto = 10, 0, v_resto);

        IF v_segundo_digito != CAST(SUBSTRING(p_CPF, 11, 1) AS UNSIGNED) THEN
            SET v_valido = FALSE;
        END IF;
    END IF;

    IF v_valido THEN
        IF p_CPF NOT IN ('00000000000', '11111111111', '22222222222', '33333333333', 
                         '44444444444', '55555555555', '66666666666', '77777777777', 
                         '88888888888', '99999999999') THEN
            INSERT INTO Funcionario (nome_completo, CPF, RG, data_nascimento, email, telefone, endereco

DELIMITER $$

CREATE FUNCTION CalcularSalarioAnual(p_matricula INT)
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE v_salario_mensal DECIMAL(10,2);
    SELECT Salário INTO v_salario_mensal FROM Funcionario WHERE matricula = p_matricula;
    RETURN IFNULL(v_salario_mensal * 12, 0);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE AtualizarEstoqueProduto (
    IN p_id_produto INT,
    IN p_nova_quantidade INT
)
BEGIN
    UPDATE Produto
    SET quantidade_estoque = p_nova_quantidade
    WHERE id_produto = p_id_produto;
END $$

DELIMITER ;

SELECT 
    u.id_usuario,
    u.nome,
    c.id_produto,
    c.quantidade
FROM 
    usuarios u
LEFT JOIN 
    carrinho c ON u.id_usuario = c.id_usuario
ORDER BY 
    u.id_usuario;

SELECT 
    p.id_pedido,
    p.id_usuario,
    u.nome,
    p.data_pedido,
    p.status
FROM 
    pedidos p
JOIN 
    usuarios u ON p.id_usuario = u.id_usuario
WHERE 
    p.forma_pagamento = 'Boleto'
ORDER BY 
    p.data_pedido DESC;