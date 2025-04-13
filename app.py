import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from utils import MarkUp

class Login(App):
    def build(self):
        lbl1 = Label(text="Enter Your Name : ")
        lbl2 = Label(text="Enter Your Phone Number : ")
        lbl3 = Label(text="Enter Your Email : ")

        txt1 = TextInput(multiline=False)
        txt2 = TextInput(multiline=False)
        txt3 = TextInput(multiline=False)
        box = BoxLayout(orientation="vertical")

        box.add_widget(lbl2)
        box.add_widget(txt2)

        box.add_widget(lbl1)
        box.add_widget(txt1)

        box.add_widget(lbl3)
        box.add_widget(txt3)

        box.add_widget(Button(size_hint=(1 , .5) , text=f"{MarkUp("b" , "Send")}" , font_size="40" , markup=True , background_color=(.5 , 0 , 1)))

        return box
    
if __name__ == "__main__" :
    Login().run()