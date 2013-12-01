#!/usr/bin/env python

import cgi, os, Cookie
import cgitb; 
cgitb.enable()  # for debugging

# Initialize game table
initGame = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
finalTable = [1,6,3,2,6,5,8,7,2,4,1,8,3,7,4,5]

'''
try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	print 'Content-type: text/html\r\n\r'
	print "session = " + cookie['gameTable'].value
except (Cookie.CookieError, KeyError):
	print 'Content-type: text/html\r\n\r'
	print "session cookie not set!"
	cookie = Cookie.SimpleCookie()
	cookie['clickCount'] = 0
	cookie['gameTable'] = finalTable
'''
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
gameTable = '''
		<table>
			<tr>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
			</tr>
			<tr>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
			</tr>
			<tr>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
			</tr>
			<tr>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
				<td><img src="/img/back.png"></td>
			</tr>
		</table>
'''

metaRefresh = '<meta http-equiv="refresh" content="2;url=game.py">'


form = cgi.FieldStorage()
keyword = form.getvalue('keyword')

print 'Content-type: text/html\r\n\r'
print topBody
print gameTable
# print metaRefresh
print botBody


