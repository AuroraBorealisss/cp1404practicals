"""
CP1404//CP5632, IT@JCU practical_08
dynamic_labels.py
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """ Main program for dynamic labels program. """

    def __init__(self, **kwargs):
        """ Defines the list of names to be displayed in the kivy program. """
        super().__init__(**kwargs)
        self.names = ['Angela', 'Pamela', 'Sandra', 'Rita', 'Monica', 'Erica', 'Tina', 'Mary', 'Jessica']

    def build(self):
        """ Builds kivy UI with a dynamic number of labels. """
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root


    def create_labels(self):
        """ creates a Label of every item in list. """
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)

DynamicLabelsApp().run()