import pyautogui
from time import sleep
from scraper import lyrics, lyriccheck
from tkinter import *
from tkinter import messagebox


# get position of spotify window on screen
# position = pyautogui.locateCenterOnScreen("search.png")
# # while position == None:
# #     position = pyautogui.locateCenterOnScreen("Capture.png")
# print(position, "yoy")

class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('%dx%d+%d+%d' % (25, 25, 694, 1005))
        self.root.overrideredirect(1)
        self.root.attributes("-topmost", True)
        self.img = PhotoImage(file="cover.png")
        self.img2 = PhotoImage(file="lyricalgenius.png")
        self.frame = Frame(self.root, width=25, height=50, bg="black",
                           borderwidth=0, relief=RAISED)
        self.frame.pack_propagate(False)
        self.frame.grid()
        self.toggle_lyrics = False
        self.blyrics = Button(self.frame, image=self.img2, fg="white",bg="black", borderwidth=0,
                            command=self.lyrics_show)
        self.blyrics.grid(column=2, row=1, sticky="N")
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
            self.newWindow.geometry('%dx%d+%d+%d' % (500, 300, 1400, 700))
            self.newWindow.overrideredirect(1)
            self.newWindow.attributes("-topmost", True)
            frame = Frame(self.newWindow, width=500, height=300, bg="black",
                        borderwidth=0, relief=RAISED)
            frame.pack_propagate(False)
            frame.pack()
            grip = Label(frame, bitmap="gray25")
            grip.pack(side=TOP)
            T = Text(frame, height=833, width =500, font=("Gotham-Bold", 12), bg="black", fg="white")


            T.insert(END,lyrics)
            T.tag_add("center", "1.0", "end")
            T.pack(side=LEFT)
            scroll_bar = Scrollbar(frame,
                                   orient=VERTICAL).pack(side=RIGHT,fill=Y)
            self.label = Label(frame, text="Click on the grip to move")

            self.label.pack(side="right", fill="both", expand=True)

            grip.bind("<ButtonPress-1>", self.start_move)
            grip.bind("<ButtonRelease-1>", self.stop_move)
            grip.bind("<B1-Motion>", self.do_move)

        else:
            self.newWindow.destroy()
            self.toggle_lyrics = False


    def start_move(self, event):
        self.x = event.x
        self.y = event.y


    def stop_move(self, event):
        self.x = None
        self.y = None


    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.newWindow.winfo_x() + deltax
        y = self.newWindow.winfo_y() + deltay
        self.newWindow.geometry(f"+{x}+{y}")

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()



app = App()
app.root.mainloop()
