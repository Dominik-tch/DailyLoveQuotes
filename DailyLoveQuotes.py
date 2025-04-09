import json
import encrypting_tests as crypt
import os
import sys
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import subprocess
import requests

#check current version
result = subprocess.run(["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE)
print("Current Version:")
print(result.stdout.decode("utf-8").strip())

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
        with open("QuoteList.json", "r", encoding="utf-8") as file:
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

# Create a window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Custom pop-up with large font
popup = tk.Toplevel()
popup.title("💖Your daily love quote <3💖" + added_title)

popup.minsize(400, 250)

# Create a label with large font
label = tk.Label(popup, text= loveQuote, font=("Arial", 26, "bold"))
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

popup.mainloop()


