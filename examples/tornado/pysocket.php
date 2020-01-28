<!doctype html>
<html>
	<head>
		<title>WebSockets con Python e Tornado</title>
		<meta charset="utf-8" />
		<style type="text/css">
			body {
				text-align:center;
				width:100%;
				font-family: Arial, Helvetica, sans-serif;
				}
		
			.button {
				background-color: #4CAF50; /* Green */
				border:none;
				color:white;
				padding:15px 20px;
				margin:8px 0;
				text-align:center;
				text-decoration:none;
				display:inline-block;
				width:25%;
				border-radius:4px;
				font-size:16px;
			}
			
			.button:hover {
				background-color: #00E600; /* Green */
			}
			
			.button.block{
				position:relative;
				display:block;
				left:37%;
				width:25%;
			}
			
			input[type=text], select {
				display:inline-block;
				width:25%;
				padding-top:12px;
				padding-bottom:12px;
				padding-left:15px;
				padding-right:15px;
				margin-top:8px;
				margin-bottom:0px;
				margin-left:0px;
				margin-right:8px;
				border:1px solid #ccc;
				border-radius:4px;
				box-sizing:border-box;
				font-size:16px;
			}
			
			.logwindow{
				overflow:scroll;
				width:50%;
				height:200px;
				background-color:#ffeeaa;
				margin:auto;
				text-align:left;
				padding:5px;
			}
			
			.statusmsg{
				width:100%;
				height:15px;
				margin:auto;
				text-align:center;
			}
		</style>
		
		<script src="jquery.min.js"></script>
		
		<script>
		  $(document).ready(function()
			  {
				var ws;

				// ---------------------------------------------------------------------------------
				// Istanzia il websocket
				// ---------------------------------------------------------------------------------
				ws = new WebSocket("ws://"+window.location.hostname+":8888/ws");
				
				// ---------------------------------------------------------------------------------
				// Apre il websocket
				// ---------------------------------------------------------------------------------
				ws.onopen = function(evt) { $("#log").text("Opening socket..."); };
				
				// ---------------------------------------------------------------------------------
				// Gestione chiusura websocket
				// ---------------------------------------------------------------------------------
				ws.onclose = function(evt)
				{ 
				  $("#log").text("Connection was closed..."); 
				  $("#btn_sendmsg #msg").prop('disabled', true);
				};
				
				// ---------------------------------------------------------------------------------
				// Gestione finestra di Log sulla pagina web
				// ---------------------------------------------------------------------------------
				var logger = function(msg)
				{
				  var now = new Date();
				  var sec = now.getSeconds();
				  var min = now.getMinutes();
				  var hr = now.getHours();
				  var logcontents = $("#log").html() + "<br/>" + hr + ":" + min + ":" + sec + " ___ " +  msg;
				  $("#log").html(logcontents);
				  $('#log').scrollTop($('#log')[0].scrollHeight);
				}

				// ---------------------------------------------------------------------------------
				// Funzione trasmissione messaggi nella casella di testo
				// dalla pagina web a RPi
				// ---------------------------------------------------------------------------------
				var sender = function()
				{
				  var msg = $("#msg").val();
				  if (msg.length > 0)
					ws.send(msg);
				  $("#msg").val(msg);
				}
				
				// ---------------------------------------------------------------------------------
				// Gestione messaggi in arrivo sul websocket
				// da RPi a pagina web
				// ---------------------------------------------------------------------------------
				ws.onmessage = function(evt)
				{
				  logger(evt.data);
				};
				
				// ---------------------------------------------------------------------------------
				// Gestione trasmissione messaggio da pagina web a RPi
				// premendo solo il tasto Enter quando il focus e' sulla casella di testo
				// ---------------------------------------------------------------------------------
				$("#msg").keypress(
					function(event)
					{
						if (event.which == 13)
						{
							sender();
						}
					}
				);

				// ---------------------------------------------------------------------------------
				// Gestione trasmissione messaggio da pagina web a RaspberryPi
				// attraverso il pulsante di invio
				// ---------------------------------------------------------------------------------
				$("#btn_sendmsg").click(
					function()
					{
						sender();
					}
				);
				
				// ---------------------------------------------------------------------------------
				// Pulsante accensione led id="btn_ledon"
				// ---------------------------------------------------------------------------------
				$("#btn_ledon").on("click",
					function (event)
					{
						if (event.type === "click")
						{
							ws.send("LEDON");
						}
					});
				
				// ---------------------------------------------------------------------------------
				// Pulsante spegnimento led id="btn_ledoff"
				// ---------------------------------------------------------------------------------
				$("#btn_ledoff").on("click",
					function (event)
					{
						if (event.type === "click")
						{
							ws.send("LEDOFF");
						}
					});
			  });
		</script>
		
	</head>
	<body>
		<h1>WebSockets con Python e Tornado</h1>
		<div id="log" class="logwindow">Messages go here</div>

		<div>
		  <input type="text" id="msg"/>
		  <input type="button" class="button" id="btn_sendmsg" value="Invia messaggio" />
		  <input type="button" class="button block" id="btn_ledon" value="LED ON" />
		  <input type="button" class="button block" id="btn_ledoff" value="LED OFF" />
		</div>

		<div id="status" class="statusmsg">Esempio comunicazione con websocket-php-javascript-python</div>
	</body>
</html>
