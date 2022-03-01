""" Script to run the python/Kivy GUI to interact with the local MariaDB database titled "compoundpingpong" """

import mariadb
import sys
#import pongRdbconnect as prdbconn
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

class PongRStartscreen(Screen):
    """ displays a banner on startup """

    def build(self):
        main_layout = FloatLayout()
        main_layout.add_widget(Image(source = 'images/wood-bg-splash-screen.png'))
        self.add_widget(main_layout)
        return main_layout

class PongRApp(App):
    """ class that is called when the app is run - directly implements the member ScreenManager object 'sm' """

    def build(self):
        # cur, conn = prdbconn.dbconnect("localhost")
        sm = ScreenManager()
        pr_startscreen = PongRStartScreen(name='pr_startscreen')
        sm.add_widget(pr_startscreen)

        sm.current = 'pr_startscreen'
        return sm

# if this is the main program, run the PongRApp
if __name__=='__main__':
    PongRStartscreen().run()
