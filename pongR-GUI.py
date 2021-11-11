""" Script to run the python/Kivy GUI to interact with the local MariaDB database titled "compoundpingpong" """

import mariadb
import sys
# import pongR-dbconnect as pongconnect
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

class PongRStartscreen(FloatLayout):

    def __init__(self,**kwargs):
        super(PongRStartscreen, self).__init__(**kwargs)
        self.add_widget(Image(source = 'images/wood-bg-splash-screen.png'))


class PongRApp(App):

    def build(self):
        return PongRStartscreen()

if __name__=='__main__':
    PongRApp().run()
