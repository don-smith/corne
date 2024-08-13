# import time
# import busio

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.modules.split import Split
from kmk.modules.layers import Layers
# from kmk.modules.combos import Combos, Sequence
# from kmk.extensions.display.ssd1306 import SSD1306
# from kmk.extensions.peg_rgb_matrix import Rgb_matrix, Rgb_matrix_data, Color
# from kmk.extensions.display import Display, TextEntry, ImageEntry

keyboard = KMKKeyboard()
keyboard.modules = []

#
# Define this as a split keyboard
split = Split(use_pio=True)

#
# Enable layers
layers = Layers()

#
# Define key combos
# combos = Combos()
# combos.combos = [
#     Sequence((KC.LCTL, KC.QUOT), KC.ESC)
# ]

keyboard.modules = [layers, split] #, combos]

#
# RGB LEDs!
rgb = RGB(
    pixel_pin=keyboard.rgb_pin,
    num_pixels=keyboard.num_pixels,
)

# data = Rgb_matrix_data(keys=[
#     Color.RED, Color.BLUE, Color.GREEN, Color.RED, Color.BLUE, Color.GREEN,            Color.RED, Color.BLUE, Color.GREEN, Color.RED, Color.BLUE, Color.GREEN,
#     Color.RED, Color.BLUE, Color.GREEN, Color.RED, Color.BLUE, Color.GREEN,            Color.RED, Color.BLUE, Color.GREEN, Color.RED, Color.BLUE, Color.GREEN,
#     Color.RED, Color.BLUE, Color.GREEN, Color.RED, Color.BLUE, Color.GREEN,            Color.RED, Color.BLUE, Color.GREEN, Color.RED, Color.BLUE, Color.GREEN,
#                                             Color.GREEN, Color.BLUE, Color.RED,    Color.GREEN, Color.BLUE, Color.RED
# ], underglow=[
#     Color.WHITE, Color.WHITE,Color.WHITE,     Color.WHITE, Color.WHITE, Color.WHITE,
#     Color.WHITE, Color.WHITE, Color.WHITE,    Color.WHITE, Color.WHITE, Color.WHITE,
# ])
# rgb = Rgb_matrix(ledDisplay=data, split=True, disable_auto_write=True)

keyboard.extensions = [rgb]

#
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.ENT)

RGB_TOG = KC.RGB_TOG
RGB_HUI = KC.RGB_HUI
RGB_HUD = KC.RGB_HUD
RGB_SAI = KC.RGB_SAI
RGB_SAD = KC.RGB_SAD
RGB_VAI = KC.RGB_VAI
RGB_VAD = KC.RGB_VAD

# fmt:off
keyboard.keymap = [
    [  #QWERTY
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,
        KC.LCTL,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,
                                            KC.LGUI,   LOWER,  ADJUST,     KC.SPC,   RAISE,  KC.RALT,
    ],
    [  #LOWER
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                            KC.LGUI,   LOWER,  ADJUST,     KC.SPC,   RAISE,  KC.RALT,
    ],
    [  #RAISE
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,
                                            KC.LGUI,   LOWER,  ADJUST,     KC.SPC,   RAISE,  KC.RALT,
    ],
    [  #ADJUST
        RGB_TOG, RGB_HUI, RGB_SAI, RGB_VAI, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, RGB_HUD, RGB_SAD, RGB_VAD, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                            KC.LGUI,   LOWER,  ADJUST,     KC.SPC,   RAISE,  KC.RALT,
    ]
]
# fmt:on

#
# Setting up the OLED display

# i2c_bus = busio.I2C(keyboard.scl_pin, keyboard.sda_pin)

# driver = SSD1306(
#     # Mandatory:
#     i2c=i2c_bus,
# )

# display = Display(
#     # Mandatory:
#     display=driver,
#     # Optional:
#     width=128, # screen size
#     height=32, # screen size
#     flip=True, # flips the display content
#     brightness=0.8, # initial screen brightness level
#     brightness_step=0.1, # used for brightness increase/decrease keycodes
#     dim_time=15, # time in seconds to reduce screen brightness
#     dim_target=0.01, # set level for brightness decrease
#     off_time=60, # time in seconds to turn off screen
#     powersave_dim_time=15, # time in seconds to reduce screen brightness
#     powersave_dim_target=0.01, # set level for brightness decrease
#     powersave_off_time=60, # time in seconds to turn off screen
# )

# display.entries = [
#     TextEntry(text="Lower", x=80, layer=1, direction="DWR"),
#     TextEntry(text="Layer", x=65, layer=1, direction="DWR"),

#     TextEntry(text="Raise", x=80, layer=2, direction="DWR"),
#     TextEntry(text="Layer", x=65, layer=2, direction="DWR"),

#     TextEntry(text="LED",   x=80, layer=3, direction="DWR"),
#     TextEntry(text="Layer", x=65, layer=3, direction="DWR"),
# ]

# keyboard.extensions = [rgb, display]

if __name__ == '__main__':
    keyboard.go()
