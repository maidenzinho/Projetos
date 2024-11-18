CREATE DATABASE AULA_STOREDPROCEDURE;
USE AULA_STOREPROCEDURE;
CREATE TABLE funcionario (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(80),
    salario DECIMAL(10, 2) NOT NULL,
    irpf DECIMAL(10, 2) DEFAULT 0
);

DELIMITER //
	CREATE PROCEDURE addFuncionario (IN addfuncionario_name VARCHAR(80), IN addfuncionario_salario DECIMAL(10, 2))
	BEGIN
		INSERT INTO funcionario(nome, salario) VALUES (addfuncionario_name, addfuncionario_salario); 
	END //
DELIMITER ;

CALL addFuncionario('Julio César', 5000);

DELIMITER //
CREATE PROCEDURE checarSalarioIRPF (IN nomeFun VARCHAR(80), IN salarioFun DECIMAL(10, 2))
BEGIN
    IF salarioFun <= 2259.21 THEN
        INSERT INTO funcionario (nome, salario, irpf) VALUES (nomeFun, salarioFun, 0);
    ELSEIF salarioFun <= 2826.65 THEN
        INSERT INTO funcionario (nome, salario, irpf) VALUES (nomeFun, salarioFun, 169.44);
    ELSEIF salarioFun <= 3751.05 THEN
        INSERT INTO funcionario (nome, salario, irpf) VALUES (nomeFun, salarioFun, 381.44);
    ELSEIF salarioFun <= 4664.68 THEN
        INSERT INTO funcionario (nome, salario, irpf) VALUES (nomeFun, salarioFun, 662.77);
    ELSE
        INSERT INTO funcionario (nome, salario, irpf) VALUES (nomeFun, salarioFun, 896.00);
    END IF;
END //
DELIMITER ;

CALL checarSalarioIRPF('Maycon Fernandes', 7000);
CALL checarSalarioIRPF('Bianca Caroline', 3000);

SELECT * FROM funcionario;

DELIMITER //
CREATE PROCEDURE checarSalarioIRPF_v2 (IN nomeFun VARCHAR(80), IN salarioFun DECIMAL(10, 2))
BEGIN
	DECLARE _irfp DECIMAL(10,2);
    IF salarioFun <= 2259.20 THEN
        SET _irpf = 0;
    ELSEIF salarioFun <= 2826.65 THEN
        SET _irpf = (salarioFun * 0.075) - 169.44;
    ELSEIF salarioFun <= 3751.05 THEN
        SET _irpf = (salarioFun * 0.15) - 381.44;
    ELSEIF salarioFun <= 4664.68 THEN
        SET _irpf = (salarioFun * 0.225) - 662.77;
    ELSE
        SET _irpf = (salarioFun * 0.275) - 896.00;
    END IF;
	INSERT INTO funcionario (nome, salario, irpf) VALUES (nomeFun, salarioFun, _irpf);
END //
DELIMITER ;

CALL checarSalarioIRPF('Monique Léticia', 3200);
CALL checarSalarioIRPF('Marcia Maria', 10000);

CREATE TABLE operadoresmatematicos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    mensagem TEXT
);

DELIMITER //
	CREATE PROCEDURE operadores_matematicos_basicos ( IN valor1 DECIMAL(10, 2), IN valor2 DECIMAL(10, 2) )
	BEGIN
		DECLARE ResultadoSoma DECIMAL(10,2);
		DECLARE ResultadoSubtracao DECIMAL(10,2);
		DECLARE ResultadoMultiplicacao DECIMAL(10,2);
		DECLARE ResultadoDivisao DECIMAL(10,2);
        DECLARE texto VARCHAR(255);
        
        SET ResultadoSoma = valor1 + valor2;
		SET texto = CONCAT(valor1, ' + ', valor2, ' = ', ResultadoSoma);
        INSERT INTO operadoresmatematicos (mensagem) VALUES (texto);
        
        SET ResultadoSubtracao = valor1 - valor2;
		SET texto = CONCAT(valor1, ' - ', valor2, ' = ', ResultadoSubtracao);
        INSERT INTO operadoresmatematicos (mensagem) VALUES (texto);
        
        SET ResultadoMultiplicacao = valor1 * valor2;
		SET texto = CONCAT(valor1, ' * ', valor2, ' = ', ResultadoMultiplicacao);
        INSERT INTO operadoresmatematicos (mensagem) VALUES (texto);
        
        IF valor2 != 0 THEN
			SET ResultadoDivisao = valor1 / valor2;
			SET texto = CONCAT(valor1, ' / ', valor2, ' = ', ResultadoDivisao);
			INSERT INTO operadoresmatematicos (mensagem) VALUES (texto);
        END IF;
        
	END //
DELIMITER ;

CALL operadores_matematicos_basicos(10, 2);
SELECT * FROM operadoresmatematicos;

CREATE TABLE tabela_exemplo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    valor INT
);

-- Apagar uma Procedure
DROP PROCEDURE IF EXISTS inserirValores;


DELIMITER //
CREATE PROCEDURE inserirValores()
BEGIN
    DECLARE contador INT DEFAULT 1;
    DECLARE limite INT DEFAULT 10;
    
    loop_exemplo: LOOP
		IF contador >= 10 THEN
			LEAVE loop_exemplo;
        END IF;
        -- Inserir o Contéudo na base de dados
        INSERT INTO tabela_exemplo (valor) VALUES (contador);
        SET contador = contador + 1;
    END LOOP loop_exemplo;
END //
DELIMITER ;

-- Exibir a Procedure
SHOW CREATE PROCEDURE inserirValores;

CALL inserirValores();
SELECT * FROM tabela_exemplo;

DELIMITER //
CREATE PROCEDURE CalcularMedia(IN number1 INT, IN number2 INT)
BEGIN
	DECLARE media INT;
    SET media = number1 / number2;
    SELECT media AS Media;
END //
DELIMITER ;
CALL CalcularMedia(1, 0);

DELIMITER //
CREATE PROCEDURE CalcularMediaTratamento(IN number1 INT, IN number2 INT)
BEGIN
    DECLARE media FLOAT;
    -- Usar CONTINUE HANDLER para capturar exceções
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        SELECT 'An error occurred' AS ErrorMessage;
    END;
    
    -- Lógica principal da stored procedure
    IF number2 = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Count cannot be zero.';
    ELSE
        SET media = number1 / number2;
        SELECT media AS Media;
    END IF;
END //
DELIMITER ;
CALL CalcularMediaTratamento(1, 0);

-- Próxima aula percorrer tabelas
-- Criação da Tabela
CREATE TABLE Funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    salario DECIMAL(10, 2) NOT NULL
);

INSERT INTO Funcionarios (nome, cargo, salario) VALUES
('João Silva', 'Gerente', 5000.00),
('Maria Oliveira', 'Desenvolvedor', 4000.00),
('Pedro Santos', 'Analista', 3000.00),
('Ana Costa', 'Desenvolvedor', 4500.00);

DELIMITER //
CREATE PROCEDURE SomaTotalSalarios(OUT totalSalarios DECIMAL(10, 2))
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE salarioAtual DECIMAL(10, 2);
    DECLARE cursorSalarios CURSOR FOR SELECT salario FROM Funcionarios;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    SET totalSalarios = 0;
    OPEN cursorSalarios;
    read_loop: LOOP
        FETCH cursorSalarios INTO salarioAtual;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET totalSalarios = totalSalarios + salarioAtual;
    END LOOP;
    CLOSE cursorSalarios;
END //
DELIMITER ;

-- Uso da Stored Procedure
CALL SomaTotalSalarios(@total);
SELECT @total AS TotalSalarios;
