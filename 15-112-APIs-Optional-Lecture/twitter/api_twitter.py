# create twitter app - https://apps.twitter.com/app/new
# get keys
# get started - https://python-twitter.readthedocs.io/en/latest/twitter.html

import twitter

api = twitter.Api(consumer_key="",
				  consumer_secret="",
				  access_token_key="",
				  access_token_secret="")

def getFriends(api):
	users = api.GetFriends()
	for u in users:
		print(u.name)

getFriends(api)

def post(api, msg):
	status = api.PostUpdate(msg)
	print(status.text)

# post(api, "Testing Python Twitter API!")

def DM(api, user, msg):
	dm = api.PostDirectMessage(msg, user)
	print(dm)

DM(api, "1107124159", "BOO") # message Amy Shan "Boo"
