from level import Level
from input_validator import InputValidator
import curses
from curses import wrapper
from display import Display



def main():
    level = Level()
    input_validator = InputValidator()
    display = Display()

    while(True):
        c = display.menu_select_window.getch()

        if c == ord('1'):
            display.selection_menu()


        elif c == ord('q') or c == ord('Q'):
            break

        display.stdscr.noutrefresh()
        display.menu_select_window.noutrefresh()
        display.main_window.noutrefresh()
        curses.doupdate()

    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)

    curses.endwin()


        


if __name__ == "__main__":
    main()