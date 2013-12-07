COMP 206 Assignment 5

Michael Ho 260532097
Che-Yuan Liu 260523197
Hee Su Jang 260531165

Hosted on McGill servers
New welcome page: http://cs.mcgill.ca/~hjang6/ass5/
Login page: http://cs.mcgill.ca/~cliu62/ass5/
Room page(handled by transfer.py): http://www.cs.mcgill.ca/~mho32/cgi-bin/transfer.py
Game page(handled by game.py): http://www.cs.mcgill.ca/~mho32/cgi-bin/game.py

1. While testing our game, please do not refresh the page as it is going to mess up the GET/POST and cookies. 
2. Also, in the magic card game, please wait until the cards close back after the second card opens, as Trottier servers are slower, if cards are clicked too fast, it’s gonna mess up the game, we used metarefresh tags in html
3. The only way to restart the game is to logout and log back in, as we use cookies to track game points (but the first cookie is initialized by a POST request)
4. Another detail is that the name of the POST <input> for inventories are Inventory1, Inventory2, etc. with capital “I” as described in the instructions
5. A TA said it was okay to have to a room page as well as a game page, it seems that some other groups say the opposite
6. Also, we made all the commands call directly from transfer.py instead of transfering to game.py for readability purpose, since our game system is extremely large and handles a lot of variables, game.py also carries the Inventory but through cookies and handle the game engine while keeping all information intact upon returning to the room page
7. Moving accross game room and door room will keep all gold coins and inventory due to cookies! But do not refresh the page

Our entire code will be made available on https://github.com/michaelchum/comp206 three days after submission (around December 7th)

Thank you for your time and this amazing semester!

Cheers,

Michael