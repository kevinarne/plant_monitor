<?php
  include('../mysqli_connect.php')
?>

<html>
<head>
  <title>Test Display</title>
</head>


<body>
  <table border="0" cellspacing="0" cellpadding="4">
    <tr>
      <td>Col0</td>
      <td>Col1</td>
    </tr>
    <?php
      $query = "SELECT * FROM event_codes";
      $response = @mysqli_query($dbc,$query);
      if($response)
      {
        echo 'Success';
        while($row = mysqli_fetch>array($response))
        {
          echo '<tr>';
          echo '  <td>'.$row["id"].'</td>';
          echo '  <td>'.$row[""].'</td>';
          echo '</tr>';
        }
      }
    ?>
  </table>
</body>
</html>
