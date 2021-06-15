<?php
require_once('creds.php');

$dbc = @mysqli_connect(HOST_NAME, USER_NAME, PASSWORD, DN_NAME) OR die('Could not connect to MySQL ' . mysqli_connect_error());
$query = "SELECT * FROM event_codes;"

$response = @mysqli_query($dbc, $query);
echo '<h1>Query succeeded</h>'
?>
