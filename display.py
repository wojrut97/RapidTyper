import curses
from curses import textpad

class Display:
    def __init__(self):
        self.width = 100
        self.height = 40
        self.stdscr = curses.initscr()

        #Empty initialization of window instances
        self.menu_window = 0
        self.menu_select_window = 0
        self.level_selection_window = 0

        self.levels = [1,2,3]

        self.setup()
        self.main_menu()

    def setup(self):
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        if curses.has_colors():
            curses.start_color()

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

        self.main_window = curses.newwin(curses.LINES-2, curses.COLS, 1, 0)

        
    
    def main_menu(self):
        self.menu_select_window = self.main_window.subwin(curses.LINES-6, curses.COLS-4, 3,2)
        self.menu_select_window.box()

        self.menu_select_window.addstr(1,2,"1 - Choose Level")
        self.menu_select_window.addstr(2,2,"Q - Quit")
        self.stdscr.noutrefresh()
        self.menu_select_window.noutrefresh()
        curses.doupdate()

    def selection_menu(self):
        self.menu_select_window.clear()
        #TODO: autowyświetlanie leveli w zaleznosci od zawartosci jsona i tego ile tych lvli tam w ogóle jest
        #self.levels jest na ten moment tylko pomocnicze
        for level in self.levels:
            self.menu_select_window.addstr(level, 0, str(level) + ". Level")
        self.menu_select_window.noutrefresh()
        curses.doupdate()
