from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog

from base64_functions import *
from vigenere_functions import *
from caesar_functions import *

class app:
    file = None
    def __init__(self):
        def chooseFileClicked():
            self.file = filedialog.askopenfilename(initialdir="/Users/~", title="Select file",
                                                        filetypes=(("text files", "*.txt"), ("all files", "*.*")))

            if self.file:
                fileName.configure(text=self.file)


        def computeClicked():
            if self.file:
                with open(self.file, "r") as f:
                    i = f.read()
                self.file = None
                fileName.configure(text="")
            else:
                i = input.get()

            if edChoose.get() == "Encode":
                if typeChoose.get() == "base64":
                    ans.delete("1.0", END)
                    ans.insert(END, encodeBase64(i))
                elif typeChoose.get() == "vigenere" and key.get() != "":
                    ans.delete("1.0", END)
                    ans.insert(END, encodeVigenere(i, key.get()))
                elif typeChoose.get() == 'caesars' and key.get().isdigit():
                    ans.delete("1.0", END)
                    ans.insert(END, encodeCaesar(i, int(key.get())))
                else:
                    ans.delete("1.0", END)
                    ans.insert(END, "Invalid")

            elif edChoose.get() == "Decode":
                if typeChoose.get() == "base64":
                    ans.delete("1.0", END)
                    ans.insert(END, decodeBase64(i))
                elif typeChoose.get() == "vigenere" and key.get() != "":
                    ans.delete("1.0", END)
                    ans.insert(END, decodeVigenere(i, key.get()))
                elif typeChoose.get() == 'caesars' and key.get().isdigit():
                    ans.delete("1.0", END)
                    ans.insert(END, decodeCaesar(i, int(key.get())))
                else:
                    ans.delete("1.0", END)
                    ans.insert(END, "Invalid")

            else:
                ans.delete("1.0", END)
                ans.insert(END, "Invalid")

        myApp = Tk()
        myApp.title("Codec")
        myApp.geometry("400x300")

        chooseFileButton = Button(myApp, text = "Choose File", command = lambda:chooseFileClicked())
        chooseFileButton.pack(anchor="nw", padx=20, pady=10)

        fileName = Label(myApp)
        fileName.pack(anchor="nw", padx=20, pady=0)

        input = Entry(myApp, width=30)
        input.pack(anchor="nw", padx=20, pady=10)

        edChoice = ['Encode', 'Decode']
        edChoose = Combobox(myApp, values=edChoice, width=10, state="readonly")
        edChoose.pack(anchor="nw", padx=20, pady=0)

        typeChoices = ['base64', 'vigenere', 'caesars']
        typeChoose = Combobox(myApp, values=typeChoices, width=10, state="readonly")
        typeChoose.pack(anchor="nw", padx=20, pady=0)

        key = Entry(myApp, width=10)
        key.pack(anchor="nw", padx=20, pady=5)

        compute = Button(myApp, text="Go", command=computeClicked)
        compute.pack(anchor="nw", padx=20, pady=5)

        ans = Text(myApp)
        ans.pack(anchor="nw", padx=20, pady=0)

        myApp.mainloop()


app()
