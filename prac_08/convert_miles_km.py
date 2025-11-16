"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Rory Harland CSE
Started 13/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KILOMETRE = 1.60934 #on the off chance those french nerds at BIPM decide to change either unit


class ConvertMilesToKm(App):
    result = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


    def handle_update(self, value):
        """Handle changes to the text input by updating the model from the view."""
        self.result = str(value * MILE_TO_KILOMETRE)


    def handle_calculate(self, text):
        """ Takes parameter text, calls updating function. """
        value = self.convert_to_float(text)
        self.handle_update(value)


    def handle_increment(self, text, increment):
        """ Takes parameter increment and updates the kivy TextInput text. """
        self.root.ids.input_number.text = str(self.convert_to_float(text) + increment)


    @staticmethod
    def convert_to_float(text):
        """ Takes the input text, and returns it as float or 0. """
        try:
            value = float(text)
            return value
        except ValueError:
            return 0.0


ConvertMilesToKm().run()