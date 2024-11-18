<?php
session_start();
require 'config/db.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = $_POST['title'];
    $director = $_POST['director'];
    $cover = $_POST['cover'];
    $video_url = $_POST['video_url'];

    $stmt = $pdo->prepare("INSERT INTO movies (title, director, cover, video_url) VALUES (?, ?, ?, ?)");
    $stmt->execute([$title, $director, $cover, $video_url]);
    
    header("Location: dashboard.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Painel de Controle</title>
</head>
<body>
    <header>
        <h1>Painel de Controle</h1>
        <a href="index.php">Inicio</a>
        <a href="logout.php">Sair</a>
    </header>

    <main>
        <h2>Adicionar Filme</h2>
        <form action="dashboard.php" method="POST">
            <input type="text" name="title" placeholder="Título do Filme" required>
            <input type="text" name="director" placeholder="Diretor" required>
            <input type="text" name="cover" placeholder="URL da Capa" required>
            <input type="text" name="video_url" placeholder="URL do Vídeo" required>
            <button type="submit">Adicionar Filme</button>
        </form>
    </main>
</body>
</html>
