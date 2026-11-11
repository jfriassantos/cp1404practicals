"""
CP1404: Convert Miles to Kilometres
Date: 11/11/2026
By: Jose Santos
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

KILOMETRES_TO_MILES_RATIO = 1.60934


class ConvertMilesToKilometres(App):
    """ConvertMilesToKilometres is a Kivy app that will convert miles to kilometres."""
    output_text = StringProperty()

    def build(self):
        """Build the Kivy App from the kv file."""
        Window.size = (250, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self, value):
        """Handle calculation to convert miles to kilometres."""
        try:
            result = float(value) * KILOMETRES_TO_MILES_RATIO
            self.output_text = str(result)
        except ValueError:
            self.output_text = "0"

    def handle_increment(self, value, increment):
        """Handle incrementing amount of kilometres."""
        try:
            result = float(value) + increment
            self.root.ids.input_text.text = f"{result}"
        except ValueError:
            pass


ConvertMilesToKilometres().run()
