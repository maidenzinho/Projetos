<?php
session_start();
require 'config/db.php';

if (!isset($_GET['id'])) {
    header("Location: index.php");
    exit();
}

$id = $_GET['id'];
$stmt = $pdo->prepare("SELECT * FROM movies WHERE id = ?");
$stmt->execute([$id]);
$movie = $stmt->fetch();

if (!$movie) {
    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title><?php echo htmlspecialchars($movie['title']); ?></title>
</head>
<body>
    <header>
        <h1><?php echo htmlspecialchars($movie['title']); ?></h1>
        <?php if (isset($_SESSION['user_id'])): ?>
            <a href="logout.php">Sair</a>
        <?php else: ?>
            <a href="login.php">Login</a>
            <a href="register.php">Registrar</a>
        <?php endif; ?>
    </header>

    <main>
        <img src="<?php echo htmlspecialchars($movie['cover']); ?>" alt="Capa do Filme" width="250" height="300">
        <h3>Diretor: <?php echo htmlspecialchars($movie['director']); ?></h3>
        <a href="<?php echo htmlspecialchars($movie['video_url']); ?>" target="_blank" class="movie-button">Assistir Trailer</a>
        
        <h4>Avaliações</h4>
        <form action="submit_review.php" method="POST">
            <textarea name="review" placeholder="Escreva sua avaliação..."></textarea>
            <input type="hidden" name="movie_id" value="<?php echo $movie['id']; ?>">
            <button type="submit">Enviar Avaliação</button>
        </form>
    </main>

    <script src="js/scripts.js"></script>
</body>
</html>
