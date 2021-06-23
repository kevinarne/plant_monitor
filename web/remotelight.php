<?php
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
  }

  if(empty($_POST['sid']))
  {
    // Exit error
  }
  else
  {
    $f_sid = $_POST['sid'];
  }

  if(empty($_POST['dt']))
  {
    //$f_dt = now;
  }
  else
  {
    $f_dt = $_POST['dt'];
  }

  if(empty($_POST['eid']))
  {
    //exit
  }
  else
  {
    $f_eid = $_POST['eid'];
  }
  // Get plants subscribed to that sensor
    // Add sensor values for each plant
