<?php
session_start();
require 'config/db.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user_id = $_POST['user_id'];
    $is_admin = $_POST['is_admin'] == '1' ? 0 : 1;

    $stmt = $pdo->prepare("UPDATE users SET is_admin = ? WHERE id = ?");
    $stmt->execute([$is_admin, $user_id]);

    header("Location: manage_users.php");
    exit();
}

$stmt = $pdo->query("SELECT * FROM users");
$users = $stmt->fetchAll();
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Gerenciar Usuários</title>
</head>
<body>
    <header>
        <h1>Gerenciar Usuários</h1>
        <a href="logout.php">Sair</a>
    </header>

    <main>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome de Usuário</th>
                    <th>Status Admin</th>
                    <th>Ação</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($users as $user): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($user['id']); ?></td>
                        <td><?php echo htmlspecialchars($user['username']); ?></td>
                        <td><?php echo $user['is_admin'] ? 'Admin' : 'Usuário'; ?></td>
                        <td>
                            <form action="manage_users.php" method="POST">
                                <input type="hidden" name="user_id" value="<?php echo htmlspecialchars($user['id']); ?>">
                                <input type="hidden" name="is_admin" value="<?php echo htmlspecialchars($user['is_admin']); ?>">
                                <button type="submit"><?php echo $user['is_admin'] ? 'Remover Admin' : 'Tornar Admin'; ?></button>
                            </form>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </main>
</body>
</html>
