from tkinter import *
import Colleague

class ColleagueCheckbox(Checkbutton):
    def __init__(self, root, caption, state):
        Checkbutton.__init__(self, root, text=caption, variable=state)
        self.bind('<<Change>>', self.item_state_changed())
    def set_mediator(self, mediator):
        self.mediator = mediator
    def set_colleague_enabled(self, enabled):
        self.configure(state=enabled)
    def item_state_changed(self):
        self.mediator.colleague_changed()