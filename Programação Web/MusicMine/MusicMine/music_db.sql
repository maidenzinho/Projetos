-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 03/11/2024 às 05:40
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
-- Banco de dados: `music_db`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `musics`
--

CREATE TABLE `musics` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `artist` varchar(255) NOT NULL,
  `cover` varchar(255) NOT NULL,
  `video_url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `musics`
--

INSERT INTO `musics` (`id`, `title`, `artist`, `cover`, `video_url`) VALUES
(1, 'Never Gonna Give You Up', 'Rick Astley', 'https://c8.alamy.com/comp/2JAC6FX/picture-cover-of-the-seven-inch-single-version-of-never-gonna-give-you-up-by-rick-astley-which-was-released-in-1987-2JAC6FX.jpg', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
(2, 'Sweet Child O\' Mine', 'Guns N\' Roses', 'https://i.discogs.com/xMT_wLJexbB86D5xmGJXjMeGIALQugG_xrbjN2mh2-w/rs:fit/g:sm/q:90/h:600/w:600/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTk3NDAx/OC0xNDQyMjcxNjA1/LTQ0ODMuanBlZw.jpeg', 'https://www.youtube.com/watch?v=1w7OgIMMRc4');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Playlists`
--

CREATE TABLE `Playlists` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `song_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `Songs`
--

CREATE TABLE `Songs` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `artist` varchar(100) NOT NULL,
  `youtube_url` varchar(255) NOT NULL,
  `vagalume_id` varchar(50) NOT NULL,
  `image_url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `Songs`
--

INSERT INTO `Songs` (`id`, `title`, `artist`, `youtube_url`, `vagalume_id`, `image_url`) VALUES
(1, 'Song Title 1', 'Artist 1', 'https://www.youtube.com/embed/VIDEO_ID_1', 'song-title-1', 'https://via.placeholder.com/250x300'),
(2, 'Song Title 2', 'Artist 2', 'https://www.youtube.com/embed/VIDEO_ID_2', 'song-title-2', 'https://via.placeholder.com/250x300'),
(3, 'Song Title 3', 'Artist 3', 'https://www.youtube.com/embed/VIDEO_ID_1', 'song-title-1', 'https://via.placeholder.com/250x300'),
(4, 'Song Title 4', 'Artist 4', 'https://www.youtube.com/embed/VIDEO_ID_2', 'song-title-2', 'https://via.placeholder.com/250x300');

-- --------------------------------------------------------

--
-- Estrutura para tabela `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'mfweinf', '$2y$10$l7Cqs5P1R41r8WmmsJ5.Q.wMKleXjYojK8BgBdt/EHOQLcG4H8oDW'),
(2, 'teste', '$2y$10$ulGzhMClZ7zkAAmNubCVou6C.VMrc9Dl6ngdgD28dKESEFh99i3jW');

-- --------------------------------------------------------

--
-- Estrutura para tabela `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `musics`
--
ALTER TABLE `musics`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `Playlists`
--
ALTER TABLE `Playlists`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `song_id` (`song_id`);

--
-- Índices de tabela `Songs`
--
ALTER TABLE `Songs`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Índices de tabela `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `musics`
--
ALTER TABLE `musics`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `Playlists`
--
ALTER TABLE `Playlists`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `Songs`
--
ALTER TABLE `Songs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `Playlists`
--
ALTER TABLE `Playlists`
  ADD CONSTRAINT `Playlists_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  ADD CONSTRAINT `Playlists_ibfk_2` FOREIGN KEY (`song_id`) REFERENCES `Songs` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
