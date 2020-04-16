from display import Display
from input_validator import InputValidator
import curses
from curses import wrapper

def main(stdscr):
    displayer = Display()
    input_validator = InputValidator()
    input_validator.template_string = displayer.generate_string(displayer.level_content)
    #Main loop
    error = 0
    stdscr.addstr(input_validator.template_string)
    while(error != 1):
        error = input_validator.get_key(stdscr)
    

if __name__ == "__main__":
    wrapper(main)