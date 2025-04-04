from kivymd.app import MDApp 
from kivymd.uix.label import MDLabel

class TheApp(MDApp):
    def build(self):
        return MDLabel(
            text="Hello to Qimono", 
            halign="center",
            theme_text_color="Primary",
            font_style="H4"
            )

TheApp().run()
