import tkinter
from tkinter import ttk


class GUI(tkinter.Tk):
    def __init__(self, options) -> None:
        """
        Voter GUI framework & landing page
        """
        super().__init__()
        self.VOTE_OPTIONS = options

        self.title("CSCI 1620- Project 1")
        self.height = "320"
        self.geometry("220x" + self.height)
        self.resizable(False, False)

        self._user_input = []
        self.error = None

        self.vote_header = tkinter.Label(self, text="VOTING APPLICATION")
        self.vote_header.grid(row=0, column=1, padx=20, pady=10)

        self.id_label = tkinter.Label(self, text="ID")
        self.id_label.grid(row=1, column=0, padx=10, pady=10)
        self.id = tkinter.StringVar(self)
        self.id_entry = tkinter.ttk.Entry(self, textvariable=self.id)
        self.id_entry.grid(row=1, column=1, columnspan=1)

        self.vote_label = tkinter.Label(self, text="CANDIDATES")
        self.vote_label.grid(row=3, column=1, pady=10)
        self._vote_selection = tkinter.StringVar()
        for vote in self.VOTE_OPTIONS:
            (tkinter.ttk.Radiobutton(text=vote, variable=self._vote_selection, value=vote)
             .grid(row=self.VOTE_OPTIONS.index(vote) + 4, column=1, pady=10))

        self.save = tkinter.ttk.Button(self, text="SUBMIT VOTE", command=self.refresh)
        self.save.grid(row=7, column=1, columnspan=4, padx=10, pady=10)

    def refresh(self) -> None:
        """
        Reload window after selecting the "Enter" button
        """
        try:  # clear error, if present
            self.error.destroy()
        except AttributeError:
            pass

        if self.valid_input():
            if self.height != "320":
                self.height = "320"
                self.geometry("220x" + self.height)
            self._user_input.append([self.get_id(), self.get_vote()])

        self.id_entry.delete(0, tkinter.END)
        self._vote_selection.set("nan")

    def valid_input(self):
        if self.get_id() == "nan":
            if self.height != "340":
                self.height = "340"
                self.geometry("220x" + self.height)

            self.error = tkinter.Label(self, text="No ID entry; please try again.")
            self.error.config(fg="#ED7117")
            self.error.grid(row=8, column=0, columnspan=4, padx=10, pady=10)
            return False
        if self.get_id() == "invalid":
            if self.height != "340":
                self.height = "340"
                self.geometry("220x" + self.height)

            self.error = tkinter.Label(self, text="Duplicate ID; please try again.")
            self.error.config(fg="#FF69B4")
            self.error.grid(row=8, column=0, columnspan=4, padx=10, pady=10)
            return False
        elif self.get_vote() == "nan":
            if self.height != "340":
                self.height = "340"
                self.geometry("220x" + self.height)

            self.error = tkinter.Label(self, text="No vote cast; please try again.")
            self.error.config(fg="#D74826")
            self.error.grid(row=8, column=0, columnspan=4, padx=10, pady=10)
            return False
        else:
            return True

    def get_id(self):
        """
        Get data from the ID entry
        :return: ID, else "nan" if no value is selected
        """
        if self.id.get() == "":
            return "nan"
        else:
            for entry in self._user_input:
                if entry[0] == self.id.get():
                    return "invalid"

            return self.id.get()

    def get_vote(self) -> str:
        """
        Get data from the Vote entry
        :return: candidate, else "nan" if no value is selected
        """
        if self._vote_selection.get() == "None":
            return "nan"
        else:
            return self._vote_selection.get()

    def get_user_input(self) -> list:
        """
        :return: List[] containing all the votes made
        """
        return self._user_input
