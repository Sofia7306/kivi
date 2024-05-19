from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.spinner import Spinner



class MyApp(App):
    def build(self):
        label =Label(text="Привіт")
        button =Button(text="Привіт")
        text = TextInput()
        spinner= Spinner(text="вибір",values=("1","2","3"))
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(spinner)
        layout.add_widget(label)
        layout2 = BoxLayout()
        layout2.add_widget(button)
        layout2.add_widget(layout)
        return layout2
    
app = MyApp()
app.run()
    
