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
        self.height = "80"
        self.geometry("240x" + self.height)
        self.resizable(False, False)

        self._user_input = []
        self.error_one = None

        self.vote_label = tkinter.Label(self, text="Vote")
        self.vote_label.grid(row=2, column=0, pady=10)
        self._vote_selection = tkinter.StringVar()
        for vote in self.VOTE_OPTIONS:
            (tkinter.ttk.Radiobutton(text=vote, variable=self._vote_selection, value=vote)
             .grid(row=0, column=self.VOTE_OPTIONS.index(vote) + 1, pady=10))

        self.save = tkinter.ttk.Button(self, text="ENTER", command=self.refresh)
        self.save.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    def refresh(self) -> None:
        """
        Reload window after selecting the "Enter" button
        """
        try:
            self.error_one.destroy()
        except AttributeError:
            pass  # ignore, if error DNE

        if self._vote_selection.get() == "nan" or self._vote_selection.get() == "":
            if self.height != "120":
                self.height = "120"
                self.geometry("240x" + self.height)

            self.error_one = tkinter.Label(self, text="No selection made; please try again.")
            self.error_one.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
        else:
            if self.height != "80":
                self.height = "80"
                self.geometry("240x" + self.height)
            self._user_input.append(self.get_vote())

        self._vote_selection.set("nan")

    def get_vote(self) -> str:
        """
        Get data from the Grade entry
        :return: candidate, else "nan" if no value is selected
        """
        if self._vote_selection.get() != "None":
            return self._vote_selection.get()
        else:
            return "nan"

    def get_user_input(self) -> list:
        """
        :return: List[] containing all the votes made
        """
        return self._user_input
