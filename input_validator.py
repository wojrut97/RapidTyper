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


    def on_press(self):
        c = readchar.readkey()
        # print("Wcisnąłeś: ", c)
        if(c != '' or c != chr(13)):
            self.user_input_str += c
            print(c, end='', flush=True)
        elif(c == chr(13)):
            pass

    def validate(self):
        if(self.user_input_list):
            if(self.user_input_list[-1] == self.template_string[len(self.user_input_list) - 1]):
                print(colors.colors.lightgrey + self.user_input_list[-1], end = '')
            else:
                print(colors.colors.red + self.user_input_list[-1], end = '')

    def update_template_string(self, template_string):
        self.template_string = template_string

