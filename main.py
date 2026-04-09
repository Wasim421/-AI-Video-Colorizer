from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.image import Image as CoreImage
import os

class ColorizerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="AI Colorizer (Ultra Lite)", font_size='20sp', size_hint_y=0.1)
        self.layout.add_widget(self.label)

        # ফাইল সিলেক্টর
        self.file_chooser = FileChooserIconView(filters=['*.jpg', '*.png'], size_hint_y=0.7)
        self.layout.add_widget(self.file_chooser)

        self.btn = Button(text="Colorize (Simple)", size_hint=(1, 0.2), background_color=(0.2, 0.6, 1, 1))
        self.btn.bind(on_press=self.process_image)
        self.layout.add_widget(self.btn)
        return self.layout

    def process_image(self, instance):
        selected = self.file_chooser.selection
        if selected:
            # এখানে Kivy-র কোর ইমেজ ব্যবহার করে কাজ হবে
            img_path = selected[0]
            self.label.text = f"Selected: {os.path.basename(img_path)}\nProcessing without heavy libs..."
        else:
            self.label.text = "Please select an image!"

if __name__ == "__main__":
    ColorizerApp().run()
