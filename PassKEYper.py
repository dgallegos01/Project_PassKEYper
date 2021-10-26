from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from PIL import ImageTk,Image
from WindowsApplications import *
import time
import os

def center_window(w=300, h=300):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
 
root = Tk()
root.title("PassKEYper")
root.minsize(600, 600)
root.maxsize(600, 600)
center_window(600, 600)
root.iconbitmap('PassKEYper_Icon.ico')
image = Image.open("PassKEYper_LogoV5.png")
image2 = Image.open("GeorgeMeme.png")
resize_image = image.resize((575, 230))
resize_image2 = image2.resize((600, 515))
img = ImageTk.PhotoImage(resize_image)
img2 = ImageTk.PhotoImage(resize_image2)

userName = False
passWord = False
userExists = True
variable = StringVar()

class newScreen:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.screen = Canvas(root, width=x, height=y, bg=color)
        self.screen.place(x=0, y=0)


    def textLabel(self, wordLabel, wordStyle, backColor, fontColor, pos_x, pos_y):
        self.wordLabel = wordLabel
        self.wordStyle = wordStyle
        self.backColor = backColor
        self.fontColor = fontColor
        self.pos_x = pos_x
        self.pos_y = pos_y 
        screenText = Label(self.screen, text=wordLabel, font=wordStyle, bg=backColor, fg=fontColor)
        screenText.place(x=pos_x, y=pos_y)

    def imageLabel(self, pos_x, pos_y, backColor):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.backColor = backColor
        screenText = Label(self.screen, image=img, bg=backColor)
        screenText.place(x=pos_x, y=pos_y)

    def imageLabel2(self, pos_x, pos_y, backColor):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.backColor = backColor
        screenText = Label(self.screen, image=img2, bg=backColor)
        screenText.place(x=pos_x, y=pos_y)

    def buttons(self, buttonLabel, pos_x, pos_y, buttonWidth, buttonHeight, wordStyle, backColor, fontColor, borderSize, buttonCommand = None):
        self.buttonLabel = buttonLabel
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.wordStyle = wordStyle
        self.backColor = backColor
        self.fontColor = fontColor
        self.borderSize = borderSize
        self.buttonCommand = buttonCommand
        newButton = Button(self.screen, text = buttonLabel, width = buttonWidth, height = buttonHeight, font = wordStyle, bg = backColor, fg = fontColor, activeforeground = fontColor, activebackground = backColor, bd = borderSize, command = buttonCommand).place(x=pos_x,y=pos_y)

    def boxes(self, X1, Y1, X2, Y2, thickness=None, color=None):
        self.X1 = X1
        self.Y1 = Y1
        self.X2 = X2
        self.Y2 = Y2
        self.thickness = thickness
        self.color = color
        self.screen.create_rectangle(X1, Y1, X2, Y2, width = thickness, outline=color)

    def line(self, X1, Y1, X2, Y2, thickness=None, color=None):
        self.X1 = X1
        self.Y1 = Y1
        self.X2 = X2
        self.Y2 = Y2
        self.thickness = thickness
        self.screen.create_line( X1, Y1, X2, Y2, width = thickness, fill = color)

    def message(self, pos_x, pos_y, width, text, backColor, fontColor, wordStyle):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.backColor = backColor
        self.fontColor = fontColor
        self.wordStyle = wordStyle
        newMessage = Message(self.screen, text= text)
        newMessage.config(bg=backColor, fg=fontColor, font=wordStyle, aspect=width)
        newMessage.place(x=pos_x, y=pos_y)
    
    def menu(self, pos_x, pos_y, Width, Height, text, color):
        global variable
        account_list = ['Choose an Account', 'Gmail', 'Amazon', 'Zoom', 'Spotifiy']
        variable.set(account_list[0])
        dropdown = OptionMenu(self.screen,variable,*account_list)
        dropdown.config(width=Width, height=Height, font=text, bg=color, activebackground=color)
        dropdown.place(x=pos_x, y=pos_y)

class AccountAutoSignIn:
    def __init__(self):
        self.Path1 = "chromedriver.exe"
        self.Path2 = "geckodriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.credentialCount = 0
        self.signIn = Credentials()
        self.credentials = { line.split()[0] : line.split()[1] for line in open("credentials.txt") }

    def gmailAccount(self):
        try:
            self.driver = webdriver.Chrome(self.Path1, options=self.options)
            self.driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
            'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
            '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
            print("{} has been launched".format(self.driver.title))
            time.sleep(2)
            self.gmail = self.driver.find_element_by_xpath('//*[@id ="identifierId"]')
            self.gmail.send_keys(self.credentials.get("username_100"))
            self.gmail.send_keys(Keys.ENTER)
            time.sleep(3)
            self.gmailLogin = self.driver.find_element_by_xpath( '//*[@id ="password"]/div[1]/div / div[1]/input')
            self.gmailLogin.send_keys(self.credentials.get("password_101"))
            self.gmailLogin.send_keys(Keys.ENTER)
        except:
            self.driver.quit()
            print("Something went wrong. Try again")
        print("Launch Successful!")


    def amazonAccount(self):
        try:
            self.driver = webdriver.Chrome(self.Path1, options=self.options)
            self.driver.get(r'https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_'+\
                'handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_'+\
                'select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_'+\
                'select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape='+\
                'http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to='+\
                'https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252F'+\
                'yourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1')
            print("{} has been launched".format(self.driver.title))
            self.amazon = self.driver.find_element_by_id("ap_email")
            time.sleep(2)
            self.amazon.send_keys(self.credentials.get("username_200"))
            self.amazon.send_keys(Keys.ENTER)
            self.amazonLogIn = self.driver.find_element_by_id("ap_password")
            time.sleep(2)
            self.amazonLogIn.send_keys(self.credentials.get("password_201"))
            self.amazonLogIn.send_keys(Keys.ENTER)
        except:
            self.driver.quit()
            print("Something went wrong. Try again")
        print("Launch Successful!")

    def facebookAccount(self):
        pass

    def youtubeAccount(self):
        pass


class Credentials:
    def __init__(self):
        self.usernameCount = 0
        self.passwordCount = 0
        self.passwordKrypt = {}

        try:
            with open("credentials.txt", 'r') as f:
                self.lines = f.read().splitlines()
                self.last_Password = self.lines[-1]
                self.last_username = self.lines[-2]
                self.passwordNum = self.last_Password[9]
                self.passwordCount = int(self.passwordNum)
        except:
            f = open("credentials.txt", "w+")


    def newPassword(self, createUSER, creatPSW):
        self.creatPSW = creatPSW
        self.createUSER = createUSER
        self.passwordCount += 1
        self.usernameCount += 1
        self.passwordKrypt["username_{}".format(self.passwordCount)] = createUSER
        self.passwordKrypt["password_{}".format(self.passwordCount)] = creatPSW

    def GmailCredentials(self, createUSER, creatPSW):
        self.passwordKrypt["username_100"] = createUSER
        self.passwordKrypt["password_101"] = creatPSW

    def AmazonCredentials(self, createUSER, creatPSW):
        self.passwordKrypt["username_200"] = createUSER
        self.passwordKrypt["password_201"] = creatPSW

    def ZoomCredentials(self, createUSER, creatPSW):
        self.passwordKrypt["username_300"] = createUSER
        self.passwordKrypt["password_301"] = creatPSW

    def SpotifiyCredentials(self, createUSER, creatPSW):
        self.passwordKrypt["username_400"] = createUSER
        self.passwordKrypt["password_401"] = creatPSW

    def savePassword(self):
        with open("credentials.txt", 'a') as f:
            for key, value in self.passwordKrypt.items(): 
                f.write('%s %s\n' % (key, value))

    def getPasswords(self, usernameMatch, passwordMatch):
        global userName
        global passWord
        global userExists
        self.usernameMatch = usernameMatch
        self.passwordMatch = passwordMatch
        try:
            self.d = { line.split()[0] : line.split()[1] for line in open("credentials.txt") }
            self.l = []
            for key in self.d:
                if key[0:8] == 'password':
                    self.l.append(self.d[key])
                elif key[0:8] == 'username':
                    self.l.append(self.d[key])

            if usernameMatch in self.l and passwordMatch in self.l:
                print("Login successful!")
                userName = True
                passWord = True

            elif usernameMatch == '' and passwordMatch == '':
                print("Please Enter your username and password")
            
            elif usernameMatch not in self.l and passwordMatch not in self.l:
                print("No such username or password exists. Please register an account")
                userExists = False
            
            else:
                print("Username or password is incorrect. Try again")
                
        except:
            print("Somthing went wrong. Closing program.")
            quit()
            

def register_page():
    Main_Screen = newScreen(600, 600, "#2A2A2A")
    Main_Screen.line(0, 90, 600, 90, thickness = 5, color = "#32CD32")
    Main_Screen.boxes(5,5,595,595, thickness=7, color="#32CD32")
    Main_Screen.textLabel("Register", "Times 40 bold", "#2A2A2A", "#32CD32", 190, 10)
    Main_Screen.buttons("Back", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, firstPage)
    Main_Screen.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)
    Main_Screen.textLabel("Create Username:","Times 20 bold", "#2A2A2A", "#32CD32", 180, 152)
    Main_Screen.textLabel("Create Password:","Times 20 bold", "#2A2A2A", "#32CD32", 180, 253)  
    # Function for the username text box
  
    credentials = Credentials()

    def register_credentials_click(): 
        if user_register.get() == '' and pass_register.get() == '':
            print("Invalid Input. Try again")
            return register_page()
        else:
            credentials.newPassword(user_register.get(), pass_register.get())
            credentials.savePassword()

    def showPassword():
        passwordEntered = Entry(width = 19, textvariable = pass_register).place(x = 210, y = 285)
    def unshowPassword():
        passwordEntered = Entry(width = 19, show = '*', textvariable = pass_register).place(x = 210, y = 285)


    user_register = StringVar()
    usernameEntered = Entry(width = 19, textvariable = user_register).place(x = 210, y = 185)
    pass_register = StringVar()
    passwordEntered = Entry(width = 19, show = '*', textvariable = pass_register).place(x = 210, y = 285)

    # Submit Button
    Main_Screen.buttons("Submit", 190, 450, 15, 2, "Times 15 bold", "#32CD32", "Black", 10, buttonCommand = lambda:[register_credentials_click(), login_page()])# buttonCommand = password)
    Main_Screen.buttons("Show Password", 175, 320, 15, 2, "Times 7 bold", "#32CD32", "Black", 5, buttonCommand = lambda:[showPassword()])# buttonCommand = password)
    Main_Screen.buttons("Un-Show Password", 285, 320, 15, 2, "Times 7 bold", "#32CD32", "Black", 5, buttonCommand = lambda:[unshowPassword()])

def login_page():
    Main_Screen = newScreen(600, 600, "#2A2A2A")
    Main_Screen.line(0, 90, 600, 90, thickness = 5, color = "#32CD32")
    Main_Screen.boxes(5,5,595,595, thickness=7, color="#32CD32")
    Main_Screen.textLabel("Login", "Times 40 bold", "#2A2A2A", "#32CD32", 220, 10)
    Main_Screen.buttons("Back", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, firstPage)
    Main_Screen.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)
    Main_Screen.textLabel("Username:","Times 25 bold", "#2A2A2A", "#32CD32", 65, 140)
    Main_Screen.textLabel("Password:","Times 25 bold", "#2A2A2A", "#32CD32", 75, 240) 
    # Function for the text box

    checkCredentials = Credentials()

    def credentials_click():   
        checkCredentials.getPasswords(user_name.get(), password.get())
        if userName == True and passWord == True:
            choicePage()
        elif userExists == False:
            register_page()
        else:
            login_page()

    def showPassword1():
        passwordEntered = Entry(width = 19, textvariable = password).place(x = 230, y = 255)
    def unshowPassword1():
        passwordEntered = Entry(width = 19, show = '*', textvariable = password).place(x = 230, y = 255)

    # Instance variable
    user_name = StringVar()
    usernameEntered = Entry(width = 19, textvariable = user_name).place(x = 230, y = 155)
    # Function for the text box     
    password = StringVar()
    passwordEntered = Entry(width = 19, show="*", textvariable = password).place(x = 230, y = 255)
    # Submit Button
    Main_Screen.buttons("Submit", 190, 350, 15, 2, "Times 15 bold", "#32CD32", "Black", 10, credentials_click)# buttonCommand = password)
    Main_Screen.buttons("Show Password", 195, 290, 15, 2, "Times 7 bold", "#32CD32", "Black", 5, buttonCommand = lambda:[showPassword1()])# buttonCommand = password)
    Main_Screen.buttons("Un-Show Password", 305, 290, 15, 2, "Times 7 bold", "#32CD32", "Black", 5, buttonCommand = lambda:[unshowPassword1()])
    

def firstPage():
    startScreen = newScreen(600, 600, "#2A2A2A")
    startScreen.imageLabel(10,10, "#2A2A2A")
    startScreen.boxes(5,5,595,595, thickness=7, color="#32CD32")
    startScreen.line(0, 250, 600, 250, thickness = 5, color = "#32CD32")
    startScreen.textLabel("Login or Register", "Times 30 bold", "#2A2A2A", "#32CD32", 135, 260)
    startScreen.buttons("Info", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, infoPage)
    startScreen.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)
    startScreen.buttons("Login", 190, 325, 15, 2, "Times 15 bold", "#32CD32", "Black", 10, login_page)
    startScreen.buttons("Register", 190, 425, 15, 2, "Times 15 bold", "#32CD32", "Black", 10, register_page)

def choicePage():
    global userName
    global passWord
    choice_page = newScreen(600, 600, "#2A2A2A")
    choice_page.line(0, 90, 600, 90, thickness = 5, color = "#32CD32")
    choice_page.boxes(5,5,595,595, thickness=7, color="#32CD32")
    choice_page.textLabel("Options", "Times 40 bold", "#2A2A2A", "#32CD32", 200, 10)
    def logout():
        userName = False
        passWord = False

    choice_page.buttons("Logout", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, buttonCommand = lambda:[firstPage(), logout()])
    choice_page.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)
    choice_page.textLabel("1. Access an account:", "Times 25 bold", "#2A2A2A", "#32CD32", 140, 120)
    choice_page.buttons("Enter", 250, 170, 5, 1, "Times 16 bold", "#32CD32", "Black", 10, accountPage)
    choice_page.textLabel("2. Add account credentials:", "Times 25 bold", "#2A2A2A", "#32CD32", 90, 240)
    choice_page.buttons("Enter", 250, 290, 5, 1, "Times 16 bold", "#32CD32", "Black", 10, accountCreationPage)
    choice_page.textLabel("3. Access a password:", "Times 25 bold", "#2A2A2A", "#32CD32", 130, 350)
    def passwordAccess():
        passwordList = { line.split()[0] : line.split()[1] for line in open("credentials.txt") }
        for key in passwordList:
            if key[0:8] == 'password':
                print(passwordList[key],"\n")
    choice_page.buttons("Enter", 250, 400, 5, 1, "Times 16 bold", "#32CD32", "Black", 10,passwordAccess)
    choice_page.buttons("", 10, 566, None, None, None, "#2A2A2A", None, None, easterEggPage)
   
def accountPage():
    accountAccess = AccountAutoSignIn()
    account_page = newScreen(600, 600, "#2A2A2A")
    account_page.line(0, 90, 600, 90, thickness = 5, color = "#32CD32")
    account_page.boxes(5,5,595,595, thickness=7, color="#32CD32")
    account_page.textLabel("Accounts", "Times 40 bold", "#2A2A2A", "#32CD32", 180, 10)
    account_page.buttons("Home", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, choicePage)
    account_page.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)
    account_page.menu(100,210,16,1,"Times 20 bold","#32CD32")
    
    def accountChoice():
        d = { line.split()[0] : line.split()[1] for line in open("credentials.txt") } 
        l = []
        for key in d:
            l.append(key)
        global variable
        print(variable.get())
        if variable.get() == 'Gmail':
            if 'password_101' in l:
                accountAccess.gmailAccount()
            else:
                print("Account not registered. Please make one")
                accountCreationPage()
        elif variable.get() == 'Amazon':
            if 'password_201' in l:
                accountAccess.amazonAccount()
            else:
                print("Account not registered. Please make one")
                accountCreationPage()
        elif variable.get() == 'Zoom':
            if 'password_301' in l:
                openApp("Zoom")
            else:
                print("Account not registered. Please make one")
                accountCreationPage()
        elif variable.get() == 'Spotifiy':
            if 'password_401' in l:
                openApp("Spotify")
            else:
                print("Account not registered. Please make one")
                accountCreationPage()
        else:
            pass
    account_page.buttons("Enter", 390, 200, 5, 1, "Times 20 bold", "#32CD32", "Black", 10, accountChoice)

 
def infoPage():
    info_page = newScreen(600, 600, "#2A2A2A")
    info_page.line(0, 90, 600, 90, thickness = 5, color = "#32CD32")
    info_page.boxes(5,5,595,595, thickness=7, color="#32CD32")
    info_page.textLabel("Info", "Times 40 bold", "#2A2A2A", "#32CD32", 240, 10)
    info_page.buttons("Back", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, firstPage)
    info_page.textLabel("Welcome to PassKEYper!", "Times 30 bold", "#2A2A2A", "#32CD32", 85, 100)
    info_page.textLabel("• When registering you are creating one 'master password'", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 200)
    info_page.textLabel("  to access your accounts.", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 225)
    info_page.textLabel("• Once logged in you may access, add, or remove any accounts;", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 300)
    info_page.textLabel("  as well as check password history.", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 325)
    info_page.textLabel("• When dealing with webistes or apps, all you have to do is select", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 400)
    info_page.textLabel("  an account from PassKEYper to login in securely.", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 425)
    info_page.textLabel("• Sit back and enjoy the luxury of not remembering passwords", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 500)
    info_page.textLabel("  while still being cyber-secure!", "Times 15 bold", "#2A2A2A", "#32CD32", 30, 525)
    info_page.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)

def accountCreationPage():
    newCredentials = Credentials()
    account_page = newScreen(600, 600, "#2A2A2A")
    account_page.line(0, 90, 600, 90, thickness = 5, color = "#32CD32")
    account_page.boxes(5,5,595,595, thickness=7, color="#32CD32")
    account_page.textLabel("Account Registration", "Times 25 bold", "#2A2A2A", "#32CD32", 145, 25)
    account_page.buttons("Home", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, choicePage)
    account_page.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)
    account_page.menu(160,120,16,1,"Times 20 bold","#32CD32")
    account_page.textLabel("Enter credentials for the selected account", "Times 20 bold", "#2A2A2A", "#32CD32", 50, 260)
    account_page.textLabel("Username:","Times 20 bold", "#2A2A2A", "#32CD32", 140, 300)
    account_page.textLabel("Password:","Times 20 bold", "#2A2A2A", "#32CD32", 140, 340)
    user_name = StringVar()
    usernameEntered = Entry(width = 19, textvariable = user_name).place(x = 275, y = 310)
    password = StringVar()
    passwordEntered = Entry(width = 19, show="*", textvariable = password).place(x = 275, y = 350)
    account_page.textLabel("Once you hit 'Submit' your credentials will be saved", "Times 18 bold", "#2A2A2A", "#32CD32", 30, 390)
    def accountChoice():
        global variable
        print(variable.get())
        if variable.get() == 'Gmail':
            newCredentials.GmailCredentials(user_name.get(), password.get())
            newCredentials.savePassword()
            accountPage()
        elif variable.get() == 'Amazon':
            newCredentials.AmazonCredentials(user_name.get(), password.get())
            newCredentials.savePassword()
            accountPage()
        elif variable.get() == 'Zoom':
            newCredentials.ZoomCredentials(user_name.get(), password.get())
            newCredentials.savePassword()
            accountPage()
        elif variable.get() == 'Spotifiy':
            newCredentials.SpotifiyCredentials(user_name.get(), password.get())
            newCredentials.savePassword()
            accountPage()
        else:
            print("Please choose an account")
    account_page.buttons("Submit", 240, 430, 5, 1, "Times 20 bold", "#32CD32", "Black", 10, accountChoice)
    
def easterEggPage():
    page = newScreen(600, 600, "#2A2A2A")
    page.boxes(5,5,595,595, thickness=7, color="#32CD32")
    page.textLabel("Easter Egg!", "Times 30 bold", "#2A2A2A", "#32CD32", 190, 25)
    page.buttons("Home", 455, 20, 0, 0, "Times 20 bold", "grey", "black", 5, choicePage)
    page.buttons("Exit", 60, 20, 0, 0, "Times 20 bold", "grey", "black", 5, quit)
    page.imageLabel2(0,85, "#2A2A2A")

    
firstPage()

root.mainloop()