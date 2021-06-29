<?php
  echo "Loading...";
  // Get the data from post (* required)
    // * light val
    // * sensor number
    // time (now() if not provided)
    // * event code
  // Check that all data was provided
  // Return negative response if something was left out
  if(empty($_POST['val']))
  {
      // Exit error
      $f_val = 0;
  }
  else
  {
    $f_val = $_POST['val'];
    echo $f_val;
  }

  if(empty($_POST['sid']))
  {
    exit();
    $f_sid = 0;
  }
  else
  {
    $f_sid = $_POST['sid'];
    echo $f_sid;
  }

  if(empty($_POST['dt']))
  {
    $f_dt = date('Y-m-dTH:i:s');
  }
  else
  {
    $f_dt = $_POST['dt'];
    echo $f_dt;
  }

  if(empty($_POST['eid']))
  {
    //exit
    $f_eid = 0;
  }
  else
  {
    $f_eid = $_POST['eid'];
    echo $f_eid;
  }

  require_once('../mysqli_connect.php');
  // Get plants subscribed to that sensor
  $sensorquery = "SELECT subscribed FROM sensors WHERE id=".$f_sid;
  $sensorresponse = @mysqli_query($dbc, $sensorquery);
  $subscribed = mysqli_fetch_array($sensorresponse);
  $subarr = explode(",", $subscribed[0]);

  foreach($subarr as $plant)
  {
    $query = "INSERT INTO plant_events (code, datetime, val, plant, notes) VALUES (?, ?, ?, ?, ?)";
    $stmt = mysqli_prepare($dbc, $query);
    $notes = "";

    mysqli_stmt_bind_param(
      $stmt,
      "isiis",
      intval($f_eid),
      $f_dt,
      intval($f_val),
      intval($plant),
      $notes
      );
    mysqli_stmt_execute($stmt);
  }
