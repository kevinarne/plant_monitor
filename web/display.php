<?php
  include('mysqli_connect.php')
?>

<html>
<head>
  <title>Test Display</title>
</head>


<body>
  <?php
  $query = "SELECT * FROM event_codes";
  $response = @mysqli_query($dbc,$query);
  echo 'Success';
  ?>
</body>
</html>
