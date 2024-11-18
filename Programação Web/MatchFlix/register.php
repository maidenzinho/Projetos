<?php
session_start();
require 'config/db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);

    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->execute([$username, $password]);
    
    header("Location: login.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Registrar</title>
    <a href="index.php">Inicio</a>
</head>
<body>
    <h1>Registrar</h1>
    <form action="register.php" method="POST">
        <input type="text" name="username" placeholder="Nome de usuário" required>
        <input type="password" name="password" placeholder="Senha" required>
        <button type="submit">Registrar</button>
    </form>
</body>
</html>
