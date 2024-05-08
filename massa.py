from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class Login(BoxLayout):
    def __init__(self, **kwargs):
        Window.clearcolor = (0.1, 0, 0.1, 1)
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = [100, 100]
        self.spacing = 10

        
        self.add_widget(Label(text="LOGIN", font_size=30, font_name='Georgia', color=get_color_from_hex('#1E90FF')))

        
        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)
        

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#32CD32')))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#32CD32')))
        self.add_widget(self.senha_input)
        
        

       
        self.cadastrar_button = Button(text="Cadastrar", background_color=(0, 1, 0, 0.75))
        self.login_button = Button(text="Já possuo uma conta", background_color=(0, 0, 1))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()