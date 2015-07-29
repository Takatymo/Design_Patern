from tkinter import *
from abc import ABCMeta, abstractmethod




class ColleagueCheckbox(Checkbutton):
    def __init__(self, root, caption, state):
        Checkbutton.__init__(self, root, text=caption, variable=state)

    def set_mediator(self, mediator):
        self.mediator = mediator

    def set_colleague_enabled(self, enabled):
        self.configure(state=enabled)

    def item_state_changed(self, event):
        self.mediator.colleague_changed()




class ColleagueButton(Button):
    def __init__(self, root, caption):
        Button.__init__(self, root, text=caption)
    def set_mediator(self, mediator):
        self.mediator = mediator
    def set_colleague_enabled(self, enabled):
        self.configure(state=enabled)

class ColleagueTextField(Text):
    def __init__(self, root, columns):
        Text.__init__(self, root, height=columns)
    def set_mediator(self, mediator):
        self.mediator = mediator

    def set_colleague_enabled(self, enabled):
        self.configure(state=enabled)
        self.configure(bg = 'white' if enabled=='normal' else 'lightGray')

    def text_value_changed(self, event):
        self.mediator.colleague_changed()

class LoginFrame(Frame):
    def __init__(self, title, master=None):

        Frame.__init__(self, master, bg='lightGray')
        self.master.title(title)
        self.pack()

        self.create_colleagues()
        self.colleague_changed()
        self.check_guest.grid(row=0, column=1)
        self.check_login.grid(row=0, column=2)
        Label(self, text='Username:').grid(row=1, column=1)
        self.text_user.grid(row=1, column=2)
        Label(self, text='Password:').grid(row=2, column=1)
        self.text_pass.grid(row=2, column=2)
        self.button_ok.grid(row=3, column=1)
        self.button_cancel.grid(row=3, column=2)


    def create_colleagues(self):
        self.guest_var = BooleanVar(value=False)
        self.login_var = BooleanVar(value=True)
        self.check_guest = ColleagueCheckbox(self, 'Guest', self.guest_var)
        self.check_login = ColleagueCheckbox(self, 'Login', self.login_var)
        self.text_user = ColleagueTextField(self, 10)
        self.text_pass = ColleagueTextField(self, 10)
        self.button_ok = ColleagueButton(self, 'OK')
        self.button_cancel = ColleagueButton(self, 'Cancel')

        self.check_guest.set_mediator(self)
        self.check_login.set_mediator(self)
        self.text_user.set_mediator(self)
        self.text_pass.set_mediator(self)
        self.button_ok.set_mediator(self)
        self.button_cancel.set_mediator(self)


        self.check_guest.bind('<Button-1>', self.check_guest.item_state_changed)
        self.check_login.bind('<Button-1>', self.check_login.item_state_changed)
        self.text_user.bind('<KeyRelease>', self.text_user.text_value_changed)
        self.text_pass.bind('<KeyRelease>', self.text_pass.text_value_changed)

    def colleague_changed(self):
        if self.guest_var.get():
            self.text_user.set_colleague_enabled('disabled')
            self.text_pass.set_colleague_enabled('disabled')
            self.button_ok.set_colleague_enabled('normal')
        else:
            self.text_user.set_colleague_enabled('normal')
            self._userpass_changed()

    def _userpass_changed(self):
        if len(self.text_user.get("1.0",END))-1:
            self.text_pass.set_colleague_enabled('normal')
            if len(self.text_pass.get("1.0",END))-1:
                self.button_ok.set_colleague_enabled('normal')
            else:
                self.button_ok.set_colleague_enabled('disabled')
        else:
            self.text_pass.set_colleague_enabled('disabled')
            self.button_ok.set_colleague_enabled('disabled')

if __name__=='__main__':
    frame = LoginFrame('Mediator Sample')
    frame.mainloop()
