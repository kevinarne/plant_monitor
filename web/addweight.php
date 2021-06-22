<html>
<head>
    	<title>Add Weight</title>
	<style>
		p, select, input{font-size:30px;}
		div{
			padding:20;
			margin:30;
			box-shadow: 10px 10px #0000000F;
			border-style:solid;
			border-width:1px;
			margin:0 auto;
			width:75%;
		}
	</style>
</head>

<body>
	<div >
    	<form action="http://10.0.0.123/weightadded.php" method="post">
		<select name="plant" id="plant">
      		<?php
        	require_once('../mysqli_connect.php');
        	# Pull the possible plants to add to the drop down
       		$query = "SELECT id, nickname FROM plants";
        	$response = @mysqli_query($dbc, $query);
        	if($response)
        	{
          		# Plant drop down
          		while($row = mysqli_fetch_array($response))
          		{
              			echo '<option value='.$row["id"].'>'.$row["nickname"].'</option>';
          		}
		}
      		?>
      		</select>
      		<p>Date:  <input type="date" name="date"/></p>
      		<p>Value:  <input type="number" name="val" step="any"/></p>
      		<p>Notes:  <input type="text" name="notes"/></p>
      		<p><input style="width:100%; display:block;" type="submit" name="submit" value="Submit"/></p>
    	</form>
	</div>
</body>
</html>
