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
      <td>Weight at Last Watering</td>
    </tr>
    <?php
      $query = "SELECT * FROM plant_events WHERE code=2";
      $events = @mysqli_query($dbc,$query);
      $plants = @mysqli_query($dbc,"SELECT * FROM plants");

      if($events && $plants)
      {
	$display = array();
        $temp = array();

	while($row = mysqli_fetch_array($plants))
	{
		// Create display array from the plants table with empty values
		$display [$row["id"]] = array(
			"nickname"=>$row["nickname"],
			"waterdate"=>"",
			"waterweight"=>"",
			"curweight"=>""
			);
		// Create temporary variables for each plant to store yesterday's date and yesterday's weight
		$temp [$row["id"]] = array(
			"yesterweight"=>0,
			"yesterdate"=>""
			);
	}
	// Traverse the events array
	// This next bit is practically unreadable, needs refactoring
	while($row = mysqli_fetch_array($events))
	{
          // Determine which plant it pertains to
          // If there's a value for yesterday's date, and yesterday's weight
	  if($temp[$row["plant"]]["yesterweight"]!="")
	  {
	    // Compare today's weight to yesterday's and store the date and weight in the watering event if today's is greater than yesterday's
	    if($temp[$row["plant"]]["yesterweight"] < $row["val"])
	    {
	      // Store today's weight in display array
	      $display[$row["plant"]]["waterdate"] = $temp[$row["plant"]]["yesterdate"];
	      $display[$row["plant"]]["waterweight"] = $temp[$row["plant"]]["yesterweight"];
	    }
	  }
	  $display[$row["plant"]]["curweight"] = $row["val"];
          // Store today's weight and date in yesterday's
	  $temp[$row["plant"]]["yesterweight"] = $row["val"];
	  $temp[$row["plant"]]["yesterdate"] = $row["datetime"];
        }

	foreach($display as $plantrow)
        {
          echo '<tr>';
          echo '  <td>'.$plantrow["nickname"].'</td>';
          echo '  <td>'.$plantrow["curweight"].'</td>';
          echo '  <td>'.$plantrow["waterdate"].'</td>';
          echo '  <td>'.$plantrow["waterweight"].'</td>';
	  echo '</tr>';
        }
    }
    ?>
  </table>
</body>
</html>
