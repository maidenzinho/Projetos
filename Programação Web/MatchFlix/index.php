<?php
session_start();
require 'config/db.php';

$stmt = $pdo->query("SELECT * FROM movies");
$movies = $stmt->fetchAll();

$isAdmin = false;
if (isset($_SESSION['user_id'])) {
    $stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
    $stmt->execute([$_SESSION['user_id']]);
    $user = $stmt->fetch();

    if ($user && $user['is_admin'] == 1) {
        $isAdmin = true;
    }
}

function getAverageRating($movieId) {
    global $pdo;
    $stmt = $pdo->prepare("SELECT AVG(rating) AS average FROM reviews WHERE movie_id = ?");
    $stmt->execute([$movieId]);
    $result = $stmt->fetch();
    return $result['average'] ? round($result['average'], 1) : 'N/A';
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="css/styles.css">
    <title>Home</title>
    <script>
        function openReviewForm(movieId) {
            const rating = prompt("Avalie o filme de 1 a 5:");
            if (rating >= 1 && rating <= 5) {
                document.getElementById('reviewForm').action = 'submit_review.php';
                document.getElementById('movieId').value = movieId;
                document.getElementById('rating').value = rating;
                document.getElementById('reviewForm').submit();
            } else {
                alert("Por favor, insira um número entre 1 e 5.");
            }
        }
    </script>
</head>
<body>
    <header>
        <h1>Filmes</h1>
        <?php if (isset($_SESSION['user_id'])): ?>
            <a href="logout.php">Sair</a>
            <?php if ($isAdmin): ?>
                <a href="dashboard.php">Painel de Controle</a>
            <?php endif; ?>
        <?php else: ?>
            <a href="login.php">Login</a>
            <a href="register.php">Registrar</a>
        <?php endif; ?>
    </header>

    <main>
        <div class="movies-grid">
            <?php foreach ($movies as $movie): ?>
                <div class="movie-card">
                    <img src="<?php echo htmlspecialchars($movie['cover']); ?>" alt="Capa de <?php echo htmlspecialchars($movie['title']); ?>" style="width: 250px; height: 300px;">
                    <h3><?php echo htmlspecialchars($movie['title']); ?></h3>
                    <p>Diretor: <?php echo htmlspecialchars($movie['director']); ?></p>
                    <a class="movie-button" href="<?php echo htmlspecialchars($movie['video_url']); ?>" target="_blank">Assistir no YouTube</a>
                    <button class="review-button" onclick="openReviewForm(<?php echo htmlspecialchars($movie['id']); ?>)">Fazer Review</button>
                    <p class="rating-average">Média de Avaliações: <?php echo getAverageRating($movie['id']); ?></p>
                </div>
            <?php endforeach; ?>
        </div>
    </main>

    <form id="reviewForm" method="POST" style="display: none;">
        <input type="hidden" id="movieId" name="movie_id" value="">
        <input type="hidden" id="rating" name="rating" value="">
    </form>
</body>
</html>
