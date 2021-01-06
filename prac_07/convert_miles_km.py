from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class Convert_miles_km(App):
    result_km=StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self, miles):
        km = miles * 1.609344
        self.result_km = str(km)

    def miles_increase(self, miles):
        miles+=1
        self.root.ids.input_number.text=str(miles)
    def miles_decrease(self, miles):
        miles -= 1
        self.root.ids.input_number.text = str(miles)

Convert_miles_km().run()