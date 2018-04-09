<?php

function Connect()
{
 $dbhost = "localhost";
 $dbuser = "lauriegr_laurie";
 $dbpass = "l0lSpring1890!";
 $dbname = "lauriegr_test";

 // Create connection
 $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname) or die($conn->connect_error);

 return $conn;
}
 
?>