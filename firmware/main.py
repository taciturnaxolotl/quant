# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(MediaKeys())

# Define your pins here!
PINS = [board.D11, board.D2, board.D9, board.D1, board.D8, board.D10, board.D3, board.D4, board.D6]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.MPRV, KC.MPLY, KC.MNXT,
        KC.MUTE, KC.VOLD, KC.VOLU,
        KC.PSCR, KC.Macro(KC.Press(KC.LCTRL), KC.Tap(KC.PSCR)), KC.Macro(KC.Press(KC.LCTRL, KC.Press(KC.LALT), KC.Tap(KC.DOT))),
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
