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
				}

				if(empty($_POST['val']))
				{
					$data_missing[] = 'value';
				}
				else
				{
					$f_val = $_POST['val'];
				}

				if(empty($_POST['notes']))
				{
					$f_notes = "";
				}
				else
				{
					$f_notes = $_POST['notes'];
				}
			if(empty($data_missing))
			{
				require_once('../mysqli_connect.php');
				//Convert the val to an integer
				$m_val = (int)($f_val*100);
				$query = "INSERT INTO plant_events (code, datetime, val, plant, notes) VALUES (?,?,?,?,?)";
				$datetime = date_create_from_format("Y-m-d",$f_date);
				$s_datetime = $datetime->format(DateTime::ISO8601);
				$code = 2;
				$stmt = mysqli_prepare($dbc,$query);
				mysqli_stmt_bind_param($stmt, "isiis", $code, $s_datetime, $m_val, intval($f_plant), $f_notes);
				mysqli_stmt_execute($stmt);
			}
		}
		?>


	</body>
</html>
