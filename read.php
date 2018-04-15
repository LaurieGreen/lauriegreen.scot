<?php

require 'database.php';

$conn = Connect();

$gifs = array();

$query = "SELECT number, url FROM gifs";

$result = $conn->query($query);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
    	array_push($gifs, $row["url"]);
    }
    //echo $gifs[rand(0, $gifs.count())];
    //echo $gifs[rand(0, count($gifs)-1)];
    shuffle($gifs);
    echo json_encode($gifs);
} else {
    echo "0 results";
}
$conn->close();

?>