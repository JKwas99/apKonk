from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size=(350, 600)

class Interface(Widget):
    def zmien(self,sm):
        if sm.current=="log":
            sm.current="rej"
            sm.transition.direction = "left"
        else:
            sm.current="log"
            sm.transition.direction = "right"
    def zaloguj(self,sm):
        login = self.ids.login.text
        haslo = self.ids.haslo.text
        if login!="" and haslo!="":
            sm.current="glowna"
            sm.transition.direction = "right"
            self.ids.blad.text = ""
        elif login=="" and haslo!="":
            self.ids.blad.text="Podaj poprawny login!"
            self.ids.haslo.text=""
        elif haslo=="" and login!="":
            self.ids.blad.text = "Podaj poprawne hasło!"
            self.ids.login.text = ""
        else:
            self.ids.blad.text = "Podaj poprawne dane!"
    def zarejestruj(self,sm):
        # sm.current = "glowna"
        blad=""
        if self.ids.Rimie.text!="" and self.ids.Rnazwisko.text!="" and self.ids.Remail.text != "" and '@' in self.ids.Remail.text and self.ids.Rhaslo.text!="" and self.ids.Radres.text!="":
            sm.current = "glowna"
            # print("działa")
        else:
            if self.ids.Rimie.text=="":
                blad+="imię "
            if self.ids.Rnazwisko.text=="":
                blad+="nazwisko "
            if self.ids.Remail.text == "" or '@' not in self.ids.Remail.text:
                blad+="email "
            if self.ids.Rhaslo.text=="":
                blad+="hasło "
            if self.ids.Radres.text=="":
                blad+="adres "
        print(blad)

class MyApp(MDApp):
    def build(self):
        pass

MyApp().run()