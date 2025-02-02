from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivymd.uix.chip import MDChip
from kivymd.app import MDApp
# from kivymd.uix.button import MDRaisedButton

KV = '''
<MyChip@MDChip>:
    size_hint: None, None
    size: self.texture_size[0] + dp(16), dp(36)
    font_size: '14sp'

FloatLayout:
    orientation: 'vertical'

    BoxLayout:
        id: chips_container
        spacing: dp(10)
        padding: dp(10)
        size_hint_y: None
        height: self.minimum_height

    Button:
        text: "Get Selected Chip"
        on_press: app.get_selected_chip()
        size_hint: .1,.1
'''


class MyChip(ToggleButtonBehavior, MDChip):
    pass


class ChipExampleApp(MDApp):
    selected_chip = ListProperty([])

    def build(self):
        return Builder.load_string(KV)

    def create_chips(self):
        chips_container = self.root.ids.chips_container
        chips_container.clear_widgets()

        chip_data = ['Chip 1', 'Chip 2', 'Chip 3']  # Sample chip data

        for chip_text in chip_data:
            chip = MyChip(text=chip_text)
            chip.bind(on_release=self.on_chip_selected)
            chips_container.add_widget(chip)

    def on_chip_selected(self, chip):
        if chip.state == 'down':
            self.selected_chip = [chip.text]
            for child in self.root.ids.chips_container.children:
                if child != chip:
                    child.state = 'normal'

    def get_selected_chip(self):
        if self.selected_chip:
            print("Selected Chip:", self.selected_chip[0])
        else:
            print("No chip selected")


ChipExampleApp().run()