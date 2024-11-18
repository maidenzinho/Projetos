<!-- CREATE TABLE nometabela (
    id INT AUTO_INCREMENT PRIMARY KEY,
    texto VARCHAR(100) NOT NULL,
    numreal FLOAT NOT NULL,
); -->
<?php
$servername = "localhost";
$username = "seu_usuario";
$password = "sua_senha";
$dbname = "seu_banco_de_dados";
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $arg1 = $_POST['argumento_post'];

    $sql = "INSERT INTO nome_tablea (campo1, campo2) VALUES ('$arg1', '$arg1')";

    if ($conn->query($sql) === TRUE) {
        echo "Nova dado adicionada com sucesso";
    } else {
        echo "Erro: " . $sql . "<br>" . $conn->error;
    }
}
$conn->close();
?>

<!DOCTYPE html>
<html>
<body>
<h2>Adicionar Música</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  parametro1: <input type="text" name="argumento_post" required><br><br>
  <input type="submit" value="Adicionar">
</form>

</body>
</html>
