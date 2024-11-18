<?php
require '../config/db.php';
header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $stmt = $pdo->query("SELECT * FROM Songs");
    $songs = $stmt->fetchAll(PDO::FETCH_ASSOC);
    echo json_encode($songs);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents("php://input"));
    $stmt = $pdo->prepare("INSERT INTO Songs (title, artist, youtube_url, vagalume_id, image_url) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute([$data->title, $data->artist, $data->youtube_url, $data->vagalume_id, $data->image_url]);
    echo json_encode(["status" => "success"]);
}
?>
