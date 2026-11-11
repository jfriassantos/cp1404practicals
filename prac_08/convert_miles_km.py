"""
CP1404: Convert Miles to Kilometres
Date: 11/11/2026
By: Jose Santos
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometres(App):
    """ConvertMilesToKilometres is a Kivy app that will convert miles to kilometres."""

    def build(self):
        """Build the Kivy App from the kv file."""
        Window.size = (250, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root


ConvertMilesToKilometres().run()
