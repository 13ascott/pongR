""" Script to run the python/Kivy GUI to interact with the local MariaDB database titled "compoundpingpong" """

import mariadb
import sys
import pongRdbconnect as prdbconn
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

class MSLabel(Label):
    pass

class MSButton(Button):
    screen_text = 'pr_errorscreen'

class BasicBkg(FloatLayout):

  def gotomain(self, instance):
      self.parent.parent.current = 'pr_mainscreen'
      return
    
class RecGameScreen(Screen):
    pass

class TournamentScreen(Screen):
    pass

class RankingsScreen(Screen):
    pass

class SearchGameScreen(Screen):
    pass

class AddPlayerScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class MainScreen(Screen):

    def changeScreen(self, instance):
        self.parent.current = instance.screen_text
        return

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        main_layout = FloatLayout()
        main_layout.add_widget(Image(source = 'images/wood-bg-w-logo.png'))

        main_menu = BoxLayout(orientation = 'vertical', size_hint = (0.6, 0.95), pos_hint = {'x':0.3, 'y':0.03}, spacing = 14)
        main_menu.add_widget(MSLabel(text='MAIN MENU'))
        rgbutt = MSButton(text='RECORD GAME', on_release=self.changeScreen)
        rgbutt.screen_text = 'pr_recgamescreen'
        main_menu.add_widget(rgbutt)
        stbutt = MSButton(text='START TOURNAMENT', on_release=self.changeScreen)
        stbutt.screen_text = 'pr_tournamentscreen'
        main_menu.add_widget(stbutt)
        main_menu.add_widget(MSButton(text='VIEW RANKINGS', on_release=self.changeScreen))
        main_menu.add_widget(MSButton(text='VIEW GAME RESULTS', on_release=self.changeScreen))
        main_menu.add_widget(MSButton(text='ADD PLAYER', on_release=self.changeScreen))
        main_menu.add_widget(MSButton(text='SETTINGS', on_release=self.changeScreen))
        main_layout.add_widget(main_menu)
        
        self.add_widget(main_layout)

class PongRStartscreen(Screen):
    """ displays a banner on startup """

    def __init__(self, **kwargs):
        super(PongRStartscreen, self).__init__(**kwargs)
        main_layout = FloatLayout()
        main_layout.add_widget(Image(source = 'images/wood-bg-splash-screen.png'))
        self.add_widget(main_layout)

    def on_touch_down(self, touch):
        self.manager.transition = NoTransition()
        self.manager.current = 'pr_mainscreen'

class PongRApp(App):
    """ class that is called when the app is run - directly implements the member ScreenManager object 'sm' """

    def build(self):
        self.cur, self.conn = prdbconn.dbconnect("localhost")
        self.sm = ScreenManager()
        self.sm.add_widget(PongRStartscreen(name='pr_startscreen'))
        self.sm.add_widget(MainScreen(name = 'pr_mainscreen'))
        self.sm.add_widget(RecGameScreen(name = 'pr_recgamescreen'))
        self.sm.add_widget(TournamentScreen(name = 'pr_tournamentscreen'))
        self.sm.add_widget(RankingsScreen(name = 'pr_rankingsscreen'))
        self.sm.add_widget(SearchGameScreen(name = 'pr_viewgamescreen'))
        self.sm.add_widget(AddPlayerScreen(name = 'pr_addplayerscreen'))
        self.sm.add_widget(SettingsScreen(name = 'pr_settingsscreen'))

        self.sm.current = 'pr_startscreen'
        Window.size = (1280,720)
        
        return self.sm
        

# if this is the main program, run the PongRApp
if __name__=='__main__':
    PongRApp().run()
