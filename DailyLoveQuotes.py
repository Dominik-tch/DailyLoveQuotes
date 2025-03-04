import json
import os
import sys
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
memory_fileName = "Memory.json"
memory = {"days": "", "quoteNum":""}

#Generate a Memory.json file to store information about already used quotes and days

if os.path.exists(memory_fileName):
    with open("QuoteList.json", "r", encoding="utf-8") as file:
            memory = json.load(file)
else:    
    with open(memory_fileName, "w", encoding="utf-8") as file:
        json.dump(memory, file)


current_date = datetime.now().date()




if memory["days"] == current_date:
      sys.exit()
else:
      memory["days"] = current_date





try:
    with open("QuoteList.json", "r", encoding="utf-8") as file:
            quoteList = json.load(file)
except:
      raise ValueError("Coud not open the QuoteList.json Check if it exits in the same directory (DailyLoveQuotes)")


# Create a window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Custom pop-up with large font
popup = tk.Toplevel()
popup.title("Your daily love quote <3")

popup.minsize(400, 200)

# Create a label with large font
label = tk.Label(popup, text= loveQuote, font=("Arial", 40, "bold"))
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
button = tk.Button(popup, text="OK", command=root.destroy, font=("Arial", 20))
button.pack(pady=10)

popup.mainloop()


