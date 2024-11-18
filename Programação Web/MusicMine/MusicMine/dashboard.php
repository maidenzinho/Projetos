<?php
session_start();
require 'config/db.php'; // Inclua o arquivo de conexão

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php"); // Redireciona para o login se não estiver logado
    exit();
}

// Adicionar música
$error = "";
$success = "";

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['add_music'])) {
    $title = trim($_POST['title']);
    $artist = trim($_POST['artist']);
    $cover = trim($_POST['cover']);
    $video_url = trim($_POST['video_url']);

    // Verifica se todos os campos foram preenchidos
    if (empty($title) || empty($artist) || empty($cover) || empty($video_url)) {
        $error = "Por favor, preencha todos os campos.";
    } else {
        // Insere a nova música no banco de dados
        $stmt = $pdo->prepare("INSERT INTO musics (title, artist, cover, video_url) VALUES (:title, :artist, :cover, :video_url)");
        if ($stmt->execute(['title' => $title, 'artist' => $artist, 'cover' => $cover, 'video_url' => $video_url])) {
            $success = "Música adicionada com sucesso!";
        } else {
            $error = "Erro ao adicionar a música. Tente novamente.";
        }
    }
}

// Recupera todas as músicas cadastradas
$stmt = $pdo->query("SELECT * FROM musics");
$musics = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Dashboard</title>
</head>
<body>
    <header>
        <h1>Dashboard</h1>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="logout.php">Logout</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <?php if ($error): ?>
            <div class="error"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>
        <?php if ($success): ?>
            <div class="success"><?php echo htmlspecialchars($success); ?></div>
        <?php endif; ?>
        
        <h2>Adicionar Música</h2>
        <form method="POST">
            <input type="text" name="title" placeholder="Título da Música" required>
            <input type="text" name="artist" placeholder="Artista" required>
            <input type="text" name="cover" placeholder="URL da Capa" required>
            <input type="text" name="video_url" placeholder="URL do Vídeo do YouTube" required>
            <button type="submit" name="add_music">Adicionar Música</button>
        </form>

        <h2>Músicas Cadastradas</h2>
        <ul>
            <?php foreach ($musics as $music): ?>
                <li>
                    <h3><?php echo htmlspecialchars($music['title']); ?> - <?php echo htmlspecialchars($music['artist']); ?></h3>
                    <img src="<?php echo htmlspecialchars($music['cover']); ?>" alt="Capa da Música" width="100">
                    <br>
                    <a href="<?php echo htmlspecialchars($music['video_url']); ?>" target="_blank">Ouvir no YouTube</a>
                </li>
            <?php endforeach; ?>
        </ul>
    </main>
    <footer>
        <p>&copy; 2024 Music Mine</p>
    </footer>
</body>
</html>
