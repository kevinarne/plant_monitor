<?php
require_once('../../creds.php');

$dbc = @mysqli_connect(HOST_NAME, USER_NAME, PASSWORD, DB_NAME) OR die('Could not connect');
$query = "SELECT * FROM event_codes;";

$response = @mysqli_query($dbc,$query);

if($response)
{
	echo "Test4";
}
?>
