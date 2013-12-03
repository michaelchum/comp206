#!/usr/bin/env python

import cgi, os, Cookie, datetime, string, csv
import cgitb; 
cgitb.enable()  # for debugging

''' ROOM MODE CODE '''

roomIndex = '''
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="/room.css"/>
		<title> Portal room </title>
	</head>

	<body bgcolor="black" text=#c9efff align="center">
		<div id="title">
			<span style="font-size:80px">Welcome to the</span><br>
			<span style="color:white">P</span>
			<span style="color:blue">O</span>
			<span style="color:red">R</span>
			<span style="color:yellow">T</span>
			<span style="color:turquoise">A</span>
			<span style="color:green">L</span> 
			<br>
			<span>room</span>
			<span><p class="gold">You have <span style="color:yellow">
'''
roomIndex2 = '''</span> gold</p></span>

		</div>

		<div id="banner">
			<a id="banner">
				<img src="/img/tron.jpg" border="0">
			</a>
		</div>

	<table>
		<tr>
			<td></td>
			<td>
				<center>
					<form name="goNorth" action="http://cs.mcgill.ca/~dkim63/roomPage.html" method="post">
'''
roomIndex3 = '''
						<input type="image" img id="door" src="/img/north.jpg">
						<br>
						<span>NORTH</span>
					</form>
				</center>
			</td>
			<td></td>
		<tr>
			<td>
				<center>
					<form name="goWest" action="http://cs.mcgill.ca/~mwu33/room.html" method="post">
'''
roomIndex4 = '''
						<input type="image" img id="door" src="/img/west.png">
						<br>
						<span>WEST</span>
					</form>
				</center>
			</td>
			<td>
				<center>
					<form name="game" action="game.py" method="POST">
						<input id="door" name="submit" type="image" src="/img/riddle.jpg" value="myValue" alt="" />
'''
roomIndex5 = '''
						<br>
						<input type="submit" name="submitgame" value="Challenge me" id="puzzle">
					</form>
					
				</center>
			</td>
			<td>
				<center>
					<form name="goEast" action="http://www.cs.mcgill.ca/~lwong27/room.html" method="post">
'''
roomIndex6 = '''
						<input type="image" img id="door" src="/img/east.jpg">
						<br>
						<span>EAST</span>
					</form>
				</center>
			</td>
		</tr>

		<tr>
			<td></td>
			<td>
				<center>
					<form name="goSouth" action="http://cs.mcgill.ca/~dbiggs3/room.html" method="post">
'''
roomIndex7 = '''
						<input type="image" img id="door" src="/img/south.jpg">
						<br>
						<span>SOUTH</span>
					</form>
				</center>
			</td>
			<td></td>
		</tr>
		<br>
			<form name="game" action="game.py" method="POST">
				<span class="command">Command:</span><br>
				<input type="text" name="command">
				<input type="submit" name="submit"><br>
'''
roomIndex8 = '''
			</form>

		<br>
			<span style="position:relative; left:320px; top:85px"><span id="lookaround">Look around</span></span>
'''

botBody = '''
	</body>
</html>
'''

def roomMode():
	points = "100"
	invent1 = ""
	invent2 = ""
	invent3 = ""
	invent4 = ""
	invent5 = ""
	# Check GET/POST request for room and game
	if (cgi.FieldStorage):
		form = cgi.FieldStorage()
	if (form.getvalue('points')):
		points = form.getvalue('points')

	print 'Content-type: text/html\r\n\r'
	print roomIndex
	print points
	print roomIndex2
	print '<input type="hidden" name="points" value="' + points + '">'
	print '<input type="hidden" name="Inventory1" value="'+ invent1 + '">'
	print '<input type="hidden" name="Inventory2" value="'+ invent2 + '">'
	print '<input type="hidden" name="Inventory3" value="'+ invent3 + '">'
	print '<input type="hidden" name="Inventory4" value="'+ invent4 + '">'
	print '<input type="hidden" name="Inventory5" value="'+ invent5 + '">'
	print roomIndex3
	print '<input type="hidden" name="points" value="' + points + '">'
	print '<input type="hidden" name="Inventory1" value="'+ invent1 + '">'
	print '<input type="hidden" name="Inventory2" value="'+ invent2 + '">'
	print '<input type="hidden" name="Inventory3" value="'+ invent3 + '">'
	print '<input type="hidden" name="Inventory4" value="'+ invent4 + '">'
	print '<input type="hidden" name="Inventory5" value="'+ invent5 + '">'
	print roomIndex4
	print '<input type="hidden" name="points" value="' + points + '">'
	print '<input type="hidden" name="Inventory1" value="'+ invent1 + '">'
	print '<input type="hidden" name="Inventory2" value="'+ invent2 + '">'
	print '<input type="hidden" name="Inventory3" value="'+ invent3 + '">'
	print '<input type="hidden" name="Inventory4" value="'+ invent4 + '">'
	print '<input type="hidden" name="Inventory5" value="'+ invent5 + '">'
	print roomIndex5
	print '<input type="hidden" name="points" value="' + points + '">'
	print '<input type="hidden" name="Inventory1" value="'+ invent1 + '">'
	print '<input type="hidden" name="Inventory2" value="'+ invent2 + '">'
	print '<input type="hidden" name="Inventory3" value="'+ invent3 + '">'
	print '<input type="hidden" name="Inventory4" value="'+ invent4 + '">'
	print '<input type="hidden" name="Inventory5" value="'+ invent5 + '">'
	print roomIndex6
	print '<input type="hidden" name="points" value="' + points + '">'
	print '<input type="hidden" name="Inventory1" value="'+ invent1 + '">'
	print '<input type="hidden" name="Inventory2" value="'+ invent2 + '">'
	print '<input type="hidden" name="Inventory3" value="'+ invent3 + '">'
	print '<input type="hidden" name="Inventory4" value="'+ invent4 + '">'
	print '<input type="hidden" name="Inventory5" value="'+ invent5 + '">'
	print roomIndex7
	print '<input type="hidden" name="points" value="' + points + '">'
	print '<input type="hidden" name="Inventory1" value="'+ invent1 + '">'
	print '<input type="hidden" name="Inventory2" value="'+ invent2 + '">'
	print '<input type="hidden" name="Inventory3" value="'+ invent3 + '">'
	print '<input type="hidden" name="Inventory4" value="'+ invent4 + '">'
	print '<input type="hidden" name="Inventory5" value="'+ invent5 + '">'
	print roomIndex8

	print botBody

def lookMode():
	print 'Content-type: text/html\r\n\r'
	print '<HTML><body>mold system/options/cgi</body></HTML>'
	'''
	file = open('/inventory.csv','r')
	ReadData=csv.readerline(file)
	print roomIndex
	print '<p>'
	for line in ReadData
		print line
	print '</p>'
	print botGame
	'''
''' END OF ROOM MODE CODE '''


roomMode()