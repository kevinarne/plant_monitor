<html>
	<head>
		<title>Weight Added</title>
	</head>
	<body>
		<?php
			if(isset($_POST['submit']))
			{
				$data_missing = array();
				$f_plant = $_POST['plant'];
				if(empty($_POST['date']))
				{
					$data_missing[] = 'date';
				}
				else
				{
					$f_date = $_POST['date'];
					echo $f_date;
				}

				if(empty($_POST['val']))
				{
					$data_missing[] = 'value';
				}
				else
				{
					$f_val = $_POST['val'];
					echo $f_val;
				}

				if(empty($_POST['notes']))
				{
					$f_notes = "";
					echo $f_val;
				}
				else
				{
					$f_notes = $_POST['notes'];
				}
			}
			echo '<h1>success</h1>';
		?>


	</body>

<?php
	echo '<h1>Nothing here<h1>';
?>
</html>
