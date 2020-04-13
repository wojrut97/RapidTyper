from display import Display
from input_validator import InputValidator

def main():
    displayer = Display()
    input_validator = InputValidator()
    template_string = displayer.generate_string(displayer.level_content)
    print(template_string)
    input_validator.update_template_string(template_string)
    counter = 10
    while(counter):
        input_validator.on_press()
        counter -= 1
        continue
    

if __name__ == "__main__":
    main()