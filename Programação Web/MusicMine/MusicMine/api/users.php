<?php
require '../config/db.php';
session_start();
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action'])) {
    if ($_POST['action'] === 'register') {
        $username = $_POST['username'];
        $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
        $stmt = $pdo->prepare("INSERT INTO Users (username, password_hash) VALUES (?, ?)");
        $stmt->execute([$username, $password]);
        echo json_encode(["status" => "success"]);
    }

    if ($_POST['action'] === 'login') {
        $username = $_POST['username'];
        $password = $_POST['password'];
        $stmt = $pdo->prepare("SELECT * FROM Users WHERE username = ?");
        $stmt->execute([$username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($user && password_verify($password, $user['password_hash'])) {
            $_SESSION['user_id'] = $user['id'];
            echo json_encode(["status" => "success"]);
        } else {
            echo json_encode(["status" => "error", "message" => "Invalid credentials."]);
        }
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_SESSION['user_id'])) {
    echo json_encode(["status" => "success", "user_id" => $_SESSION['user_id']]);
}
?>
