import pyautogui
from time import sleep
from scraper import lyrics, lyriccheck
from tkinter import *
from tkinter import messagebox


# get position of spotify window on screen
position = pyautogui.locateCenterOnScreen("search.png")
while position == None:
    position = pyautogui.locateCenterOnScreen("useless.png")


class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('%dx%d+%d+%d' % (390, 50, position.x - 88, position.y - 15))
        self.root.overrideredirect(1)
        self.img = PhotoImage(file="cover.png")
        self.frame = Frame(self.root, width=390, height=50, bg="black",
                           borderwidth=0, relief=RAISED)
        self.frame.pack_propagate(False)
        self.frame.grid()
        self.toggle_lyrics = False
        self.background = Label(self.frame, image=self.img, bg="black")
        self.background.grid(column=1, row=1)
        self.bQuit = Button(self.frame, text="Lyrics", fg="white",bg="black", borderwidth=0,
                            command=self.lyrics_show)
        self.bQuit.grid(column=2, row=1, sticky="N")
        # photo = PhotoImage(file="lyricalgenius.png")
        #
        # self.bHello = Button(self.frame, text="Lyrics",fg="Grey",
        #                      command=self.hello)
        # self.bHello.pack(pady=20, side=TOP)

    def lyrics_show(self):
        if self.toggle_lyrics == False:
            self.toggle_lyrics = True
            lyrics = lyriccheck()
            self.newWindow = Toplevel(self.root)
            self.newWindow.title("New Window")
            self.newWindow.geometry('%dx%d+%d+%d' % (480, 833, position.x-88, position.y+20))
            self.newWindow.overrideredirect(1)
            frame = Frame(self.newWindow, width=480, height=833, bg="black",
                        borderwidth=0, relief=RAISED)
            frame.pack_propagate(False)
            frame.pack()
            T = Text(frame, height=833, width =480, font=("Gotham-Bold", 12), bg="black", fg="white")
            T.pack(side=LEFT)
            T.insert(END,lyrics)
            scroll_bar = Scrollbar(frame,
                                   orient=VERTICAL).pack(side=RIGHT,fill=Y)
        else:
            self.newWindow.destroy()
            self.toggle_lyrics = False

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

app = App()
app.root.mainloop()
