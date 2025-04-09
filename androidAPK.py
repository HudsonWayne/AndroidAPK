from kivymd.app import MDApp
from kivymd.uix.label import MDLabel  # Fixed 'uix'

class Main_App(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Wscube Tech", halign="center")  # Lowercase 'center'

if __name__ == "__main__":  # Moved outside the class
    Main_App().run()
