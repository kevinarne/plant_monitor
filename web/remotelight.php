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
      //exit();
  }
  else
  {
    $f_val = $_POST['val'];
    echo $f_val;
  }

  if(empty($_POST['sid']))
  {
    // Exit error
    //exit();
  }
  else
  {
    $f_sid = $_POST['sid'];
    echo $f_sid;
  }

  if(empty($_POST['dt']))
  {
    //$f_dt = now;
  }
  else
  {
    $f_dt = $_POST['dt'];
    echo $f_dt;
  }

  if(empty($_POST['eid']))
  {
    //exit
    //exit();
  }
  else
  {
    $f_eid = $_POST['eid'];
    echo $f_eid;
  }
  $f_sid = 1;
  require_once('../mysqli_connect.php');
  // Get plants subscribed to that sensor
  $sensorquery = "SELECT subscribed FROM sensors WHERE id=".$f_sid;
  $sensorresponse = @mysqli_query($dbc, $sensorquery);
  $subscribed = mysqli_fetch_array($sensorresponse);
  $subarr = explode(",", $subscribed[0]);
  foreach($subarr as $plant)
  {
    $query = "INSERT INTO plant_events (code, datetime, val, plant, notes) VALUES (?,?,?,?,?)";
    $code = 1;
    $stmt = mysqli_prepare($dbc, $query);
    $datetimetext = "datetime text";
    $thisplant = $plant[0];
    $notes = "test";
    $val = 2;

    mysqli_stmt_bind_param(
      $stmt,
      "isiis",
      $code,
      $datetimetext,
      $val,
      intval($thisplant),
      $notes
      );
    mysqli_stmt_execute($stmt);
  }
    // Add sensor values for each plant
