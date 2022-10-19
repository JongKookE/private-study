<?php
extract($_POST);
$location = $_POST["location"];
header("Location: $location");
exit;
?>
