
# ----------------------------------------
# 15-112 Optional Lecture: Spotify API
# ----------------------------------------

Step 1:
Information and tutorial: https://developer.spotify.com/web-api/tutorial/
Follow the steps in the tutorial to get the client ID, client secret, and
redirect URI for your account.

Step 2:
Download this for Python: https://github.com/plamere/spotipy
Unzip the file and then use Terminal (for Macs) or Command Prompt (for Windows) 
to install with either of the following commands:

	pip install spotipy

	-or-

	easy_install spotipy

	-or-

	(Make sure you're in the same folder as your setup.py file
	HINT: it's in spotipy.master so just copy the address from the file browser
	and type cd *control paste* into your terminal/cmd prompt)

	python setup.py install

	-or-

	python3 setup.py install

To make sure that spotipy has properly installed, in your command prompt type
python *enter* to run the interpreter. This should appear:
	>>>

Type
	>>> import spotipy

If no errors appear, you are successful! If some errors appear and you're a 
windows user, check if you're the administrator. You may have to go to the 
Windows PowerShell (Admin) instead and install spotipy.

Step 3:
Get started!
The documentation on Spotipy is a bit outdated; Spotify now requires everything
to be authorized. So start off your code with this:

	import spotipy
	import spotipy.util as util

	scope = 'check out the scopes here: https://developer.spotify.com/web-api/using-scopes/'
	username = 'paste your profile uri here: go to spotify->profile->more->share->copy profile uri
				you should get something like spotify:user:1234567890, just paste the 1234567890 here'
	token = util.prompt_for_user_token(username, scope, 
	                                    client_id='obtained from application',
	                                    client_secret='same as client id',
	                                    redirect_uri='http://localhost:8888/callback')
	sp = spotipy.Spotify(auth=token)

You may want to play around with the examples in the spotipy-master folder first
to familiarize yourself with the functions, adjust syntax, etc.

****TIP**** I would try user_playlists_contents.py first, replacing the sys stuff
in the main function with the scope, username, and token you've created above.
Try running it in Terminal/CMD first in the folder its contained in. An authorization
page should pop up. After confirming, copy the link of the broken page that appears
next into Terminal/CMD and enter. This confirms the authorization and allows you to
access the rest of the API.

Have fun!


