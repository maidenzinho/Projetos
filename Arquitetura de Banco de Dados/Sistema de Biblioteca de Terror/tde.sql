-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 19/11/2024 às 03:06
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `tde`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `autores_sombrios`
--

CREATE TABLE `autores_sombrios` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `biografia` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `editoras_assombradas`
--

CREATE TABLE `editoras_assombradas` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `endereco` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `fretes_do_inferno`
--

CREATE TABLE `fretes_do_inferno` (
  `id` int(11) NOT NULL,
  `custo` decimal(10,2) NOT NULL,
  `metodo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `livros_malditos`
--

CREATE TABLE `livros_malditos` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `sinopse` text DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  `autor_id` int(11) NOT NULL,
  `editora_id` int(11) NOT NULL,
  `frete_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`, `role`) VALUES
(1, 'admin', '$2b$12$/eaGjHAmevE5iDNpctT0u.rMP7Ek8irkoVIDCWaeJyzmCufjkAbCO', 'gerente');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `autores_sombrios`
--
ALTER TABLE `autores_sombrios`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `editoras_assombradas`
--
ALTER TABLE `editoras_assombradas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `fretes_do_inferno`
--
ALTER TABLE `fretes_do_inferno`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `livros_malditos`
--
ALTER TABLE `livros_malditos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `autor_id` (`autor_id`),
  ADD KEY `editora_id` (`editora_id`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `autores_sombrios`
--
ALTER TABLE `autores_sombrios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `editoras_assombradas`
--
ALTER TABLE `editoras_assombradas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `fretes_do_inferno`
--
ALTER TABLE `fretes_do_inferno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `livros_malditos`
--
ALTER TABLE `livros_malditos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `livros_malditos`
--
ALTER TABLE `livros_malditos`
  ADD CONSTRAINT `livros_malditos_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores_sombrios` (`id`),
  ADD CONSTRAINT `livros_malditos_ibfk_2` FOREIGN KEY (`editora_id`) REFERENCES `editoras_assombradas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
