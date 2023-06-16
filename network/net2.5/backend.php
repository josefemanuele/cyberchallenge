<html>
<head>
 <title>Dynamic WEB yoga</title>
 <script src="r.js"></script> 
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>

<script>
 function c(p) {
   v = parseInt(document.getElementById("n").value);
   $.ajax({
        'url' : '/backend.php',
        'type' : 'GET',
        'data' : {
            'p' : v
        },
        'success' : function(data) {              
            //alert('Data: '+ r(data, 13));
            document.getElementById("img").src = r(data, 13);
            document.getElementById("n").value = v+1;
        },
    });

 }
</script>

<body>
<h1>Dynamic WEB Yoga</h1>
<table>
<tr>
<td>
<img id="img" src="" />
</td>
</tr>

<tr>
<td>
 <input type=button name=next value=next onclick=c()>
 <input type=hidden name=n id=n value=1>
</td>
</tr>
</body>
<table>

</html>
