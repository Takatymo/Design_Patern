from tkinter import *
import Colleague

class ColleagueTextField(Text):
    def __init__(self, root, columns):
        Text.__init__(self, root, height=columns)
        self.bind('<<Change>>', self.text_value_changed())
    def set_mediator(self, mediator):
        self.mediator = mediator
    def set_colleague_enabled(self, enabled):
        self.configure(state=enabled)
    def text_value_changed(self):
        self.mediator.colleague_changed()