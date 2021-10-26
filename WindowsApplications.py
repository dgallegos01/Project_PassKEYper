import pyautogui as pag 
import pygetwindow as gw
import os 
import time 
from tkinter import Tk 
from tkinter.filedialog import askopenfilename


class OpeningApps:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def get_application(self):
        return self.name

    def open_file(self):
        Tk().withdraw()
        filename = askopenfilename()
        os.startfile(filename)
        time.sleep(10)
            
    def zoomSignIn(self,SIGN_INX,SIGN_INY):
        time.sleep(5)
        pag.moveTo(SIGN_INX,SIGN_INY)
        pag.click()
    def minimize_current(self):
        window = gw.getActiveWindowTitle()
        current_window = gw.getWindowsWithTitle(window)[0]
        current_window.minimize()
    #Login 
    def typeAt(self,x,y):
        pag.moveTo(x,y)
        pag.click()
        pag.write(self.email, interval = 0.10)
        pag.moveTo(x, y + CONSTANT_DIFFERENCE)
        pag.click()
        pag.write(self.password, interval = 0.10)
    def clickHere(self,x,y):
        pag.moveTo(x,y)
        pag.click()
    def passwordEntry(self,x,y):
        pag.moveTo(x, y)
        pag.click()
        pag.write(self.password, interval = 0.10)

        


CONSTANT_DIFFERENCE = 60 #Pixel space between the email and password location in the application


def openApp(name):
    credentials = { line.split()[0] : line.split()[1] for line in open("credentials.txt") }
    PASSWORD = credentials.get("password_300")
    EMAIL = credentials.get("username_301")
    if(name == "Spotify"):
        EMAILX, EMAILY, PASSWORDX, PASSWORDY, LOGINX, LOGINY = findCoord(name)
    SIGN_INX, SIGN_INY, EMAILX, EMAILY, LOGINX, LOGINY = findCoord(name)
    openApplication = OpeningApps(name,EMAIL,PASSWORD)
    openApplication.minimize_current()
    #time.sleep(15)
    openApplication.open_file()
    if(name == "Zoom"):
        openApplication.zoomSignIn(SIGN_INX, SIGN_INY)
    if(name == "Spotify"):
        openApplication.passwordEntry(PASSWORDX, PASSWORDY)
    if(name == "Minecraft Launcher"):
        minecraft_window = gw.getWindowsWithTitle("Minecraft Launcher")[0]
        minecraft_window.maximize()
        pag.click()
        time.sleep(2)
        pag.moveTo(SIGN_INX,SIGN_INY)
        pag.click()
        time.sleep(2)
        openApplication.typeAt(EMAILX,EMAILY)
    else:
        openApplication.typeAt(EMAILX,EMAILY)
    openApplication.clickHere(LOGINX,LOGINY)

def findCoord(name):
    if name == "Minecraft Launcher":
    #Fullscreen Coordinates

        SIGN_INX = 674 #Initial log in button location x
        SIGN_INY = 402 #Initial log in button location y 

        EMAILX = 662 #Mojang email log in x 
        EMAILY = 290 #Mojang email log in y 

        LOGINX = 670
        LOGINY = 466
        return SIGN_INX, SIGN_INY, EMAILX, EMAILY, LOGINX, LOGINY
    
    #Zoom Application
    if name == "Zoom":
        SIGN_INX = 687 #Initialize log in button location x
        SIGN_INY = 402 #Initialize log in button location y 

        EMAILX = 530 #Zoom email location x
        EMAILY = 305 #Zoom email location y 

        LOGINX = 638 #Zoom sign in button x 
        LOGINY = 414 #Zoom sign in button y
        return SIGN_INX, SIGN_INY, EMAILX, EMAILY, LOGINX, LOGINY

            #Steam Application
    if name == "Steam":
        EMAILX = 668 #Steam username input x
        EMAILY = 296 #Steam username input y

            

        LOGINX = 686 #Steam sign in button x
        LOGINY = 393 #Steam sign in button y 

        CONSTANT_DIFFERENCE = 30
        return EMAILX, EMAILY, LOGINX, LOGINY
            
            
    if name == "Spotify":
        EMAILX = 788 #Spotify Email location x 
        EMAILY = 713 #Spotify Email location y

        PASSWORDX = 645
        PASSWORDY = 245

        LOGINX = 666 #Spotify sign in button x
        LOGINY = 378 #Spotify sign in button y
        return EMAILX, EMAILY, PASSWORDX, PASSWORDY, LOGINX, LOGINY
    