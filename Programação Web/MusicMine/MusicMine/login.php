<?php
session_start();
require 'config/db.php'; // Inclua o arquivo de conexão

$error = ""; // Inicializa a variável de erro

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Verifica se o usuário existe
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($password, $user['password'])) {
        // Login bem-sucedido
        $_SESSION['user_id'] = $user['id'];
        header("Location: dashboard.php"); // Redireciona para o painel
        exit();
    } else {
        $error = "Nome de usuário ou senha incorretos.";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Login</title>
</head>
<body>
    <header>
        <h1>Login</h1>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="register.php">Registrar</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <?php if ($error): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        <form method="POST" id="login-form">
            <input type="text" name="username" placeholder="Nome de Usuário" required>
            <input type="password" name="password" placeholder="Senha" required>
            <button type="submit">Login</button>
        </form>
    </main>
    <footer>
        <p>&copy; 2024 Music Mine</p>
    </footer>
</body>
</html>
