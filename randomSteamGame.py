#Steam API Random Game Implementation
#Brendon Hollingsworth and Jacob Pillai
#9-26-2013

#TO DO:
#add ABOUT option to help tab of menu
#add radiobuttons to get a game of a particular score on GB
# etc, etc, etc...

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import SteamAPI
import GiantBombAPI


#Menu functions:
def menuHelp():
    messagebox.showinfo(title="Steam ID Help", message="Need help finding your steam ID? Go to steamcommunity.com and navigate to your account profile page. Your account ID will be in the URL at the top to the right of /profiles/. Also, make sure your profile is set to public in the privacy settings page. ")


#Button functions:
class priorUserInfo: #class to store user information from last click, should help with load times
    userName = ""
    Games = []
    unplayedGames = []

def randomGameButtonHandler():
    userName = steamID.get()
    neverPlayed = neverplayed.get()
    getGame(userName, neverPlayed)


def getGame(userName, neverPlayed):
    if(priorUserInfo.userName == userName):
        if(neverPlayed == 1):
            randomGame = SteamAPI.getRandomUnplayedGame(priorUserInfo.unplayedGames)
            outputText.set(randomGame)
            gameData = GiantBombAPI.getGBData(randomGame)
            GBgameInfo = GiantBombAPI.getMoreInfo(gameData)

        elif(neverPlayed == 0):
            randomGame = SteamAPI.getRandomGame(priorUserInfo.Games)
            outputText.set(randomGame)
            gameData = GiantBombAPI.getGBData(randomGame)
            GBgameInfo = GiantBombAPI.getMoreInfo(gameData)

    else:
        Games = SteamAPI.getUsersGames(userName)
        priorUserInfo.Games = Games
        unplayedGames = SteamAPI.getUsersUnplayedGames(userName)
        priorUserInfo.unplayedGames = unplayedGames

        if(neverPlayed == 1):
            randomGame = SteamAPI.getRandomUnplayedGame(unplayedGames)
            outputText.set(randomGame)
            gameData = GiantBombAPI.getGBData(randomGame)
            GBgameInfo = GiantBombAPI.getMoreInfo(gameData)

        elif(neverPlayed == 0):
            randomGame = SteamAPI.getRandomGame(Games)
            outputText.set(randomGame)
            gameData = GiantBombAPI.getGBData(randomGame)
            GBgameInfo = GiantBombAPI.getMoreInfo(gameData)


    infoBox.config(state=NORMAL)
    infoBox.insert(END, GBgameInfo)
    infoBox.insert(END, '\n\n')
    infoBox.see(END)
    infoBox.config(state=DISABLED)
    priorUserInfo.userName = userName

#Build GUI:
root = Tk()
root.title("_random_game_")

steamID = StringVar()#hold the input ID
outputText = StringVar()#hold the output game
neverplayed = IntVar()#hold value for never played game or not, 1 for true, 0 for false

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#MENUBAR
menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0)#tearoff enables/disables a default pop up window
helpmenu.add_command(label = "_help_", command=menuHelp)
helpmenu.add_command(label = "_about_")

menubar.add_cascade(label = "_options_", menu=helpmenu)
root.config(menu=menubar)#cannot pack. must config toplevel window to add menu



#will hold the information pane with game details
infoframe = ttk.Frame(mainframe, borderwidth = 5, relief = GROOVE)
infoframe.grid(column=2, row=2)
infoBox = Text(infoframe, wrap = WORD, width =75, height = 20)
infoBox.config(state=DISABLED)
infoBox.pack()



#steam id input label and entry box
ttk.Label(mainframe, text="_steam_ID__: ").grid(column=2, row=3, sticky=W)
userNameField = ttk.Entry(mainframe, width=30, textvariable=steamID)
userNameField.grid(column=2, row=3, sticky=E)

#random game output label and output label
ttk.Label(mainframe, text="_random_game_: ").grid(column=2, row=4, sticky=W)
ttk.Label(mainframe, textvariable=outputText).grid(column=2, row=4, sticky=E)

#check box for a never played game
neverPlayedButton = Checkbutton(mainframe, text="_Never_played_", var=neverplayed)
neverPlayedButton.grid(column=2, row=5, sticky=W)

#check box for a 'good game'

#get random game button
getgamebutton = ttk.Button(mainframe, text="_get_game_ ", command=randomGameButtonHandler)
getgamebutton.grid(column=2, row=6, sticky=(N, W, E, S))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#give everything inside mainframe a little cushion from one child to the other

userNameField.focus()
root.bind('<Return>', randomGameButtonHandler)

root.mainloop()
