# https://developers.facebook.com/tools/explorer - get token
# http://facebook-sdk.readthedocs.io/en/latest/api.html - python functionality
# get long lasting token
# https://graph.facebook.com/v2.8/oauth/access_token?grant_type=fb_exchange_token&client_id=app_id&client_secret=app_secret&fb_exchange_token=short_lived_token
import facebook

graph = facebook.GraphAPI(access_token="", version="2.10")

def searchUsers(graph, user):
	users = graph.search(type="user", q=user)
	for user in users['data']:
		print('%s, %s' % (user['id'], user['name'].encode()))

# searchUsers(graph, "Fletcher Marsh")
searchUsers(graph, "Eddie Dryer")

def searchPages(graph):
	pages = graph.search(type="page", q="CMU")
	for page in pages['data']:
		print(page['name'])

# searchPages(graph)

def getFriendCount(graph, userID='me'):
	friends = graph.get_connections(id=userID, connection_name='friends')
	print(friends)

# getFriendCount(graph)
# getFriendCount(graph, '141671133144396') # doesn't work because perms!
