<!DOCTYPE html>
<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" type="text/css" href="styles.css">

<title>Laurie's Page</title>
</head>
<body>

<div>
    <img id="gifholder" src="http://i.imgur.com/pg5qRqS.gif"></br>
    <button id="read">New Gif</button>
</div>

<script>
	var gifArray;
	var count = 0;
    $("#read").click(function(){
    	if (count < gifArray.length - 1)
    	{
    		$('#gifholder').attr("src", gifArray[count]);
    	}
    	else 
    	{
    		count = 0;
    	}
    	count++;
    	//console.log("Count: "+count);
    });
    $(document).ready(function(){
        $.get("read.php", function(data, status){   
        // do stuff with data        
            //$('#gifholder').attr("src", data);
            gifArray = JSON.parse(data);
            //console.log("Array Contents: "+data);
            //console.log("Array Length: "+gifArray.length);
        });
	});
</script>

</body>
</html>