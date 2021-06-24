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
  }
  else
  {
    $f_val = $_POST['val'];
    echo $f_val;
  }

  if(empty($_POST['sid']))
  {
    // Exit error
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
  }
  else
  {
    $f_eid = $_POST['eid'];
    echo $f_eid;
  }
  // Get plants subscribed to that sensor
    // Add sensor values for each plant
