from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton,MDFlatButton
from kivy.core.clipboard import Clipboard
from kivymd.uix.dialog import MDDialog
import string  
import random  

class DialogContent(MDBoxLayout):
    pass

class MainApp(MDApp):
    def build(self):
        self.dialog=None
        self.theme_cls.primary_palette="DeepPurple"
        return self.root


    def generate_password(self):
        len=self.root.ids.length_input.text
        if not len:
            self.show_dialog()
            return

        letters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
        password_length = int(self.root.ids.length_input.text)
        password = "".join(random.sample(letters, password_length))
        self.root.ids.answer.text = password

    def copy_password(self):
        password=self.root.ids.answer.text
        if password:
            Clipboard.copy(password)

    def show_dialog(self):
        if not self.dialog:
            self.dialog=MDDialog(
                title="Warning",
                text="Please enter the length of the password",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=self.theme_cls.primary_color,
                        on_release= lambda x: self.dialog.dismiss()
                    )
                ],
            )
            self.dialog.open()




if __name__=="__main__":
    MainApp().run()