#!/usr/bin/env python

import cgi, os, Cookie, datetime, string, csv
import cgitb; 
cgitb.enable()  # for debugging

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
		<p class="gold">You have <span style="color:yellow">
'''
middleBody = '''
</span> gold</p>
'''

pointsBody = '''<form name="game" action="transfer.py" method="post">
			<input type="hidden" name="points" value="'''
Inventory1Body ='''">
			<input type="hidden" name="Inventory1" value="
'''
Inventory2Body ='''">
			<input type="hidden" name="Inventory2" value="'''
Inventory3Body ='''">
			<input type="hidden" name="Inventory3" value="'''
Inventory4Body ='''">
			<input type="hidden" name="Inventory4" value="'''
Inventory5Body ='''">
			<input type="hidden" name="Inventory5" value="'''
botBody ='''">
			<input id="lower" type="submit" name="submitroom" value="Return to room">
		</form>
		<span><a id="logout" href="game.py?logout=logout">Logout to restart WARNING All items in your Inventory will be lost</a></span>
	</body>
</html>
'''

metaRefresh = '<meta http-equiv="refresh" content="1;url=game.py">'
metaRefreshLoginPage = '<meta http-equiv="refresh" content="2;url=http://cs.mcgill.ca/~cliu62/ass5">'

def gameMode():

	points = 100

	# GET and POST requests
	form = cgi.FieldStorage()

	# Check if cookie exists if not, initialize cookie
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		# Retrieve cookie info
		clickCount = int(cookie['clickCount'].value)
		userTable = decodeList(cookie['userTable'].value)
		points = int(cookie['points'].value)
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

	# Fetch points from POST and update cookie
	if (form.getvalue('points')):
		points = form.getvalue('points')
		try:
			points = int(points)
		except TypeError:
			error_pop("id should be number")
		cookie['points'] = points
		print cookie

	# Fetch Inventory1 and insert in cookie
	if (form.getvalue('Inventory1')):
		cookie['inventory1'] = form.getvalue('Inventory1')
		print cookie

	# Fetch Inventory2 and insert in cookie
	if (form.getvalue('Inventory2')):
		cookie['inventory2'] = form.getvalue('Inventory2')
		print cookie

	# Fetch Inventory3 and insert in cookie
	if (form.getvalue('Inventory3')):
		cookie['inventory3'] = form.getvalue('Inventory3')
		print cookie

	# Fetch Inventory4 and insert in cookie
	if (form.getvalue('Inventory4')):
		cookie['inventory4'] = form.getvalue('Inventory4')
		print cookie

	# Fetch Inventory5 and insert in cookie
	if (form.getvalue('Inventory5')):
		cookie['inventory5'] = form.getvalue('Inventory5')
		print cookie

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
							points+=5
						#If cards don't match
						else:
							userTable[x]=0
							userTable[y]=0
							cookie['userTable'] = userTable
							points-=2
		cookie['clickCount'] = 0
		cookie['points'] = points
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
	print points
	print middleBody

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
	print pointsBody
	print points

	print Inventory1Body
	try:
		inventory = cookie['inventory1'].value
		print inventory
	except (KeyError):
		pass
	print Inventory2Body
	try:
		inventory = cookie['inventory2'].value
		print inventory
	except (KeyError):
		pass
	print Inventory3Body
	try:
		inventory = cookie['inventory3'].value
		print inventory
	except (KeyError):
		pass
	print Inventory4Body
	try:
		inventory = cookie['inventory4'].value
		print inventory
	except (KeyError):
		pass
	print Inventory5Body
	try:
		inventory = cookie['inventory5'].value
		print inventory
	except (KeyError):
		pass

	print botBody

''' MAIN '''
if os.environ['REQUEST_METHOD'] == 'GET':
	arguments = cgi.FieldStorage()
	for i in arguments.keys():
			if (i=='logout'):
				logout()
				print 'Content-type: text/html\r\n\r'
				print '''
					<head>
						<title>Log out</title>
					</head>
					<body>
						<p>Logging out</p>
					</body>
					'''
				print metaRefreshLoginPage
	else:
		gameMode()
else:
	gameMode()


