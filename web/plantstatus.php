<?php
  include('../mysqli_connect.php')
?>

<html>
<head>
  <title>Plant Statuses</title>
</head>


<body>
  <table border="0" cellspacing="0" cellpadding="4">
    <tr>
      <td>Plant</td>
      <td>Current Weight</td>
      <td>Last Watering</td>
    </tr>
    <?php
      $query = "SELECT * FROM plant_events WHERE code=2";
      $events = @mysqli_query($dbc,$query);
      $plants = @mysqli_query($dbc,"SELECT * FROM plants");

      if($events && $plants)
      {
        // Create display array from the plants table with empty values
          // $display = array(id => array(name =>, waterdate=>,waterweight=>,mostrecent=>));
        // Create temporary variables for each plant to store yesterday's date, yesterday's weight, and today's weight
          // $temp = array(id => array(yesterweight =>, yesterdate=>);
        // Traverse the events array
          // Determine which plant it pertains to
          // If there's a value for yesterday's date, and yesterday's weight
            // Compare today's weight to yesterday's and store the date and weight in the watering event if today's is greater than yesterday's
            // Store today's weight in display array
          // Store today's weight and date in yesterday's
        while($row = mysqli_fetch_array($events))
        {
          echo '<tr>';
          echo '  <td>'.$row["plant"].'</td>';
          echo '  <td>'.$row["val"].'</td>';
          echo '  <td>'.0.'</td>';
          echo '</tr>';
        }
      }
    ?>
  </table>
</body>
</html>
