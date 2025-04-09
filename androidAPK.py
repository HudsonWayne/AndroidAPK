from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        return MDLabel(
            text="Welcome to Wscube Tech",
            halign="center",
            theme_text_color="Custom",
            text_color=(0, 0.5, 1, 1),  # Optional: Blue text
            font_style="H5"
        )

if __name__ == "__main__":
    MainApp().run()
