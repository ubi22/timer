from kivy.lang import Builder
from kivymd.app import MDApp
import time
import threading


class MoneyTest(MDApp):
    def popman(self):
        t1 = threading.Thread(target=self.mans)
        t1.start()

    def mans(self):
        a = 0
        while True:
            time.sleep(0.1)
            a+=0.1
            print(a)
            a = round(a, 2)
            self.root.ids.button.text = f"{a}"

    def build(self):
        return Builder.load_file('kivy.kv')

MoneyTest().run()
