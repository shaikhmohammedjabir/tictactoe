import tkinter


class Code:
    def __init__(self):
        width = 10
        height = 5
        self.number = 1
        self.playeronename = 'playerone'
        self.playertwoname = 'playertwo'
        self.p1flag = False
        self.p2flag = False
        self.colorone = 'red'
        self.colortwo = 'green'

        window = tkinter.Tk()
        window.geometry('600x300')
        window.resizable(False, False)
        window.title("CLASSIC TIC-TAC-TOE")
        img = tkinter.PhotoImage(file='logo/tic.png')
        window.iconphoto(False, img)

        self.one = tkinter.Button(window, width=width, height=height)
        self.one.bind('<Button-1>', lambda x: self.assignColor(self.one))
        self.one.bind('<space>', lambda x: self.assignColor(self.one))
        self.one.bind('<Return>', lambda x: self.assignColor(self.one))
        self.one.bind('<KP_Enter>', lambda x: self.assignColor(self.one))
        self.one.grid(row=0, column=0)

        self.two = tkinter.Button(window, width=width, height=height)
        self.two.bind('<Button-1>', lambda x: self.assignColor(self.two))
        self.two.bind('<space>', lambda x: self.assignColor(self.two))
        self.two.bind('<Return>', lambda x: self.assignColor(self.two))
        self.two.bind('<KP_Enter>', lambda x: self.assignColor(self.one))
        self.two.grid(row=0, column=1)

        self.three = tkinter.Button(window, width=width, height=height)
        self.three.bind('<Button-1>', lambda x: self.assignColor(self.three))
        self.three.bind('<space>', lambda x: self.assignColor(self.three))
        self.three.bind('<Return>', lambda x: self.assignColor(self.three))
        self.three.bind('<KP_Enter>', lambda x: self.assignColor(self.three))
        self.three.grid(row=0, column=2)

        self.four = tkinter.Button(window, width=width, height=height)
        self.four.bind('<Button-1>', lambda x: self.assignColor(self.four))
        self.four.bind('<space>', lambda x: self.assignColor(self.four))
        self.four.bind('<Return>', lambda x: self.assignColor(self.four))
        self.four.bind('<KP_Enter>', lambda x: self.assignColor(self.four))
        self.four.grid(row=1, column=0)

        self.five = tkinter.Button(window, width=width, height=height)
        self.five.bind('<Button-1>', lambda x: self.assignColor(self.five))
        self.five.bind('<space>', lambda x: self.assignColor(self.five))
        self.five.bind('<Return>', lambda x: self.assignColor(self.five))
        self.five.bind('<KP_Enter>', lambda x: self.assignColor(self.five))
        self.five.grid(row=1, column=1)

        self.six = tkinter.Button(window, width=width, height=height)
        self.six.bind('<Button-1>', lambda x: self.assignColor(self.six))
        self.six.bind('<space>', lambda x: self.assignColor(self.six))
        self.six.bind('<Return>', lambda x: self.assignColor(self.six))
        self.six.bind('<KP_Enter>', lambda x: self.assignColor(self.six))
        self.six.grid(row=1, column=2)

        self.seven = tkinter.Button(window, width=width, height=height)
        self.seven.bind('<Button-1>', lambda x: self.assignColor(self.seven))
        self.seven.bind('<space>', lambda x: self.assignColor(self.seven))
        self.seven.bind('<Return>', lambda x: self.assignColor(self.seven))
        self.seven.bind('<KP_Enter>', lambda x: self.assignColor(self.seven))
        self.seven.grid(row=2, column=0)

        self.eight = tkinter.Button(window, width=width, height=height)
        self.eight.bind('<Button-1>', lambda x: self.assignColor(self.eight))
        self.eight.bind('<space>', lambda x: self.assignColor(self.eight))
        self.eight.bind('<Return>', lambda x: self.assignColor(self.eight))
        self.eight.bind('<KP_Enter>', lambda x: self.assignColor(self.eight))
        self.eight.grid(row=2, column=1)

        self.nine = tkinter.Button(window, width=width, height=height)
        self.nine.bind('<Button-1>', lambda x: self.assignColor(self.nine))
        self.nine.bind('<space>', lambda x: self.assignColor(self.nine))
        self.nine.bind('<Return>', lambda x: self.assignColor(self.nine))
        self.nine.bind('<KP_Enter>', lambda x: self.assignColor(self.nine))
        self.nine.grid(row=2, column=2)

        tkinter.Label(window, text="player 1 name").place(x=330, y=0)
        self.playerone = tkinter.Entry(window, bg='yellow', highlightcolor='green')
        self.playerone.bind('<FocusOut>', lambda x: self.authenticatePlayer(self.playerone))
        self.playerone.place(x=430, y=0)

        tkinter.Label(window, text="player 2 name").place(x=330, y=30)
        self.playertwo = tkinter.Entry(window, bg='yellow', highlightcolor='green')
        self.playertwo.bind('<FocusOut>', lambda x: self.authenticatePlayer(self.playertwo))
        self.playertwo.place(x=430, y=30)

        self.playeronebutton = tkinter.Button(window,text=self.playeronename,width=width,height=height)
        self.playeronebutton.place(x=342, y=100)
        self.playertwobutton = tkinter.Button(window,text=self.playertwoname,width=width,height=height)
        self.playertwobutton.place(x=461, y=100)

        rst = tkinter.Button(window, text='reset', bg='yellow', activebackground='yellow')
        rst.bind('<Button-1>', lambda x: self.reset())
        rst.bind('<space>', lambda x: self.reset())
        rst.bind('<Return>', lambda x: self.reset())
        rst.bind('<KP_Enter>', lambda x: self.reset())
        rst.place(x=385, y=270)

        ext = tkinter.Button(window, text='exit', bg='red', activebackground='red')
        ext.bind('<Button-1>', lambda x: window.destroy())
        ext.bind('<space>', lambda x: window.destroy())
        ext.bind('<Return>', lambda x: window.destroy())
        ext.bind('<KP_Enter>', lambda x: window.destroy())
        ext.place(x=450, y=270)

        dev = tkinter.Button(window, text='developer', bg='green', activebackground='green')
        dev.bind('<Button-1>', lambda x: self.devInfo())
        dev.bind('<space>', lambda x: self.devInfo())
        dev.bind('<Return>', lambda x: self.devInfo())
        dev.bind('<KP_Enter>', lambda x: self.devInfo())
        dev.place(x=505, y=270)

        window.mainloop()

    def checkCondition(self):
        if self.one['background'] == self.colorone and self.two['background'] == self.colorone and self.three[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.one['background'] == self.colortwo and self.two['background'] == self.colortwo and self.three[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()
        elif self.four['background'] == self.colorone and self.five['background'] == self.colorone and self.six[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.four['background'] == self.colortwo and self.five['background'] == self.colortwo and self.six[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()
        elif self.seven['background'] == self.colorone and self.eight['background'] == self.colorone and self.nine[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.seven['background'] == self.colortwo and self.eight['background'] == self.colortwo and self.nine[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()
        elif self.one['background'] == self.colorone and self.four['background'] == self.colorone and self.seven[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.one['background'] == self.colortwo and self.four['background'] == self.colortwo and self.seven[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()
        elif self.two['background'] == self.colorone and self.five['background'] == self.colorone and self.eight[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.two['background'] == self.colortwo and self.five['background'] == self.colortwo and self.eight[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()
        elif self.three['background'] == self.colorone and self.six['background'] == self.colorone and self.nine[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.three['background'] == self.colortwo and self.six['background'] == self.colortwo and self.nine[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()
        elif self.one['background'] == self.colorone and self.five['background'] == self.colorone and self.nine[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.one['background'] == self.colortwo and self.five['background'] == self.colortwo and self.nine[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()
        elif self.three['background'] == self.colorone and self.five['background'] == self.colorone and self.seven[
            'background'] == self.colorone:
            self.p1flag = True
            self.winner()
        elif self.three['background'] == self.colortwo and self.five['background'] == self.colortwo and self.seven[
            'background'] == self.colortwo:
            self.p2flag = True
            self.winner()

    def authenticatePlayer(self, entry):
        if len(entry.get()) < 3:
            entry.configure(bg='red')
        else:
            if entry['bg'] == 'red':
                entry.configure(bg='white')

    def assignColor(self, button):
        if button['background'] == self.colorone or button['background'] == self.colortwo:
            pass
        else:
            if self.number == 1:
                if len(self.playerone.get()) >= 1:
                    self.playeronename = self.playerone.get()
                if len(self.playertwo.get()) >= 1:
                    self.playertwoname = self.playertwo.get()
                self.playeronebutton.configure(text=self.playeronename,bg=self.colorone,activebackground=self.colorone)
                self.playertwobutton.configure(text=self.playertwoname,bg=self.colortwo,activebackground=self.colortwo)
            if self.number % 2 == 0:
                button.configure(background=self.colortwo, activebackground=self.colortwo)
            else:
                button.configure(background=self.colorone, activebackground=self.colorone)
            self.number += 1
        self.checkCondition()

    def winner(self):
        playeronecount = 0
        playertwocount = 0
        for button in [self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight,
                       self.nine]:
            if button['background'] == self.colorone:
                playeronecount += 1
            elif button['background'] == self.colortwo:
                playertwocount += 1
        window = tkinter.Tk()
        window.geometry('400x150')
        window.resizable(False, False)
        window.title('WINNER SCORE CARD')
        if self.p1flag:
            window.configure(background=self.colorone)
            tkinter.Label(window,
                          text=f"!!!CONGRATULATION {self.playeronename.upper()}\n*************you win************",
                          bg=self.colorone, font=('', 16)).pack()
            tkinter.Label(window,
                          text=f"SCORE : \n{self.playeronename} : {playeronecount}\n{self.playertwoname} : {playertwocount}",
                          bg=self.colorone).pack()
            tkinter.Label(window, text='-----------------------------', bg=self.colorone, font=('', 16)).pack()
            self.reset()
        elif self.p2flag:
            window.configure(background=self.colortwo)
            tkinter.Label(window,
                          text=f"!!!CONGRATULATION {self.playertwoname.upper()}\n*************you win************",
                          bg=self.colortwo, font=('', 16)).pack()
            tkinter.Label(window,
                          text=f"SCORE : \n{self.playertwoname} : {playertwocount}\n{self.playeronename} : {playeronecount}",
                          bg=self.colortwo).pack()
            tkinter.Label(window, text='-----------------------------', bg=self.colortwo, font=('', 16)).pack()
            self.reset()
        window.mainloop()

    def reset(self):
        self.number = 1
        self.playeronename = 'playerone'
        self.playertwoname = 'playertwo'
        self.p1flag = False
        self.p2flag = False
        for button in [self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight,
                       self.nine,self.playeronebutton,self.playertwobutton]:
            button.configure(bg='#d9d9d9', activebackground='#d9d9d9', text='')

    def devInfo(self):
        window = tkinter.Tk()
        window.geometry('400x150')
        window.resizable(False, False)
        window.title('SHAIKH JABIR MOHAMMED')
        msg = ''
        lion = [82, 65, 74, 68, 72, 65, 78, 73, 32, 69, 78, 71, 73, 78, 69, 69, 82, 73, 78, 71, 32, 67, 79, 76, 76, 69,
                71, 69, 10, 32, 32, 32, 32, 32, 32, 32, 32, 110, 97, 109, 101, 32, 32, 32, 58, 32, 115, 104, 97, 105,
                107, 104, 32, 106, 97, 98, 105, 114, 32, 109, 111, 104, 97, 109, 109, 101, 100, 10, 32, 32, 32, 32, 32,
                32, 32, 32, 114, 111, 108, 108, 32, 32, 32, 58, 32, 49, 56, 50, 49, 50, 57, 52, 51, 49, 52, 10, 32, 32,
                32, 32, 32, 32, 32, 32, 98, 114, 97, 110, 99, 104, 32, 58, 32, 66, 46, 84, 101, 99, 104, 10, 32, 32, 32,
                32, 32, 32, 32, 32, 109, 111, 98, 105, 108, 101, 32, 58, 32, 55, 56, 55, 51, 57, 50, 52, 53, 50, 51, 44,
                32, 57, 51, 51, 55, 54, 57, 52, 48, 49, 57, 10, 10, 32, 32, 32, 32, 32, 32, 32, 32, 79, 85, 82, 32, 72,
                79, 68, 32, 58, 32, 68, 114, 46, 32, 85, 116, 116, 97, 109, 32, 115, 105, 114, 44]
        for i in lion:
            msg += chr(i)
        tkinter.Label(window, text=msg, fg='green').pack()
        tkinter.Button(window, text='close', command=lambda: window.destroy()).pack()
        window.mainloop()


if __name__ == '__main__':
    Code()
