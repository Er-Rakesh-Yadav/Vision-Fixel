from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
# for Main Screen Size
from kivy.core.window import Window

Window.size = (400, 600)

# Builder-String
kv = '''
ScreenManager:
    MainScreen:

<MainScreen>:
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
                            on_action_button: app.navigation_draw()                     
                    Widget:
                    
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


class MainScreen(Screen):
    pass


loadScreen = ScreenManager()
loadScreen.add_widget(MainScreen(name='Main_screen'))


class App(MDApp):
    def build(self):
        MDApp.title = "Vision Fixel"
        MDApp.icon = 'vision_icon.png'
        screen = Screen()
        loadKv = Builder.load_string(kv)
        screen.add_widget(loadKv)
        return screen

    def navigation_draw(self):
        print("Navigation Is Working")


App().run()
