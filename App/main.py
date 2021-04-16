from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
Window.size = (400,600)

# Builder-String
kv = '''
ScreenManager:
    FirstScreen:
    SecondScreen:
     
<FirstScreen>:
    name: '1_screen'
    MDIcon:
        icon: 'laptop'
        halign: 'center'
        font_size: 150
        theme_text_color: 'Custom'
        text_color: 224,0,0,1 
        
        
    MDLabel:
        text: 'VISION-FIXEL'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 0, 0, 1, 1
        font_style: 'Subtitle2'
        font_size: 15
    MDFloatingActionButton:
        icon: 'home'
        user_font_size: '20sp'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release:
            root_manager.current = '2_screen'
        

    
<SecondScreen>:
    name:'2_screen'
    MDLabel:
        text: 'OK'
        font_size: 10
        halign: 'auto'
    MDIconButton:
        icon: 'back'
        on_touch_up:
            root_manager.current = '1_screen'      
'''


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


loadScreen = ScreenManager()
loadScreen.add_widget(FirstScreen(name='1_screen'))
loadScreen.add_widget(SecondScreen(name='2_screen'))


class MainApp(MDApp):
    def build(self):
        MDApp.title = "Vision Fixel"
        MDApp.icon = 'vision_icon.png'
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '200'
        screen = Screen()
        loadKv = Builder.load_string(kv)
        screen.add_widget(loadKv)
        return screen

    def theme_changer(self):
        self.load_kv


MainApp().run()
