#!/usr/bin/env python

import cgi, os, Cookie, datetime, string
import cgitb; 
cgitb.enable()  # for debugging

# Initialize game table
initGame = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
finalTable = [1,6,3,2,6,5,8,7,2,4,1,8,3,7,4,5]

# Helper function to parse cookie string into int list
def decodeList(string):
	string = string[1:-1]
	string_list = string.split(",")
	string_list = [int(x) for x in string_list]
	return string_list

# Logout function to delete cookie
def logout:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    cookie['clickCount']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'


# Check if cookie exists if not, initialize cookie
try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    userTable=cookie['userTable'].value
except (Cookie.CookieError, KeyError):
	cookie = Cookie.SimpleCookie()
	cookie['clickCount']=0
	cookie['userTable']=initGame
	cookie['clickCount']['expires'] = 1*1*3*60*60 # Expires in 3 hours
	cookie['userTable']['expires'] = 1*1*3*60*60
	print cookie # IMPORTANT SAVE cookie 

# Check get request for card ID
if (cgi.FieldStorage()):
	form = cgi.FieldStorage()
	card = form.getvalue('card')
	card = int(card)
	userTable = cookie['userTable'].value
	userTable = decodeList(userTable)
	userTable[card] = 1
	cookie['userTable'] = userTable
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
originalTable = '''
		<table>
			<tr>
				<td><a href=game.py?card=0><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=1><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=2><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=3><img src="/img/back.png"></a></td>
			</tr>
			<tr>
				<td><a href=game.py?card=4><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=5><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=6><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=7><img src="/img/back.png"></a></td>
			</tr>
			<tr>
				<td><a href=game.py?card=8><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=9><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=10><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=11><img src="/img/back.png"></a></td>
			</tr>
			<tr>
				<td><a href=game.py?card=12><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=13><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=14><img src="/img/back.png"></a></td>
				<td><a href=game.py?card=15><img src="/img/back.png"></a></td>
			</tr>
		</table>
'''

metaRefresh = '<meta http-equiv="refresh" content="2;url=game.py">'

print 'Content-type: text/html\r\n\r'
#print topBody
print cookie['userTable'].value
#print originalTable
#print metaRefresh
#print botBody


