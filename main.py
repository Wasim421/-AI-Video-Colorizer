import cv2
import numpy as np
import os
import urllib.request
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView

class ColorizerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="AI ভিডিও কালারাইজার", font_size='20sp', size_hint_y=0.1)
        self.layout.add_widget(self.label)

        # ফাইল সিলেক্টর
        self.file_chooser = FileChooserIconView(filters=['*.mp4', '*.avi'], size_hint_y=0.7)
        self.layout.add_widget(self.file_chooser)

        # বাটন
        self.btn = Button(text="রঙিন (Colorize) করুন", size_hint=(1, 0.2), background_color=(0, 0.6, 1, 1))
        self.btn.bind(on_press=self.start_process)
        self.layout.add_widget(self.btn)

        return self.layout

    def download_models(self):
        """বড় মডেল ফাইলটি ইন্টারনেট থেকে ডাউনলোড করার ফাংশন"""
        model_url = "https://huggingface.co/lowlevelvision/colorization/resolve/main/colorization_release_v2.caffemodel"
        model_name = "colorization_release_v2.caffemodel"
        
        if not os.path.exists(model_name):
            self.label.text = "মডেল ডাউনলোড হচ্ছে (১২৯ এমবি)... সময় লাগবে।"
            try:
                urllib.request.urlretrieve(model_url, model_name)
                return True
            except Exception as e:
                self.label.text = f"ডাউনলোড ব্যর্থ: {str(e)}"
                return False
        return True

    def start_process(self, instance):
        selected = self.file_chooser.selection
        if selected:
            input_path = selected[0]
            output_path = os.path.join(os.path.dirname(input_path), "colorized_output.mp4")
            
            # প্রথমে মডেল চেক/ডাউনলোড করা হবে
            if self.download_models():
                self.label.text = "প্রসেসিং শুরু হয়েছে... অপেক্ষা করুন।"
                self.run_ai_logic(input_path, output_path)
        else:
            self.label.text = "দয়া করে একটি ভিডিও সিলেক্ট করুন!"

    def run_ai_logic(self, input_path, output_path):
        PROTOTXT = "colorization_deploy_v2.prototxt"
        MODEL = "colorization_release_v2.caffemodel"
        POINTS = "pts_in_hull.npy"

        try:
            net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)
            pts = np.load(POINTS)

            class8 = net.getLayerId("class8_ab")
            conv8 = net.getLayerId("conv8_313_rh")
            pts = pts.transpose().reshape(2, 313, 1, 1)
            net.getLayer(class8).blobs = [pts.astype("float32")]
            net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

            cap = cv2.VideoCapture(input_path)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret: break

                scaled = frame.astype("float32") / 255.0
                lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
                resized = cv2.resize(lab, (224, 224))
                L = cv2.extractChannel(resized, 0)
                L -= 50

                net.setInput(cv2.dnn.blobFromImage(L))
                ab = net.forward()[0, :, :, :].transpose((1, 2, 0))
                ab = cv2.resize(ab, (frame.shape[1], frame.shape[0]))

                L = cv2.extractChannel(lab, 0)
                colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
                colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
                colorized = (255 * colorized).astype("uint8")

                out.write(colorized)

            cap.release()
            out.release()
            self.label.text = "সফল! রঙিন ভিডিও সেভ হয়েছে।"
        
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    ColorizerApp().run()
                
