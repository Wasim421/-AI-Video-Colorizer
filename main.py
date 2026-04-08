import os
import urllib.request
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from PIL import Image
import numpy as np

class ColorizerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="AI ফটো কালারাইজার (Lite)", font_size='20sp', size_hint_y=0.1)
        self.layout.add_widget(self.label)

        self.file_chooser = FileChooserIconView(filters=['*.jpg', '*.png', '*.jpeg'], size_hint_y=0.7)
        self.layout.add_widget(self.file_chooser)

        self.btn = Button(text="রঙিন করুন", size_hint=(1, 0.2), background_color=(0, 0.7, 0.3, 1))
        self.btn.bind(on_press=self.start_process)
        self.layout.add_widget(self.btn)
        return self.layout

    def start_process(self, instance):
        selected = self.file_chooser.selection
        if selected:
            self.label.text = "প্রসেসিং হচ্ছে... (OpenCV ছাড়া)"
            # এখানে আপনার AI লজিক বা ফিল্টার কাজ করবে
            self.label.text = "সফল! ফটোটি রঙিন হয়েছে।"
        else:
            self.label.text = "একটি ছবি সিলেক্ট করুন!"

if __name__ == "__main__":
    ColorizerApp().run()
    
