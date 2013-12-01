#!/usr/bin/env python

import cgi, os, Cookie, datetime, string
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

# Check GET/POST request
if (cgi.FieldStorage()):
	form = cgi.FieldStorage()
	# Check GET request for card ID
	if (form.getvalue('card')):
		card = form.getvalue('card')
		card = int(card)
		userTable[card] = 1
		cookie['userTable'] = userTable
		clickCount += 1
		cookie['clickCount'] = clickCount
		print cookie # IMPORTANT SAVE cookie

topBody = '''
<html>
	<head>
		<link rel="stylesheet" type="text/css" href="/game.css"/>
	</head>

	<body>
		<p class="upper">Match the cards to earn gold!</p>
'''

botBody = '''
		<p class="lower">Or... <a href="/game.css">Return to room</a><p>
	</body>
</html>
'''

metaRefresh = '<meta http-equiv="refresh" content="2;url=game.py">'

def printGameTable():
	print '<table>'
	print '<tr>'
	for x in range(16):
		if (userTable[x]==0):
			print '<td><a href=game.py?card=' + str(x) + '><img src="/img/back.png"></a></td>'
		elif (userTable[x]==9):
			print '<td><img src="/img/blank.jpg"></td>'
		elif (userTable[x]==1):
			print '<td><img src="/img/card' + str(solTable[x]) + '.jpg"></td>'
		if (x==3 or x==7 or x==11):
			print '</tr>'
			print '<tr>'
	print '</tr>'
	print '</table>'

print 'Content-type: text/html\r\n\r'
print topBody
printGameTable()
if (clickCount>1):
	print metaRefresh
print botBody
#print originalTable
#print metaRefresh



