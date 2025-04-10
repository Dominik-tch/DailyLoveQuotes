import json
import encrypting_tests as crypt
import os
import sys
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import subprocess
import requests

REPO = "dominik-tch/DailyLoveQuotes"
BRANCH = "main"

script_dir = os.path.dirname(os.path.abspath(__file__))
#Hallo test update
def git_pull():
    print("Pull started:")
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True, check=True, cwd=script_dir)
        print("Git pull output:\n", result.stdout)
        updateLabel.config(text="Update abgeschlossen! Version ist aktuell.")
        updateButton.pack_forget()
    except subprocess.CalledProcessError as e:
        print("Git pull failed:\n", e.stderr)
        
def get_remote_commit():
    url = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"
    response = requests.get(url)
    print(response.json()["sha"])
    if response.status_code == 200:
        return response.json()["sha"]
    else:
        raise Exception("Fehler beim Abrufen des Remote-Commits.")
#check current version
def get_local_commit():
    

    result = subprocess.run(["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE, cwd=script_dir)
    return result.stdout.decode("utf-8").strip()

local = get_local_commit()
remote = get_remote_commit()
updateText = ""
fontSize = 12
buttonVisible = False
if local == remote:
     updateText = "You have the latest version!"
else:
     updateText = "There is an update available!"
     fontSize = 20
     buttonVisible = True
print(updateText)


memory_fileName = "Memory.json"
memory = {"days":"2025-03-01", "quoteNum":0}

#Generate a Memory.json file to store information about already used quotes and days

if os.path.exists(memory_fileName):
    with open(memory_fileName, "r", encoding="utf-8") as file:
            memory = json.load(file)
            if isinstance(memory, dict):
                 print("it is da dictionary")
            else:
                 print("#It is not a dict!")
else:    
    with open(memory_fileName, "w", encoding="utf-8") as file:
        json.dump(memory, file)

#save the current date
#current_date = "2025-03-02"
current_date = datetime.now().date()
added_title = ""
#check if the current date is already memorized else memorize it
if memory["days"] == str(current_date):
    loveQuote = "You already had your daily love quote ;)\nLook forward to tomorrow! "
else:
    #memory["days"] = "2025-03-02"
    memory["days"] = str(current_date)

    #loads the quotes from the file
    try:
        with open(script_dir + "\QuoteList.json", "r", encoding="utf-8") as file:
                quoteList = json.load(file)
    except:
        raise ValueError("Coud not open the QuoteList.json Check if it exits in the same directory (DailyLoveQuotes)")

    #checks if there are enogh quotes left and chooses the qoute
    listLen = len(quoteList) - 1
    
    if listLen < memory["quoteNum"]:
        loveQuote = "I'm very sorry but you ran out of saved love quotes.\nYou are as strong as on every other day, so this is no problem for you!\nNow contact your loved one to update your love quotes as fast as possible!"
    else:
        if listLen < (memory["quoteNum"] + 5):
             quotesLeft = listLen - memory["quoteNum"]
             added_title = "   Attention: Only " + str(quotesLeft) + " love quotes left!"
        encrypted_loveQuote = quoteList[memory["quoteNum"]]
        memory["quoteNum"] += 1
        loveQuote = crypt.decrypt(encrypted_loveQuote, 2334)

    #saves the quotenum and date for the nextquote in the memoryfile
    with open(memory_fileName, "w", encoding="utf-8") as file:
            json.dump(memory, file)

#check lovequote length and add \n to it
if len(loveQuote) > 80:
     firstString = loveQuote[:70]
     lastString = loveQuote[70:]
     loveQuote = firstString + "\n" + lastString



# Create a window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Custom pop-up with large font
popup = tk.Toplevel()
popup.title("💖Your daily love quote <3💖" + added_title)

popup.minsize(400, 350)

# Create a label with large font
label = tk.Label(popup, text= loveQuote, font=("Arial", 22, "bold"))
label.pack(padx=20, pady=20)

# Auto-resize window based on content
popup.update_idletasks()  # Apply pending geometry changes
popup_width = popup.winfo_reqwidth()
popup_height = popup.winfo_reqheight()

# Center the window on the screen
screen_width = popup.winfo_screenwidth()
screen_height = popup.winfo_screenheight()
x_position = (screen_width // 2) - (popup_width // 2)
y_position = (screen_height // 2) - (popup_height // 2)

popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")

# Close button
button = tk.Button(popup, text="<3", command=root.destroy, font=("Arial", 20))
button.pack(pady=10)

#Update text information for version
updateLabel = tk.Label(popup, text=updateText, font=("Arial", fontSize))
updateLabel.pack(pady=10)

# update button
updateButton = tk.Button(popup, text="Update to latest verison", command=git_pull, font=("Arial", 20))
if buttonVisible:
    updateButton.pack(pady=10)

popup.mainloop()


