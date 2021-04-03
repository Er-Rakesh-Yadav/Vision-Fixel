from kivymd.app import MDApp
from kivy.lang import Builder

#Builder-String
kv = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Vision-Fixel"
            halign: 'right'

    MDBoxLayout:
        orientation:'vertical'

    MDToolbar:
        title: 'Bottom navigation'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1
        text_color_active: 1, 0, 0, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: '2.png'

            MDLabel:
                text: 'HOME'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'EXIT'
            icon: '3.png'

            MDLabel:
                text: 'BYE BYEEE!!!'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'About'
            icon: 'a.png'

            MDLabel:
                text: 'About'
                halign: 'center'

'''


class MainApp(MDApp):
    def build(self):
        MDApp.title = "Vision Fixel"
        MDApp.icon = 'vision_icon.png'
        return Builder.load_string(kv)


MainApp().run()
