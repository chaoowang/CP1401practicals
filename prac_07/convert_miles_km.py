from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609344


class Convert_miles_km(App):
    result_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self, miles_num):
        try:
            miles = float(miles_num)
            if miles <= 0:
                self.result_km = "0.0"
            else:
                km = miles * MILES_TO_KM
                self.result_km = str(km)
        except ValueError:
            self.result_km = "0.0"

    def miles_increase(self, miles_num):
        try:
            miles = float(miles_num)
            miles += 1
            self.root.ids.input_number.text = str(miles)
        except ValueError:
            self.root.ids.input_number.text = "1.0"

    def miles_decrease(self, miles_num):
        try:
            miles = float(miles_num)
            miles -= 1
            self.root.ids.input_number.text = str(miles)
        except ValueError:
            self.root.ids.input_number.text = "-1.0"


Convert_miles_km().run()
