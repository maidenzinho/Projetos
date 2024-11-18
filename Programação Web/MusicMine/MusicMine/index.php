<?php
session_start();
require 'config/db.php'; // Inclua o arquivo de conexão

// Recupera todas as músicas cadastradas
$stmt = $pdo->query("SELECT * FROM musics");
$musics = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Home</title>
</head>
<body>
    <header>
        <h1>Music App</h1>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="login.php">Login</a></li>
                <li><a href="register.php">Registrar</a></li>
                <li><a href="dashboard.php">Dashboard</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Músicas</h2>
        <div class="music-list">
            <?php foreach ($musics as $music): ?>
                <div class="music-item">
                    <img src="<?php echo htmlspecialchars($music['cover']); ?>" alt="Capa da Música" width="250" height="300">
                    <h3><?php echo htmlspecialchars($music['title']); ?></h3>
                    <p><?php echo htmlspecialchars($music['artist']); ?></p>
                    <a href="<?php echo htmlspecialchars($music['video_url']); ?>" target="_blank" class="music-button">Ouvir no YouTube</a>
                </div>
            <?php endforeach; ?>
        </div>
    </main>
    <footer>
        <p>&copy; 2024 Music Mine</p>
    </footer>
</body>
</html>
