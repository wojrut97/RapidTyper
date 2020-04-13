import pynput
import json
from pynput.keyboard import Key, Listener
import random

class Display():
    def __init__(self):
        self.level_content = self.load_level_content()

    def load_level_content(self):
        with open("levels.json", 'r') as f:
            datastore = json.load(f)
        current_level = datastore["levels"]["2"]
        level_content = current_level["keys"]
        return level_content

    def generate_string(self, level_content):
        level_content_list = level_content.split(",")
        generated_string = []
        for x in range(0, 30):
            letter_index = random.randrange(len(level_content_list))
            generated_string.append(level_content_list[letter_index])
        return ''.join(generated_string)