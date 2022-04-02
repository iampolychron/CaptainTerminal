import os

#The functions used are defined here.
def sendtocmd(queuedcommand):
    os.system(queuedcommand);

#Main Code
sendtocmd("title CaptainTerminal - Version 0.0.1-alpha")
print("_____CaptainTerminal Setup_____")
print("[!] Press CTRL+C at any time to close this app.")
username = input("Enter your username: ")
host = "captain"
os.system("clear")
print("Welcome to CaptainTerminal!");
print("A lightweight terminal available for all PCs!");
print("Made by iampolychron")
print("--------------------")
while True:
    commandin = input(username + "@" + host + " $ ")
    sendtocmd(commandin)
