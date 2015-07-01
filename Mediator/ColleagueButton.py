from tkinter import *
import Colleague

class ColleagueButton(Button):
    def __init__(self, root, caption):
        Button.__init__(self, root, text=caption)
    def set_mediator(self, mediator):
        self.mediator = mediator
    def set_colleague_enabled(self, enabled):
        self.configure(state=enabled)
