# import busio

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.modules.split import Split
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Sequence
from kmk.modules.macros import Macros, Press, Release, Tap
# from kmk.extensions.display.ssd1306 import SSD1306
# from kmk.extensions.display import Display, TextEntry, ImageEntry

# Define this as a split keyboard
split = Split(use_pio=True)

# Enable layers
LEDS = { (1, 3): 4 }
layers = Layers(LEDS)

# Define key combos
combos = Combos()
combos.combos = [
    Sequence((KC.LCTL, KC.QUOT), KC.ESC)
]

# Enable macros
macros = Macros()

keyboard = KMKKeyboard()
keyboard.modules = [layers, combos, split, macros]

# RGB LEDs!
rgb = RGB(
    pixel_pin=keyboard.rgb_pin,
    num_pixels=keyboard.num_pixels,
)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

RGB_TOG = KC.RGB_TOG
RGB_HUI = KC.RGB_HUI
RGB_HUD = KC.RGB_HUD
RGB_SAI = KC.RGB_SAI
RGB_SAD = KC.RGB_SAD
RGB_VAI = KC.RGB_VAI
RGB_VAD = KC.RGB_VAD
RGB_M_P = KC.RGB_M_P 	# RGB_MODE_PLAIN            Static RGB
RGB_M_K = KC.RGB_M_K 	# RGB_MODE_KNIGHT           Knight Rider animation
RGB_M_S = KC.RGB_M_S 	# RGB_MODE_SWIRL            Swirl animation
RGB_M_B = KC.RGB_M_B 	# RGB_MODE_BREATHE          Breathing animation
RGB_M_R = KC.RGB_M_R 	# RGB_MODE_RAINBOW 	        Rainbow animation
RGB_M_BR = KC.RGB_M_BR  # RGB_MODE_BREATHE_RAINBOW  Breathing rainbow animation

# Define layers
L1 = KC.MO(1) # Move & Numbers
L2 = KC.MO(2) # Symbols
L3 = KC.MO(3) # Braces

# fmt:off
keyboard.keymap = [
    # QWERTY
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |  Q   |  W   |  E   |  R   |  T   |                    |  Y   |  U   |   I  |  O   |  P   | Bksp |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LCtl |  A   |  S   |  D   |  F   |  G   |                    |  H   |  J   |   K  |  L   |  ;   | Quot |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |  Z   |  X   |  C   |  V   |  B   |-------.    ,-------|  N   |  M   |   ,  |  .   |  /   | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |      |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                  KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,    KC.BSPC,
        KC.LCTL,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                  KC.H,    KC.J,    KC.K,    KC.L,  KC.SCLN,  KC.QUOT,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                  KC.N,    KC.M,  KC.COMM,  KC.DOT, KC.SLSH,  KC.RSFT,
                                            L3,    L1,    KC.ENT,        KC.SPC,    L2,    KC.RGUI,
    ],

    # L1 - Move & Numbers
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Esc  |  1   |  2   |  3   |  4   |  5   |                    |  6   |  7   |  8   |  9   |  0   | Del  |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LCtl |      |      |      |      |      |                    | Left | Down |  Up  | Right|      |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |      |      |      |      |      |-------.    ,-------|      |      |      |      |      | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |      |  --  |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                  KC.N6,   KC.N7,   KC.N8,   KC.N9,    KC.N0,   KC.DEL,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                 KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                 XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, KC.RSFT,
                                            L3,    L1,    KC.ENT,        KC.SPC,    L2,    KC.RGUI,
    ],

    # L2 - Symbols
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Esc  |  !   |  @   |  #   |  $   |  %   |                    |      |      |      |      |      |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LCtl |  *   |  &   |  +   |  -   |  `   |                    |      |      |      |      |      |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |      |  ^   |  =   |  _   |  ~   |-------.    ,-------|      |      |      |      |      | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |      |      |/       /         \      \ |  --  |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.ESC,  KC.EXLM, KC.AT,   KC.HASH, KC.DLR, KC.PERC,                  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.LCTL, KC.ASTR, KC.AMPR, KC.PLUS, KC.MINS, KC.GRV,                  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, KC.CIRC, KC.EQL,  KC.UNDS, KC.TILD,                 XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.RSFT,
                                            L3,    L1,    KC.ENT,        KC.SPC,    L2,    KC.RGUI,
    ],

    # L3 - Braces
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |      |      |      |      |      |                    |      |  [   |  ]   |      |      |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LCtl |      |      |      |      |      |                    |      |  (   |  )   |      |  |   |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |      |      |      |      |      |-------.    ,-------|      |  {   |  }   |      |  \   |      |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |  --  |      |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.TAB,  XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LBRC, KC.RBRC, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.LCTL, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LPRN, KC.RPRN, XXXXXXX, KC.PIPE, XXXXXXX,
        KC.LSFT, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LCBR, KC.RCBR, XXXXXXX, KC.BSLS, XXXXXXX,
                                            L3,    L1,    KC.ENT,        KC.SPC,   L2,    KC.RGUI,
    ],
    
    # LEDS
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Togl | Hue+ | Sat+ | Val+ |      | Swrl |                    | Swrl |      | Val+ | Sat+ | Hue+ | Togl |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |      | Hue- | Sat- | Val- |      | KntRd|                    | KntRd|      | Val- | Sat- | Hue- |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | BRB  | RnBw | Brth |      |      | Plain|-------.    ,-------| Plain|      |      | Brth | RnBw | BRB  |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |  --  |  --  |/       /         \      \ |      |      |
    #                          `---------------------'           '------''-------------'
    [
        RGB_TOG, RGB_HUI, RGB_SAI, RGB_VAI, XXXXXXX, RGB_M_S,                 RGB_M_S, XXXXXXX, RGB_VAI, RGB_SAI, RGB_HUI, RGB_TOG,
        XXXXXXX, RGB_HUD, RGB_SAD, RGB_VAD, XXXXXXX, RGB_M_K,                 RGB_M_K, XXXXXXX, RGB_VAD, RGB_SAD, RGB_HUD, XXXXXXX,
        RGB_M_BR,RGB_M_R, RGB_M_B, XXXXXXX, XXXXXXX, RGB_M_P,                 RGB_M_P, XXXXXXX, XXXXXXX, RGB_M_B, RGB_M_R, RGB_M_BR,
                                            L3,    L1,    KC.ENT,        KC.SPC,    L2,    KC.RGUI,
    ]
]
# fmt:on

# Setting up the OLED display
# i2c_bus = busio.I2C(keyboard.scl_pin, keyboard.sda_pin)
# driver = SSD1306(i2c=i2c_bus)
# display = Display(display=driver)

# display.entries = [
#     TextEntry(text="Foo",   x=65, layer=0, direction="DWR"),
#     TextEntry(text="Lower", x=80, layer=1, direction="DWR"),
#     TextEntry(text="Layer", x=65, layer=1, direction="DWR"),
#     TextEntry(text="Raise", x=80, layer=2, direction="DWR"),
#     TextEntry(text="Layer", x=65, layer=2, direction="DWR"),
#     TextEntry(text="LED",   x=80, layer=3, direction="DWR"),
#     TextEntry(text="Layer", x=65, layer=3, direction="DWR"),
# ]

# keyboard.extensions = [display, rgb]
keyboard.extensions = [rgb]

if __name__ == '__main__':
    keyboard.go()
