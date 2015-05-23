import requests

def getGBData(game):#need to run this first
    query_params={  'api_key': '45d87803202f42bfa349be91e28ac9e1acc1597d',
                'format': 'json',
                'limit': 1,
                'query': game,
                'resources': 'game',
    }

    searchEndpoint = 'http://www.giantbomb.com/api/search'

    response = requests.get(searchEndpoint, params=query_params)
    searchData = response.json()

    try:
        gameEndpoint = searchData['results'][0]['api_detail_url']
    except IndexError:
        return(0)


    game_params={  'api_key': '45d87803202f42bfa349be91e28ac9e1acc1597d',
                'format': 'json',
                'limit': 1,
    }

    response = requests.get(gameEndpoint, params=game_params)
    gameData = response.json()

    return(gameData)

def getGameScore(GBData):#most games on Giant Bomb don't have a score, need to make a way to prevent an error if game has no score
    #there is probably a better way to do this I just don't know it yet
    game_params={  'api_key': '45d87803202f42bfa349be91e28ac9e1acc1597d',
                'format': 'json',
                'limit': 1,
    }
    reviewEndpoint = GBData['results']['reviews'][0]['api_detail_url']#need to make program not crash if no reviews exist
    response = requests.get(reviewEndpoint, params=game_params)
    reviewData = response.json()

    return(reviewData['results']['score'])

def getMoreInfo(GBData):
    return(GBData['results']['deck'])

def getLink(GBData):
    try:
        return(GBData['results']['site_detail_url'])
    except TypeError:
        return(0)

#def getGenre(GBData):
    #genredict = ""
    #for x in range(0,2):
       #genredict = GBData['results']['genres'][x]
       #genredict.append(", ")

    #genrestring = str(genredict)
    #return(genrestring)

#below this is a simple program to test the functions
#dunno the right place to put the stuff below...but it works here
#game = input('what game you want')

#GBData= getGBData(game)
#score = getGameScore(GBData)
#gameInfo = getMoreInfo(GBData)
#genre = getGenre(GBData)

#print(score)
#print(gameInfo)
#print(genre)



