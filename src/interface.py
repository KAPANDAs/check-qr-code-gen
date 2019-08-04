import tkinter
from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import Entry


class UserInterface:
    """
    User interface class
    """

    def __init__(self):
        """
        Initialisation of user interface
        """
        self.window = Tk()
        self.window.title("Creating QR from checks")
        self.window.geometry("400x400")
        self.window.wm_resizable(False, False)

        self.labelText = Label(self.window, text="FN:")
        self.labelText.grid(column=0, row=0)

        self.textInput = Entry(self.window)
        self.textInput.grid(column=1, row=0)

        self.buttonSend = Button(
            self.window, text="SEND", command=self.buttonSendClicked
        )
        self.buttonSend.grid(column=0, row=1)
        # EXECUTING INTERFACE
        self.window.mainloop()

    def buttonSendClicked(self):
        print(self.textInput.get())
