import requests
import pprint
import random
from xml.dom.minidom import parseString

#define multiple functions: get list of games, return random game, etc
#doesn't work for private profiles

def getUsersUnplayedGames(userName):
    unplayedGames = []#creates a list to store all the unplayed games from a users steam account

    steamAccount = userName

    if steamAccount.isnumeric():#need this if-else statement because the website has a different base url for custom accounts
        steamXML = requests.get('http://www.steamcommunity.com/profiles/' + steamAccount + '/?xml=1')
    else:
        steamXML = requests.get('http://www.steamcommunity.com/id/' + steamAccount + '/?xml=1')
    steamXML.close()

    dom = parseString(steamXML.content)
    xmlTag = dom.getElementsByTagName('steamID64')[0].toxml()#looks for the tag steamID64 and the line below strips out the tags
    steamNumber = xmlTag.replace('<steamID64>','').replace('</steamID64>','')

    query_params={  'key': '636E9A263AA0DCBCC518E06E0A55347E',
                    'format': 'json',
                    'steamid': steamNumber,
                    'include_appinfo': 1,
    }

    endpoint = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'

    response = requests.get(endpoint, params=query_params)
    data = response.json()#converts the json returned from response a dictionary

    for x in range(data['response']['game_count']):#for loop to add games the user has never played to a list
        if(data['response']['games'][x]['playtime_forever'] == 0):
           unplayedGames.append(data['response']['games'][x]['name'])

    return(unplayedGames)

def getUsersGames(userName):
    Games = []#creates a list to store all the games from a users steam account

    steamAccount = userName

    if steamAccount.isnumeric():#need this if-else statement because the website has a different base url for custom accounts
        steamXML = requests.get('http://www.steamcommunity.com/profiles/' + steamAccount + '/?xml=1')
    else:
        steamXML = requests.get('http://www.steamcommunity.com/id/' + steamAccount + '/?xml=1')
    steamXML.close()

    dom = parseString(steamXML.content)
    xmlTag = dom.getElementsByTagName('steamID64')[0].toxml()#looks for the tag steamID64 and the line below strips out the tags
    steamNumber = xmlTag.replace('<steamID64>','').replace('</steamID64>','')

    query_params={  'key': '636E9A263AA0DCBCC518E06E0A55347E',
                    'format': 'json',
                    'steamid': steamNumber,
                    'include_appinfo': 1,
    }

    endpoint = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'

    response = requests.get(endpoint, params=query_params)
    data = response.json()#converts the json returned from response a dictionary

    for x in range(data['response']['game_count']):#for loop to add games
        if(data['response']['games'][x]['playtime_forever'] >= 0):
           Games.append(data['response']['games'][x]['name'])

    return(Games)

def getRandomUnplayedGame(unplayedGames):
     random.seed()
     randomGame = random.randrange(0, len(unplayedGames)-1)#dunno if -1 is needed
     chosenGame = unplayedGames[randomGame]
     print(chosenGame)
     return(chosenGame)

def getRandomGame(Games):
     random.seed()
     randomGame = random.randrange(0, len(Games))#dunno if -1 is needed
     chosenGame = Games[randomGame]
     print(chosenGame)
     return(chosenGame)
