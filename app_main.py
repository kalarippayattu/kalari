from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class KalariApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text='Start Pose Detection', on_press=self.start_detection)
        layout.add_widget(btn)
        return layout

    def start_detection(self, instance):
        import kalari_app  # runs the pose detection code

KalariApp().run()