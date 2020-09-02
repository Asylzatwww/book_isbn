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

            $("#button").click(function(){

                var obj;

                $.ajax({url: "http://asylzat.com/cgi-bin/index.py?findValue=9176371212", success: function(result){
                        $(".result").html(result);
                        obj = jQuery.parseJSON( result );

                        var img = "";
                        var imgThumb = "";


                        for (i in obj.imageGalleryData) {
                             img += "<img src=\"" + obj.imageGalleryData[i].mainUrl + "\" />" ;
                            imgThumb += "<img src=\"" + obj.imageGalleryData[i].thumbUrl + "\" />" ;
                        }

                        $(".img").html(img);
                        $(".imgThumb").html(imgThumb);

                        $(".content").show();

                        $("#title").html( obj.title );
                        $("#description").html( obj.description );

                    }});


            });
        });


    </script>
    <style>
        .content {
            display: none;
        }

        .img img {
            width:200px;
        }

        pre {
            display: none;
        }
        
        .imageBlock {
            float: left;
        }
    </style>
</head>
<body>


<pre class="result">

</pre>
<div class="search">Search</div>
<input type="text" />
<input type="button" id="button" value="submit" />

<div class="content">
    <div class="imageBlock">
        <div class="img">

        </div>

        <div class="imgThumb">
        </div>
    </div>
    

    <div class="description">
        <h3 id="title"></h3>
        <div id="description"></div>
    </div>
</div>

</body>
</html>
