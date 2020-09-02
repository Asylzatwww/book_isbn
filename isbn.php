<!doctype html>
<html lang="fr">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="shortcut icon" type="image/x-icon" href="images/favicon.ico">
<link rel="icon" type="image/png" href="images/favicon.png">
<link href='http://fonts.googleapis.com/css?family=Permanent+Marker' rel='stylesheet' type='text/css'>

	<link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.0/themes/smoothness/jquery-ui.css" />
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.11.0/jquery-ui.min.js"></script>	
		<title>Ajouter un livre</title>
	<link type="text/css" href="styles.css" rel="stylesheet">

	<script>

        $( document ).ready(function() {
            alert( $(".response").html() );

            $("#button").click(function(){
                alert("run");
                $.ajax({url: "http://asylzat.com/cgi-bin/index.py?findValue=9176371212", success: function(result){
                        $(".response").html(result);
                        var obj = JSON.parse(result);
                        console.log( obj.description );
                    }});


            });
        });


    </script>
</head>
<body>

<div class="response">hello</div>

<input type="text" />
<input type="button" id="button" value="submit" />

</body>
</html>

