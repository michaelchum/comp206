#!/usr/bin/env python

import cgi, os, Cookie, datetime, string, csv
import cgitb;
cgitb.enable()  # for debugging
CURRENT_PATH = os.getcwd() # For path
PROJECT_PATH = os.path.abspath(os.path.join(CURRENT_PATH, os.pardir))
INVENTORY_PATH = os.path.join(PROJECT_PATH, 'inventory.csv')
TEMP_PATH = os.path.join(PROJECT_PATH, 'temp.csv')

''' ROOM MODE CODE '''

roomIndex = '''
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="../room.css"/>
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
				<img src="../img/tron.jpg" border="0">
			</a>
		</div>

	<table>
		<tr>
			<td></td>
			<td>
				<center>
					<form name="goNorth" action="http://cs.mcgill.ca/~zsu3/ass5/transfer.py" method="post">
'''
roomIndex3 = '''
						<input type="image" img id="door" src="../img/north.jpg">
						<br>
						<span>NORTH</span>
					</form>
				</center>
			</td>
			<td></td>
		<tr>
			<td>
				<center>
					<form name="goWest" action="http://cs.mcgill.ca/~dbiggs3/cgi-bin/transfer.py" method="post">
'''
roomIndex4 = '''
						<input type="image" img id="door" src="../img/west.png">
						<br>
						<span>WEST</span>
					</form>
				</center>
			</td>
			<td>
				<center>
					<form name="game" action="game.py" method="POST">
						<input id="door" name="submit" type="image" src="../img/riddle.jpg" value="myValue" alt="" />
'''
roomIndex5 = '''
						<br>
						<input type="submit" name="submitgame" value="Challenge me" id="puzzle">
					</form>
					
				</center>
			</td>
			<td>
				<center>
					<form name="goEast" action="http://www.cs.mcgill.ca/~mwu33/cgi-bin/transfer.py" method="post">
'''
roomIndex6 = '''
						<input type="image" img id="door" src="../img/east.jpg">
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
					<form name="goSouth" action="http://cs.mcgill.ca/~yxia19/ass5/cgi-bin/transfer.py" method="post">
'''
roomIndex7 = '''
						<input type="image" img id="door" src="../img/south.jpg">
						<br>
						<span>SOUTH</span>
					</form>
				</center>
			</td>
			<td></td>
		</tr>
		<br>
			<form name="game" action="transfer.py" method="POST">
				<span class="command">Command:</span><br>
				<input type="text" name="command">
				<input type="submit" name="submit"><br>
'''
roomIndex8 = '''
		<br>
			<span style="position:relative; left:320px; top:85px"><span id="lookaround">Look around</span></span>
'''

botBody = '''
	</body>
</html>
'''

def roomMode():

	# Initialize transmission variables
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
	if (form.getvalue('Inventory1')):
		invent1 = form.getvalue('Inventory1')
	if (form.getvalue('Inventory2')):
		invent2 = form.getvalue('Inventory2')
	if (form.getvalue('Inventory3')):
		invent3 = form.getvalue('Inventory3')
	if (form.getvalue('Inventory4')):
		invent4 = form.getvalue('Inventory4')
	if (form.getvalue('Inventory5')):
		invent5 = form.getvalue('Inventory5')

	item = ""
	# DROP N command
	if (form.getvalue('command')):
		command = str(form.getvalue('command'))
		if "drop" in command:
			drop, number = command.split(" ", 1)
			number = int(number)
			if(number==1):
				item = invent1
				invent1 = ""
			elif(number==2):
				item = invent2
				invent2 = ""
			elif(number==3):
				item = invent3
				invent3 = ""
			elif(number==4):
				item = invent4
				invent4 = ""
			elif(number==5):
				item = invent5
				invent5 = ""
		if (item!=""):
			output = open(INVENTORY_PATH,'a')
			output.write(item)
			output.write('\n')
			output.close()

	# PICKUP N command
	if (form.getvalue('command')):
		command = str(form.getvalue('command'))
		if "pickup" in command:
			pickup, number = command.split(" ", 1)
			number = int(number)
			# Check if a slot is empty
			if (invent1 == "" or invent2 == "" or invent3 == "" or invent4 == "" or invent5 == ""):
				input = open(INVENTORY_PATH,'r')
				output = open(TEMP_PATH,'w+')
				s = input.readlines()
				index = 1
				for line in s:
					singleLine = line.rstrip()
					if (index!=number):
						output.write(singleLine)
						output.write('\n')
					elif (index==number):
						item = singleLine
					index+=1
				input.close()
				output.close()
				os.remove(INVENTORY_PATH)
				os.rename(TEMP_PATH,INVENTORY_PATH)
				if (invent1 == ""):
					invent1 = item
				elif (invent2 == ""):
					invent2 = item
				elif (invent3 == ""):
					invent3 = item
				elif (invent4 == ""):
					invent4 = item
				elif (invent5 == ""):
					invent5 = item

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
	print '<input type="hidden" name="Inventory5" value="'+ invent5 + '">'+'</form>'
	print '<span class="command">'

	# PICKUP N command
	if (form.getvalue('command')):
		if "pickup" in command:
			pickup, number = command.split(" ", 1)
			number = int(number)
			# Check if item exists in datase
			if (item==""):
				print 'Your inventory is full or no such item in database'
			else:
				print "%s %s" % (item, 'has been added to your inventory')

	# INVENTORY command
	if (form.getvalue('command')):
		if (form.getvalue('command')=='inventory'):
			if (invent1=="" and invent2=="" and invent3=="" and invent4=="" and invent5==""):
				print 'You have no items in your inventory'
			if (invent1!=""):
				print "%s %s" % ("1.", invent1)
				print '<br>'
			elif (invent1==""):
				print "%s %s" % ("1.", "empty")
				print '<br>'
			if (invent2!=""):
				print "%s %s" % ("2.", invent2)
				print '<br>'
			elif (invent2==""):
				print "%s %s" % ("2.", "empty")
				print '<br>'
			if (invent3!=""):
				print "%s %s" % ("3.", invent3)
				print '<br>'
			elif (invent3==""):
				print "%s %s" % ("3.", "empty")
				print '<br>'
			if (invent4!=""):
				print "%s %s" % ("4.", invent4)
				print '<br>'
			elif (invent4==""):
				print "%s %s" % ("4.", "empty")
				print '<br>'
			if (invent5!=""):
				print "%s %s" % ("5.", invent5)
			elif (invent5==""):
				print "%s %s" % ("5.", "empty")
				print '<br>'

	# LOOK command
	if (form.getvalue('command')):
		if (form.getvalue('command')=='look'):
			try:
				input = open(INVENTORY_PATH)
				s = input.readlines()
				index = 1
				for line in s:
					singleLine = line.rstrip()
					print "%d%c %s" % (index, '.', singleLine)
					print '<br>'
					index+=1
				input.close()
			except IOError, (errno, strerror):
				print 'No items in the database'

	# DROP N command
	if (form.getvalue('command')):
		command = str(form.getvalue('command'))
		if "drop" in command:
			if (item!=""):
				print "%s %s" % ('You dropped', item)
			elif (item==""):
				print "You have no item at this slot, nothing will be dropped"		

	print '</span>'
	print roomIndex8

	print botBody

# Erase inventory cookies coming from game room
def eraseInventoryCookie():
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		cookie['inventory1']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
		cookie['inventory2']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
		cookie['inventory3']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
		cookie['inventory4']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
		cookie['inventory5']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
		print cookie # IMPORTANT SAVE cookie to expire immediately
	except (Cookie.CookieError, KeyError):
		return

''' END OF ROOM MODE CODE '''

eraseInventoryCookie()
roomMode()