#Steam API Random Game Implementation
#Brendon Hollingsworth and Jacob Pillai
#9-26-2013

#TO DO:
# etc, etc, etc...

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import SteamAPI
import GiantBombAPI
import webbrowser

class priorUserInfo: #class to store user information from last click, should help with load times
    userName = ""
    Games = []
    unplayedGames = []
    previousGame = ""
    previousGameLink = ""

#Menu functions:
def menuHelp():
    messagebox.showinfo(title="Steam ID Help", message="Need help finding your steam ID? \n\n1) Go to steamcommunity.com and navigate to your account profile page. \n\n2) Your account ID will be in the URL at the top to the right of /profiles/. \n\n3) Also, make sure your profile is set to public in the privacy settings page. ")

def menuAbout():
    messagebox.showinfo(title="About GameGetter", message="Creators: Brendon Hollingsworth and Jacob Pillai \n\nVersion: 1.0 \n\nContact Us: asahibeeru@gmail.com ")

#Button functions:
def randomGameButtonHandler(*args):
    userName = steamID.get()
    neverPlayed = neverplayed.get()
    getGame(userName, neverPlayed)

def getMoreInfoLinkButtonHandler():
    if(priorUserInfo.previousGameLink != "no"):
        webbrowser.open(priorUserInfo.previousGameLink, new=0, autoraise = True)
    else:
        infoBox.config(state=NORMAL)
        infoBox.insert(END, "No link could be found for the given title. ")
        infoBox.insert(END, "\n\n")
        infoBox.config(state=DISABLED)
        infoBox.see(END)


def getGame(userName, neverPlayed):
    if(priorUserInfo.userName == userName):
        if(neverPlayed == 1):
            randomGame = SteamAPI.getRandomUnplayedGame(priorUserInfo.unplayedGames)
            outputText.set(randomGame)
            gameData = GiantBombAPI.getGBData(randomGame)

            #if, else needed to make sure there was no error when getting the gameData
            if(GiantBombAPI.getLink(gameData) != 0):
                priorUserInfo.previousGameLink = GiantBombAPI.getLink(gameData)
            else:
                priorUserInfo.previousGameLink = "no"

            #if, else needed to make sure there was no error when getting gameData
            if (gameData != 0):
                GBgameInfo = GiantBombAPI.getMoreInfo(gameData)
            else:
                GBgameInfo = "No information could be found about this title. "

        elif(neverPlayed == 0):
            randomGame = SteamAPI.getRandomGame(priorUserInfo.Games)
            outputText.set(randomGame)
            gameData = GiantBombAPI.getGBData(randomGame)

            #if, else needed to make sure there was no error when getting the gameData
            if(GiantBombAPI.getLink(gameData) != 0):
                priorUserInfo.previousGameLink = GiantBombAPI.getLink(gameData)
            else:
                priorUserInfo.previousGameLink = "no"

            #if, else needed to make sure there was no error when getting gameData
            if (gameData != 0):
                GBgameInfo = GiantBombAPI.getMoreInfo(gameData)
            else:
                GBgameInfo = "No information could be found about this title. "

    else:
        Games = SteamAPI.getUsersGames(userName)
        priorUserInfo.Games = Games
        unplayedGames = SteamAPI.getUsersUnplayedGames(userName)
        priorUserInfo.unplayedGames = unplayedGames

        if(neverPlayed == 1):
            randomGame = SteamAPI.getRandomUnplayedGame(unplayedGames)
            outputText.set(randomGame)
            priorUserInfo.previousGame = randomGame
            gameData = GiantBombAPI.getGBData(randomGame)

            #if, else needed to make sure there was no error when getting the gameData
            if(GiantBombAPI.getLink(gameData) != 0):
                priorUserInfo.previousGameLink = GiantBombAPI.getLink(gameData)
            else:
                priorUserInfo.previousGameLink = "no"

            #if, else needed to make sure there was no error when getting gameData
            if (gameData != 0):
                GBgameInfo = GiantBombAPI.getMoreInfo(gameData)
            else:
                GBgameInfo = "No information could be found about this title. "

        elif(neverPlayed == 0):
            randomGame = SteamAPI.getRandomGame(Games)
            outputText.set(randomGame)
            gameData = GiantBombAPI.getGBData(randomGame)

            #if, else needed to make sure there was no error when getting the gameData
            if(GiantBombAPI.getLink(gameData) != 0):
                priorUserInfo.previousGameLink = GiantBombAPI.getLink(gameData)
            else:
                priorUserInfo.previousGameLink = "no"

            #if, else needed to make sure there was no error when getting gameData
            if (gameData != 0):
                GBgameInfo = GiantBombAPI.getMoreInfo(gameData)
            else:
                GBgameInfo = "No information could be found about this title. "


    infoBox.config(state=NORMAL)
    infoBox.insert(END, GBgameInfo)
    infoBox.insert(END, '\n\n')
    infoBox.see(END)
    infoBox.config(state=DISABLED)
    priorUserInfo.userName = userName

#Build GUI:
root = Tk()
root.title("Random Game")


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
helpmenu.add_command(label = "Help", command=menuHelp)
helpmenu.add_command(label = "About", command=menuAbout)

menubar.add_cascade(label = "Options", menu=helpmenu)
root.config(menu=menubar)#cannot pack. must config toplevel window to add menu



#will hold the information pane with game details
infoframe = ttk.Frame(mainframe, borderwidth = 5, relief = GROOVE)
infoframe.grid(column=2, row=2)
infoBox = Text(infoframe, wrap = WORD, width =75, height = 20)
infoBox.insert(END, "Welcome to Game Getter! Please enter your steam ID into the field below to find yourself a random game to play. If you require assistance in finding your correct steam ID, visit our help section located in the above options bar. ")
infoBox.insert(END, '\n\n')
infoBox.config(state=DISABLED)
infoBox.pack()

#steam id input label and entry box
ttk.Label(mainframe, text="Steam ID: ").grid(column=2, row=3, sticky=W)
userNameField = ttk.Entry(mainframe, width=30, textvariable=steamID)
userNameField.grid(column=2, row=3, sticky=E)

#random game output label and output label
ttk.Label(mainframe, text="Random Game: ").grid(column=2, row=4, sticky=W)
ttk.Label(mainframe, textvariable=outputText).grid(column=2, row=4, sticky=E)

#check box for a never played game
neverPlayedButton = ttk.Checkbutton(mainframe, text="Unplayed", var=neverplayed)
neverPlayedButton.grid(column=2, row=5, sticky=W)

#check box for a 'good game'

#get random game button
getgamebutton = ttk.Button(mainframe, text="Get Game", command=randomGameButtonHandler)
getgamebutton.grid(column=2, row=6, sticky=E)

#open link to Giant Bomb for random game button
getlinkbutton = ttk.Button(mainframe, text="Open Link", command=getMoreInfoLinkButtonHandler)
getlinkbutton.grid(column=2, row=6, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
#give everything inside mainframe a little cushion from one child to the other

userNameField.focus()
root.bind('<Return>', randomGameButtonHandler)

root.mainloop()
