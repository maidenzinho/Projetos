<?php
session_start();
require 'config/db.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $movie_id = $_POST['movie_id'];
    $user_id = $_SESSION['user_id'];
    $rating = $_POST['rating'];

    $stmt = $pdo->prepare("INSERT INTO reviews (movie_id, user_id, rating) VALUES (?, ?, ?)");
    $stmt->execute([$movie_id, $user_id, $rating]);

    header("Location: index.php");
    exit();
}
?>
