from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class FILOTApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        title = Label(
            text="FILOT Pump Assistant",
            font_size=28
        )

        button = Button(
            text="شروع"
        )

        layout.add_widget(title)
        layout.add_widget(button)

        return layout


if __name__ == "__main__":
    FILOTApp().run()__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 20

        self.label = Label(
            text="FILOT Kivy Test",
            font_size="28sp"
        )

        self.button = Button(
            text="Test",
            font_size="22sp"
        )

        self.button.bind(on_press=self.button_pressed)

        self.add_widget(self.label)
        self.add_widget(self.button)

    def button_pressed(self, instance):
        self.label.text = "Kivy is working!"


class FILOTApp(App):

    def build(self):
        return MainLayout()


if __name__ == "__main__":
    FILOTApp().run()
