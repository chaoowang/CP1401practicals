from kivy.app import App
from kivy.lang import Builder
import random

class HelloKv(App):

    def build(self):
        self.title = self.custom_title
        file_name = self.file_name

        self.root = Builder.load_file(file_name)
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.custom_title = "My title is a Hero"
        self.file_name = "layout.kv"

    def press_button(self,button):
        print("app:"+self.custom_title)
        if random.randint(0,10) <=5:
            self.root.ids.my_label.text="Ouch!"
        else:
            self.root.ids.my_label.text="Stop that!"


if __name__ == '__main__':
    the_app = HelloKv()
    the_app.run()
