<?php
session_start();
require 'config/db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        header("Location: index.php");
        exit();
    } else {
        $error = "Usuário ou senha inválidos!";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Login</title>
    <a href="index.php">Inicio</a>
</head>
<body>
    <h1>Login</h1>
    <?php if (isset($error)): ?>
        <p><?php echo htmlspecialchars($error); ?></p>
    <?php endif; ?>
    <form action="login.php" method="POST">
        <input type="text" name="username" placeholder="Nome de usuário" required>
        <input type="password" name="password" placeholder="Senha" required>
        <button type="submit">Entrar</button>
    </form>
</body>
</html>
