<?php
session_start();
require 'config/db.php'; // Inclua o arquivo de conexão

$error = ""; // Inicializa a variável de erro

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Verifica se o usuário já existe
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);

    if ($stmt->rowCount() > 0) {
        $error = "Usuário já existe.";
    } else {
        // Insere o novo usuário no banco de dados
        $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
        $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
        if ($stmt->execute(['username' => $username, 'password' => $hashedPassword])) {
            $_SESSION['user_id'] = $pdo->lastInsertId(); // Loga o novo usuário
            header("Location: dashboard.php"); // Redireciona para o painel
            exit();
        } else {
            $error = "Erro ao registrar. Tente novamente.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Registrar</title>
</head>
<body>
    <header>
        <h1>Registrar</h1>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="login.php">Login</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <?php if ($error): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        <form method="POST" id="register-form">
            <input type="text" name="username" placeholder="Nome de Usuário" required>
            <input type="password" name="password" placeholder="Senha" required>
            <button type="submit">Registrar</button>
        </form>
    </main>
    <footer>
        <p>&copy; 2024 Music Mine</p>
    </footer>
</body>
</html>
