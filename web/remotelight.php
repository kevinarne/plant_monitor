<?php
  echo "Loading...";
  // Get the data from post (* required)
    // * light val
    // * sensor number
    // time (now() if not provided)
    // * event code
  // Check that all data was provided
  // Return negative response if something was left out
  if(empty($_GET['val']))
  {
      // Exit error
      $f_val = 0;
  }
  else
  {
    $f_val = $_GET['val'];
    echo $f_val;
  }

  if(empty($_GET['sid']))
  {
    exit();
    $f_sid = 0;
  }
  else
  {
    $f_sid = $_GET['sid'];
    echo $f_sid;
  }

  if(empty($_GET['dt']))
  {
    $f_dt = date('Y-m-d H:i:s');
  }
  else
  {
    $f_dt = $_GET['dt'];
    echo $f_dt;
  }

  if(empty($_GET['eid']))
  {
    //exit
    $f_eid = 0;
  }
  else
  {
    $f_eid = $_GET['eid'];
    echo $f_eid;
  }

  require_once('../mysqli_connect.php');
  // Get plants subscribed to that sensor
  $sensorquery = "SELECT subscribed FROM sensors WHERE id=".$f_sid;
  $sensorresponse = @mysqli_query($dbc, $sensorquery);
  $subscribed = mysqli_fetch_array($sensorresponse);
  $subarr = explode(",", $subscribed[0]);
  $f_src = "s".strval($f_sid);
  foreach($subarr as $plant)
  {
    $query = "INSERT INTO plant_events (code, datetime, val, plant, notes, source) VALUES (?, ?, ?, ?, ?, ?)";
    $stmt = mysqli_prepare($dbc, $query);
    $notes = "";

    mysqli_stmt_bind_param(
      $stmt,
      "isiiss",
      intval($f_eid),
      $f_dt,
      intval($f_val),
      intval($plant),
      $notes,
      $f_src
      );
    mysqli_stmt_execute($stmt);
  }
