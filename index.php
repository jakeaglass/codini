<html>
	<head>
		<title>Codini &endash; Mobile Code Assistant with a Touch of Magic</title>
		
		<!--import some js libraries and css here-->
		<link rel="stylesheet" href="css/bootstrap.min.css">
		<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>

		<script>
			function connectToWebsocketServer(ipAddress){
				var connection = new WebSocket('ws://'+ipAddress+':8080');
				console.log("server started");
				connection.onmessage = function(e){
				   var server_message = e.data;
				   $("#message").html(server_message);
				   console.log(server_message);
				}
				connection.onerror = function(e){
					var error_message = e.data;
					console.log(error_message);
				}
			}
			var ipEntered=0;
			$("document").ready(function(){
				//let's query the local storage for a saved IP
				var previouslySavedIp=localStorage.getItem("hostIp");
				if(!previouslySavedIp){
					$('#ipSelectModal').modal('show');
				}
				else{
					connectToWebsocketServer(previouslySavedIp);
				}

				//event handler for modal dismiss and ip save function
				$("#saveIp").click(function(){
					ipEntered=1;
					if(typeof(Storage) !== "undefined") { //if the browser supports local data storage
						localStorage.setItem("hostIp", $("#ipAddressInput").val());
						console.log("ip in local storage");
					}
					console.log("ip saved");
					connectToWebsocketServer($("#ipAddressInput").val());
				}); //end saveIP event handler for button press after modal dismiss



			}); //end onLoad function
			
			

		</script>
	</head>
	<body>
	<!--MODAL SETUP-->

	<!-- ipSelectModal-->
	<div class="modal fade" id="ipSelectModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	  <div class="modal-dialog">
	    <div class="modal-content">
	      <div class="modal-header">
	        <h4 class="modal-title" id="myModalLabel">Please enter the IP address of your host programming machine</h4>
	      </div>
	      <div class="modal-body">
	        <input type="text" id="ipAddressInput" placeholder="192.168.1.1 or similar" />
	      </div>
	      <div class="modal-footer">
	        <button type="button" id="saveIp" class="btn btn-default" data-dismiss="modal">Save Host</button>
	      </div>
	    </div>
	  </div>
	</div>

		<nav class="navbar navbar-default" role="navigation">
		  <div class="container-fluid">
		    <!-- Brand and toggle get grouped for better mobile display -->
		    <div class="navbar-header">
		      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
		        <span class="sr-only">Toggle navigation</span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		        <span class="icon-bar"></span>
		      </button>
		      <a class="navbar-brand" href="#">Codini</a>
		    </div>

		    <!-- Collect the nav links, forms, and other content for toggling -->
		    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
		      <ul class="nav navbar-nav">
		        <li class="active"><a href="#">Link</a></li>
		        <li><a href="#">Link</a></li>
		        <li class="dropdown">
		          <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <span class="caret"></span></a>
		          <ul class="dropdown-menu" role="menu">
		            <li><a href="#">Action</a></li>
		            <li><a href="#">Another action</a></li>
		            <li><a href="#">Something else here</a></li>
		            <li class="divider"></li>
		            <li><a href="#">Separated link</a></li>
		            <li class="divider"></li>
		            <li><a href="#">One more separated link</a></li>
		          </ul>
		        </li>
		      </ul>
		      <form class="navbar-form navbar-left" role="search">
		        <div class="form-group">
		          <input type="text" class="form-control" placeholder="Search">
		        </div>
		        <button type="submit" class="btn btn-default">Submit</button>
		      </form>
		      <ul class="nav navbar-nav navbar-right">
		        <li><a href="#">Link</a></li>
		        <li class="dropdown">
		          <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <span class="caret"></span></a>
		          <ul class="dropdown-menu" role="menu">
		            <li><a href="#">Action</a></li>
		            <li><a href="#">Another action</a></li>
		            <li><a href="#">Something else here</a></li>
		            <li class="divider"></li>
		            <li><a href="#">Separated link</a></li>
		          </ul>
		        </li>
		      </ul>
		    </div><!-- /.navbar-collapse -->
		  </div><!-- /.container-fluid -->
		</nav>

		<!--start page content-->

		<p>Message:</p><div id="message">No Message Received</div>
		<footer style="class="footer">&copy; 2014 Jake Glass, Mihir Trivedi, and Kevin Vincent</div>