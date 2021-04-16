from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (400, 600)

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
        on_press:
            root.manager.current = 'Main_screen'
        

    
<SecondScreen>:
    name: 'Main_screen'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title: 'Menu'
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    
                    MDBottomAppBar:
                        MDToolbar:
                            title:'SAVE'
                            elevation: 5
                            left_action_items: [['download', lambda x: app.navigation_draw()]]
                            type: 'bottom'
                            mode: 'end'
                            icon: 'upload'
                                                           
                    Widget:
                    
                Image:
                    source: 'App/img/bg.jpg'
                   
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                Image:
                    source:'01.jpg'
                    
                MDLabel:
                    text: 'EFFECTS '
                    font_style: 'H5'
                    size_hint_y: None
                    halign: 'center'
                    height: self.texture_size[1]
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Pgglluuu'
                            IconLeftWidget:
                                icon: 'face'
                        OneLineIconListItem:
                            text: 'Subbuuu '
                            IconLeftWidget:
                                icon:'download'
                        OneLineIconListItem:
                            text: 'MOTO'
                            IconLeftWidget:
                                icon: 'upload'
                        OneLineIconListItem:
                            text: 'Yadav Ji'
                            IconLeftWidget:
                                icon:'send'    
'''


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


loadScreen = ScreenManager()
loadScreen.add_widget(FirstScreen(name='1_screen'))
loadScreen.add_widget(SecondScreen(name='2_screen'))


def navigation_draw():
    print("Navigation Is Working")


class MainApp(MDApp):
    def build(self):
        MDApp.title = "Vision Fixel"
        MDApp.icon = 'vision_icon.png'
        screen = Screen()
        loadKv = Builder.load_string(kv)
        screen.add_widget(loadKv)
        return screen


MainApp().run()
