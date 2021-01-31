from tkinter import *
from StockItem import *

window = Tk()
window.geometry("350x350")
window.title("Add a stock item to the server")

mainFrame = Frame(window)
mainFrame.place(x = 0, y = 0, width = 200, height = 100)



code_label = Label(mainFrame, text = "Code: ")
description_label = Label(mainFrame, text = "Description: ")
amount_label = Label(mainFrame, text = "Amount: ")



code_label.place(x = 0, y = 0)
description_label.place(x = 0, y = 20)
amount_label.place(x = 0, y = 40)


code_entry = Entry(mainFrame)
code_entry.place(x= 80, y = 0)

description_entry = Entry(mainFrame)
description_entry.place(x = 80, y = 20)

amount_entry = Entry(mainFrame)
amount_entry.place(x = 80, y = 40)

def entry_fields(): #Function that gets input from app and places 
    test = StockTracker(code_entry.get(), description_entry.get(), amount_entry.get())
    test.Add_StockItem()



button = Button(text = "Submit", command = entry_fields) #button executes entry_fields() on click
button.place(x= 150, y = 60)






window.mainloop()