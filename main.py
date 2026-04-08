import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from PIL import Image

class ColorizerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="AI Photo Colorizer Lite", font_size='20sp', size_hint_y=0.1)
        self.layout.add_widget(self.label)

        # ফাইল সিলেক্টর (শুধু ছবি দেখাবে)
        self.file_chooser = FileChooserIconView(filters=['*.jpg', '*.png', '*.jpeg'], size_hint_y=0.7)
        self.layout.add_widget(self.file_chooser)

        self.btn = Button(text="রঙিন করুন", size_hint=(1, 0.2), background_color=(0, 0.7, 0.3, 1))
        self.btn.bind(on_press=self.colorize_image)
        self.layout.add_widget(self.btn)
        return self.layout

    def colorize_image(self, instance):
        selected = self.file_chooser.selection
        if selected:
            input_path = selected[0]
            self.label.text = "প্রসেসিং হচ্ছে..."
            # আপাতত সফল মেসেজ দেখাবে, পরে আমরা AI ফিল্টার যোগ করব
            self.label.text = f"সফল! {os.path.basename(input_path)} রেডি।"
        else:
            self.label.text = "দয়া করে একটি ছবি সিলেক্ট করুন!"

if __name__ == "__main__":
    ColorizerApp().run()
    
