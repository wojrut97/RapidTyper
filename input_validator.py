from pynput import keyboard
import colorama
import sys, time
import colors
import readchar

write = sys.stdout.write


class InputValidator():
    def __init__(self):
        colorama.init()
        self.user_input_list = []
        self.template_string = ""
        self.user_input_str = ""

#    POZDRO MARCIN MORDECZKO!!!

    def get_key(self, stdscr):
        c = stdscr.getkey()
        error = self.validate(c, stdscr)
        return error
   
    def validate(self, c, stdscr):
        if c == 'q':
            return 1    #quit
        elif c == '\n':
            pass
            # return 2  #pass
        elif c == "KEY_BACKSPACE":
            stdscr.delch(1, len(self.user_input_list)) # Usuwanie ostatniego znaku tak z listy jak i z konsoli
            if self.user_input_list:
                self.user_input_list.pop()
            stdscr.refresh()
            return 0
        else:
            self.user_input_list.append(c)  # Dodaje wpisany klawisz do listy i sprawdza czy zgadza sie z templatem
            if self.user_input_list[-1] == self.template_string[len(self.user_input_list) - 1]:
                stdscr.addch(c)  # wypisuje poprawny
            else:
                stdscr.standout()  # Wypisuje ze bledny
                stdscr.addch(c)
                stdscr.standend()
                #self.user_input_list.pop()
            return 0

