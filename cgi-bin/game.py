#!/usr/bin/env python

import cgi, os, Cookie, datetime, string
import cgitb; 
cgitb.enable()  # for debugging

''' GAME MODE CODE '''

# Initialize game table
initGame = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
solTable = [1,6,3,2,6,5,0,7,2,4,1,0,3,7,4,5]

# Helper function to parse cookie string into int list
def decodeList(string):
	string = string[1:-1]
	string_list = string.split(",")
	string_list = [int(x) for x in string_list]
	return string_list

# Logout function to delete cookie
def logout():
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		cookie['clickCount']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
		cookie['userTable']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
		print cookie # IMPORTANT SAVE cookie to expire immediately
	except (Cookie.CookieError, KeyError):
		return

topBody = '''
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="/game.css"/>
	</head>

	<body>
		<p class="upper">Match the cards to earn gold!</p>
		<p class="gold">You have <span style="color:yellow">100</span> gold</p>
'''

botBody = '''
		<p class="lower">Or... <a href="game.py">Return to room</a><p>
	</body>
</html>
'''

metaRefresh = '<meta http-equiv="refresh" content="2;url=game.py?mode=game">'

def gameMode():
	# Check if cookie exists if not, initialize cookie
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		# Retrieve cookie info
		clickCount = int(cookie['clickCount'].value)
		userTable = decodeList(cookie['userTable'].value)
	except (Cookie.CookieError, KeyError):
		cookie = Cookie.SimpleCookie()
		cookie['clickCount'] = 0
		cookie['userTable'] = initGame
		cookie['clickCount']['expires'] = 1*1*3*60*60 # Expires in 3 hours
		cookie['userTable']['expires'] = 1*1*3*60*60
		print cookie # IMPORTANT SAVE cookie
		# Retrieve cookie info
		clickCount = int(cookie['clickCount'].value)
		userTable = decodeList(cookie['userTable'].value)

	# If second is already card open
	if (clickCount > 1):
		for x in range(16):
			# Find the two opened cards
			if (userTable[x]==1):
				for y in range(x+1, 16):
					if (userTable[y]==1):
						#If cards match
						if (solTable[x]==solTable[y]):
							userTable[x]=9
							userTable[y]=9
							cookie['userTable'] = userTable
						#If cards don't match
						else:
							userTable[x]=0
							userTable[y]=0
							cookie['userTable'] = userTable
		cookie['clickCount'] = 0
		print cookie

	# Check GET request for card ID
	if (form.getvalue('card')):
		card = form.getvalue('card')
		card = int(card)
		userTable[card] = 1
		cookie['userTable'] = userTable
		clickCount += 1
		cookie['clickCount'] = clickCount
		print cookie # IMPORTANT SAVE cookie

	print 'Content-type: text/html\r\n\r'
	print topBody

	print '<table>'
	print '<tr>'
	for x in range(16):
		if (userTable[x]==0):
			print '<td><a href=game.py?mode=game&card=' + str(x) + '><img src="/img/back.png"></a></td>'
		elif (userTable[x]==9):
			print '<td><img src="/img/blank.jpg"></td>'
		elif (userTable[x]==1):
			print '<td><img src="/img/card' + str(solTable[x]) + '.jpg"></td>'
		if (x==3 or x==7 or x==11):
			print '</tr>'
			print '<tr>'
	print '</tr>'
	print '</table>'
	
	if (clickCount>1):
		print metaRefresh
	print botBody

''' END OF GAME MODE CODE '''

''' ROOM MODE CODE '''

roomIndex = '''
<html>

	<head>
		<link rel="stylesheet" type="text/css" href="/room.css"/>
		<title> Portal room </title>
	
	</head>

	<body bgcolor="black" text=#c9efff>
		<center>
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
				</span>
			</div>

			<div id="banner">
					<a id="banner">
						<img src="/img/tron.jpg" border="0">
					</a>
			</div>

			<br></br>

			<div>
				<a href="http://cs.mcgill.ca/~dkim63/roomPage.html">
					<img id="door" src="/img/north.jpg"/>
				</a>
				<br>
				<span>NORTH</span>
			</div>

			<br></br>

			<span id="east">
				<a href="http://www.cs.mcgill.ca/~lwong27/room.html"><img id="door" src="/img/east.jpg"></a>
			</span>


			<form name="game" action="game.py?mode=game" method="post">
			<input id="door" name="submit" type="image" src="/img/riddle.jpg" value="myValue" alt="" />
            <input type="hidden" name="points" value="0">
            <input type="hidden" name="Inventory1" value="">
            <input type="hidden" name="Inventory2" value="">
            <input type="hidden" name="Inventory3" value="">
            <input type="hidden" name="Inventory4" value="">
            <input type="hidden" name="Inventory5" value="">
			</form>

			<span id="west">
				<a href="http://cs.mcgill.ca/~mwu33/room.html"><img id="door" src="/img/west.png"></a>               
			</span>
			<br>

			<span id="west2">
				WEST
			</span>

			<a style="text-decoration:none" href="game.py?mode=game"><span style="font-size:40; text-decoration:none">See the puzzle<span></a>

			<span style="display:inline; position:relative;left:118px; text-align:center overflow:hidden" width="200px" height="200px">
				EAST
			</span>

			<br></br>

			<span style="position:relative; left:320px; top:85px"><span id="lookaround">Look around</span></span>

				<center><a href="http://cs.mcgill.ca/~dbiggs3/room.html"><img id="door" src="/img/south.jpg"/></a></center>
			
			<center><span>SOUTH</span></center>

		<br>
		<form name="game" action="game.py" method="POST">

		<span class="command">Command:</span><br>
		<input type="text" name="command">
		<input type="submit" name="submit"><br>
		<input type="hidden" name="coins" value="100">
		<input type="hidden" name="Inventory1" value="test1">
		<input type="hidden" name="Inventory2" value="test2">
		<input type="hidden" name="Inventory3" value="test3">
		<input type="hidden" name="Inventory4" value="test4">
		<input type="hidden" name="Inventory5" value="test5">
		</form>
		</center>

		<br>

	</body>
</html>
'''

def roomMode():
	print 'Content-type: text/html\r\n\r'
	print roomIndex

''' END OF ROOM MODE CODE '''

# Check GET/POST request for room or game
if (cgi.FieldStorage()):
	form = cgi.FieldStorage()
	# If game mode activated
	if (form.getvalue('mode')):
		mode = form.getvalue('mode')
		if (mode=='game'):
			gameMode()
	# If look mode activated
	else:
		roomMode()
else:
	roomMode()

#print originalTable
#print metaRefresh



