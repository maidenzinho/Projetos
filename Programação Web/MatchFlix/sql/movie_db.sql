-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 04/11/2024 às 18:22
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
-- Banco de dados: `movie_db`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `movies`
--

CREATE TABLE `movies` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `director` varchar(100) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `video_url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `movies`
--

INSERT INTO `movies` (`id`, `title`, `director`, `cover`, `video_url`) VALUES
(7, 'O Menino e a Garça', 'Hayao Miyazaki', 'https://s2-quem.glbimg.com/fTu3hlT9y7ADSAfjqaWG89nGKWc=/0x0:1400x2001/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_b0f0e84207c948ab8b8777be5a6a4395/internal_photos/bs/2024/r/l/YAE6UETp28OU2vpYDFMg/mi2.jpg', 'https://www.youtube.com/watch?v=hCg9h3ILzJ4'),
(8, 'Ponyo', 'Hayao Miyazaki', 'https://cps-static.rovicorp.com/1/adg/cov584/dru900/u955/u95585dn34g.jpg', 'https://www.youtube.com/watch?v=pfGDfDjAdSE'),
(9, 'A Viagem de Chihiro', 'Hayao Miyazaki', 'https://media.fstatic.com/MRIQ6jV3dlxrs306FSYfeM6e_f0=/290x478/smart/media/movies/covers/2014/08/a-viagem-de-chihiro_t1246_4.jpg', 'https://www.youtube.com/watch?v=ByXuk9QqQkk'),
(10, 'Meu Amigo Totoro', 'Hayao Miyazaki', 'https://www.cinemaclock.com/images/posters/1000x1500/34/tonari-no-totoro-1988-orig-poster.jpg', 'https://www.youtube.com/watch?v=92a7Hj0ijLs'),
(11, 'O Castelo Animado', 'Hayao Miyazaki', 'https://www.justwatch.com/images/poster/265223874/s718/o-castelo-animado.jpg', 'https://www.youtube.com/watch?v=iwROgK94zcM&pp=ygUZdHJhaWxlciBvIGNhc3RlbG8gYW5pbWFkbw%3D%3D'),
(12, 'O Serviço de Entregas da Kiki', 'Hayao Miyazaki', 'https://i2.wp.com/studioghibli.com.br/wp-content/uploads/2020/04/O-Serviço-de-Entregas-da-Kiki-versátil.jpg', 'https://www.youtube.com/watch?v=4bG17OYs-GA');

-- --------------------------------------------------------

--
-- Estrutura para tabela `reviews`
--

CREATE TABLE `reviews` (
  `id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL CHECK (`rating` >= 1 and `rating` <= 5),
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `reviews`
--

INSERT INTO `reviews` (`id`, `movie_id`, `user_id`, `rating`, `created_at`) VALUES
(1, 6, 1, 4, '2024-11-03 13:43:03'),
(2, 7, 5, 5, '2024-11-04 00:29:28'),
(3, 6, 5, 3, '2024-11-04 00:29:35'),
(4, 6, 5, 5, '2024-11-04 00:29:49'),
(5, 7, 5, 4, '2024-11-04 00:29:54'),
(6, 7, 5, 5, '2024-11-04 16:47:13'),
(7, 8, 5, 5, '2024-11-04 16:47:16'),
(8, 8, 5, 3, '2024-11-04 16:47:20'),
(9, 8, 5, 5, '2024-11-04 16:47:22'),
(10, 8, 5, 5, '2024-11-04 16:47:25'),
(11, 6, 5, 5, '2024-11-04 16:47:33'),
(12, 9, 5, 5, '2024-11-04 16:58:01'),
(13, 9, 5, 5, '2024-11-04 16:58:03'),
(14, 9, 5, 5, '2024-11-04 16:58:07'),
(15, 9, 5, 5, '2024-11-04 16:58:09'),
(16, 10, 5, 5, '2024-11-04 16:58:13'),
(17, 10, 5, 4, '2024-11-04 16:58:15'),
(18, 10, 5, 5, '2024-11-04 16:58:16'),
(19, 11, 5, 5, '2024-11-04 16:58:20'),
(20, 11, 5, 5, '2024-11-04 16:58:22'),
(21, 12, 5, 5, '2024-11-04 16:58:25'),
(22, 12, 5, 4, '2024-11-04 16:58:26'),
(23, 12, 5, 5, '2024-11-04 16:58:28');

-- --------------------------------------------------------

--
-- Estrutura para tabela `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `is_admin` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `is_admin`) VALUES
(1, 'felipe', '$2y$10$zNL52mdydR9BQLyRExq95OhBWWPZKhF5woZhJRE.DEKLjiUAk2Ute', 1),
(5, 'teste', '$2y$10$GVZISwiRCVvfXxH9CiaTyehSJfTQXC5Ag1OiNA/N8ZUt3Dw2/84su', 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `movies`
--
ALTER TABLE `movies`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `movie_id` (`movie_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Índices de tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `movies`
--
ALTER TABLE `movies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
