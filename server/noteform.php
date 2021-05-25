<!DOCTYPE HTML>
<html>
<head>
</head>
<body>

<?php
$name = file_get_contents("notes.txt");
?>

<h2>PHP Form Validation Example</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  Name: <input type="text" name="name" value="<?php echo $name;?>">
  <br><br>
  <input type="submit" name="submit" value="Submit">
</form>

<?php
if (strcmp("", $_POST["name"]) !== 0) {
  $name = $_POST["name"];
  $output = shell_exec('sudo ./history.sh');
}
echo file_put_contents("notes.txt",$name);
echo "<h2>Your Input:</h2>";
echo $name;
?>

</body>
</html>
