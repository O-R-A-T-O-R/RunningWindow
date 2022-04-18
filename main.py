from tkinter import *
from utils import *
import random


class App(Tk):
    __width__ = 250
    __height__ = 250
    __indent__ = 25
    __attempts__ = 0

    def __init__(self):
        super().__init__()

        self.geometry(
            f'{self.__width__}x{self.__height__}+{self.__indent__}+{self.__indent__}')

        l1 = Label(text="[ ^_^ ]",
                   font="Arial 20")

        l1.pack(pady=100)

        # remove ability to close the window (all top taskbar)
        self.overrideredirect(1)

        # set window in front of the all apps
        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(self.attributes, '-topmost', True)

        self.bind('<Enter>', self.run_away)

    def change_position(self, x, y):
        self.geometry(f'+{x}+{y}')

    def run_away(self, event):
        """ Run away if cursor pointer on the window"""

        size, x, y = self.geometry().split('+')
        x, y = int(x), int(y)

        x_mid, y_mid = 1920 // 2, 1080 // 2

        y = random.randint(500, 850) if y < y_mid else random.randint(0, 300)
        x = random.choice([random.randint(0, 350), random.randint(800, 1300)])

        self.change_position(x, y)
        self.__attempts__ += 1

        if self.__attempts__ % 5 == 0:
            # create a new app))()()()())))
            new_app = App()
            new_app.mainloop()

        print('I RUN AWAY !!! [', x, y, ']')


if __name__ == '__main__':
    app = App()
    app.mainloop()
