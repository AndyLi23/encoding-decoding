from tkinter import *
from tkinter.ttk import Combobox

from base64_functions import *
class app:
    def __init__(self):
        def computeClicked():
            if edChoose.get() == "Encode":
                ans.delete("1.0", END)
                ans.insert(END, encodeBase64(input.get()))
            elif edChoose.get() == "Decode":
                ans.delete("1.0", END)
                ans.insert(END, decodeBase64(input.get()))
            else:
                ans.delete("1.0", END)
                ans.insert(END, "Invalid")

        myApp = Tk()
        myApp.title("Codec")
        myApp.geometry("800x600")

        input = Entry(myApp, width = 30)
        input.pack(anchor = "nw", padx = 20, pady = 10)

        edChoice = ['Encode', 'Decode']
        edChoose = Combobox(myApp, values = edChoice, width=10, state="readonly")
        edChoose.pack(anchor = "nw", padx = 20, pady = 0)

        typeChoices = ['base64']
        typeChoose = Combobox(myApp, values = typeChoices, width=10, state="readonly")
        typeChoose.pack(anchor = "nw", padx = 20, pady = 0)

        compute = Button(myApp, text = "Go", command = computeClicked)
        compute.pack(anchor = "nw", padx = 20, pady = 10)

        ans = Text(myApp)
        ans.pack(anchor="nw", padx = 20, pady = 0)

        myApp.mainloop()


app()