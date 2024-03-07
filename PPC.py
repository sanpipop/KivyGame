from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty

from kivy.core.window import Window


class Player(Widget):
    def attack(self):
        pass
    
class Enemy(Widget):
    def attack(self):
        pass

class GameWidget(Widget):
    player = ObjectProperty(None)
    enemy = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(
            self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        
    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print('you press ', text)



class PpcApp(App):
    def build(self):
        game = GameWidget()
        return game


if __name__ == '__main__':
    PpcApp().run()

