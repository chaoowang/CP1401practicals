from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class dynamic_label(App):

    status_text=StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names=["Ben","Ray","Janice","Carol"]

    def build(self):
        self.title="dynamic labels"
        self.root=Builder.load_file("dynamic_label.kv")
        self.create_widget()
        return self.root

    def create_widget(self):
        for name in self.names:
            temp_label=Label(text=name, id=name)
            temp_label.bind(on_press=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        name=instance.id
        self.status_text="".format(name)


dynamic_label().run()