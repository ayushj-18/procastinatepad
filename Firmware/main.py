import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryEncoder
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.row_pins = (board.D5, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder = RotaryEncoder(
    pins=(board.D7, board.D8),
    resolution=4,
    pos_side=KC.VOLU,
    neg_side=KC.VOLD
)
keyboard.modules.append(encoder)

keyboard.encoder_pins = (board.D9,)
keyboard.encoder_map = [(KC.MUTE,)]

layers = Layers()
keyboard.modules.append(layers)

keyboard.keymap = [
    [
        KC.ESC, KC.Q, KC.W, KC.E, KC.BSPACE,
        KC.LSHIFT,   KC.CAPSLOCK, KC.D, KC.F, KC.ENTER
    ]
]

if __name__ == '__main__':
    keyboard.go()
