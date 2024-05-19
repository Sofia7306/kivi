from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import ScreenManager, Screen

class Tempate_Button(Button):
    def __init__(self,screen,direction="right", goal="main",**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class Screen_Main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Tempate_Button(self,direction="left",goal="screen1",text="перейти на 2 екран")
        button1 = Tempate_Button(self,direction="up",goal="screen2",text="перейти на 3 екран")
        label =Label(text="11")
        layout = BoxLayout()
        layout.add_widget(label)
        layout.add_widget(button1)
        layout.add_widget(button)
        self.add_widget(layout)

class Screen_1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Tempate_Button(self,direction="right",goal="main",text="перейти на головну")
        self.add_widget(button)

class Screen_2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        button = Tempate_Button(self,direction="down",goal="main",text="перейти на головну")
        self.add_widget(button)

class MyApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(Screen_Main(name="main"))
        manager.add_widget(Screen_1(name="screen1"))
        manager.add_widget(Screen_2(name="screen2"))
        return manager


app = MyApp()
app.run()

