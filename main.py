# import busio

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.modules.split import Split
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Sequence
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.tapdance import TapDance
# from kmk.extensions.display.ssd1306 import SSD1306
# from kmk.extensions.display import Display, TextEntry, ImageEntry

# Define this as a split keyboard
split = Split(use_pio=True)

# Enable layers
LEDS = { (1, 3): 5 }
layers = Layers(LEDS)

# Define key combos
combos = Combos()
combos.combos = [
    Sequence((KC.LCTL, KC.QUOT), KC.ESC)
]

# Enable macros
macros = Macros()

# Enable tap dance
tapdance = TapDance()
tapdance.tap_time = 250  # Adjust this value (in ms) to your preference

keyboard = KMKKeyboard()
keyboard.modules = [layers, combos, split, macros, tapdance]

# RGB LEDs!
rgb = RGB(
    pixel_pin=keyboard.rgb_pin,
    num_pixels=keyboard.num_pixels,
)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

RGB_TOG = KC.RGB_TOG    # Toggle on/off
RGB_HUI = KC.RGB_HUI    # Hue increase
RGB_HUD = KC.RGB_HUD    # Hue decrease
RGB_SAI = KC.RGB_SAI    # Saturation increase
RGB_SAD = KC.RGB_SAD    # Saturation decrease
RGB_VAI = KC.RGB_VAI    # Value increase
RGB_VAD = KC.RGB_VAD    # Value decrease
RGB_M_P = KC.RGB_M_P 	# RGB_MODE_PLAIN            Static RGB
RGB_M_K = KC.RGB_M_K 	# RGB_MODE_KNIGHT           Knight Rider animation
RGB_M_S = KC.RGB_M_S 	# RGB_MODE_SWIRL            Swirl animation
RGB_M_B = KC.RGB_M_B 	# RGB_MODE_BREATHE          Breathing animation
RGB_M_R = KC.RGB_M_R 	# RGB_MODE_RAINBOW 	    Rainbow animation
RGB_M_BR = KC.RGB_M_BR  # RGB_MODE_BREATHE_RAINBOW  Breathing rainbow animation

# Define layers
L1 = KC.MO(1) # Move & Numbers
L2 = KC.MO(2) # Symbols
L3 = KC.MO(3) # Braces
L4 = KC.MO(4) # Hyperland
L5 = KC.MO(5) # LEDS

# Define tap dance for L1/L4 and L2/L4
# Single tap for L1 or L2, double tap either for L4
L1_L4_TAP = KC.TD(L1, L4)
L2_L4_TAP = KC.TD(L2, L4)

# Create shorter Hyperland key names
HL_1 = KC.LEFT_SUPER(KC.N1)
HL_2 = KC.LEFT_SUPER(KC.N2)
HL_3 = KC.LEFT_SUPER(KC.N3)
HL_4 = KC.LEFT_SUPER(KC.N4)
HL_5 = KC.LEFT_SUPER(KC.N5)
HL_6 = KC.LEFT_SUPER(KC.N6)
HL_7 = KC.LEFT_SUPER(KC.N7)
HL_8 = KC.LEFT_SUPER(KC.N8)
HL_9 = KC.LEFT_SUPER(KC.N9)
HL_LT = KC.LEFT_SUPER(KC.LEFT)
HL_RT = KC.LEFT_SUPER(KC.RIGHT)
HL_UP = KC.LEFT_SUPER(KC.UP)
HL_DN = KC.LEFT_SUPER(KC.DOWN)
HL_NEXT = KC.LEFT_SUPER(KC.LEFT_ALT(KC.TAB))
HL_PREV = KC.LEFT_SUPER(KC.LEFT_ALT(KC.LSFT(KC.TAB)))
HL_TAB = KC.LEFT_SUPER(KC.TAB)

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
                                     L3,    L1_L4_TAP,    KC.ENT,        KC.SPC,    L2_L4_TAP,    KC.RGUI,
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
    #                          |      |  --  |/       /         \      \ |  L4  |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.ESC,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                  KC.N6,   KC.N7,   KC.N8,   KC.N9,    KC.N0,   KC.DEL,
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                 KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                 XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, KC.RSFT,
                                     L3,    L1_L4_TAP,    KC.ENT,        KC.SPC,    L2_L4_TAP,    KC.RGUI,
    ],

    # L2 - Symbols
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Esc  |  !   |  @   |  #   |  $   |  %   |                    |      |      |      |      |      | Bksp |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LCtl |  *   |  &   |  +   |  -   |  `   |                    |      |      |      |      |      |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |      |  ^   |  =   |  _   |  ~   |-------.    ,-------| LOpt |      |      |      |      | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |      |  L4  |/       /         \      \ |  --  |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.ESC,  KC.EXLM, KC.AT,   KC.HASH, KC.DLR, KC.PERC,                  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.BSPC,
        KC.LCTL, KC.ASTR, KC.AMPR, KC.PLUS, KC.MINS, KC.GRV,                  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.LSFT, XXXXXXX, KC.CIRC, KC.EQL,  KC.UNDS, KC.TILD,                 KC.LOPT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.RSFT,
                                      L3,    L1_L4_TAP,    KC.ENT,        KC.SPC,    L2_L4_TAP,    KC.RGUI,
    ],

    # L3 - Braces & Hyperland window navigation in groups
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |      |      |      |      |      |                    |      |  [   |  ]   |      |      | Bksp |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LCtl |      |      |      |      |      |                    | PREV |  (   |  )   | NEXT |  |   |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |      |      |      |      |      |-------.    ,-------|      |  {   |  }   |      |  \   | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |  --  |  L4  |/       /         \      \ |  L4  |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.TAB,  XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LBRC, KC.RBRC, XXXXXXX, XXXXXXX, KC.BSPC,
        KC.LCTL, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                HL_PREV, KC.LPRN, KC.RPRN, HL_NEXT, KC.PIPE, XXXXXXX,
        KC.LSFT, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LCBR, KC.RCBR, XXXXXXX, KC.BSLS, KC.RSFT,
                                      L3,    L1_L4_TAP,    KC.ENT,        KC.SPC,   L2_L4_TAP,    KC.RGUI,
    ],

    # L4 - Hyperland
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |      |      |      |      |      |                    |      |      |      |      |      |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |      |  1   |  2   |  3   |  4   |      |                    | Left | Down |  Up  | Right|      |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |  5   |  6   |  7   |  8   |  9   |-------.    ,-------| G-lf | G-dn | G-up | G-rt |      | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L4  | / Enter /       \ Ray  \  |  L4  | RCmd |
    #                          |      |  --  |/       /         \ Cast \ |  --  |      |
    #                          `---------------------'           '------''-------------'
    [
        HL_TAB, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,  HL_1,    HL_2,    HL_3,    HL_4,  XXXXXXX,           HL_LT,    HL_DN,   HL_UP,   HL_RT,  XXXXXXX, XXXXXXX,
        KC.LSFT,  HL_5,    HL_6,    HL_7,    HL_8,    HL_9,            XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.RSFT,
                                     L3,   L1_L4_TAP,   KC.ENT,     XXXXXXX,    L2_L4_TAP,    KC.RGUI,
    ],

    # L5 - LEDS
      # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Togl | Hue+ | Sat+ | Val+ |      | Swrl |                    | Swrl |      | Val+ | Sat+ | Hue+ | Togl |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |      | Hue- | Sat- | Val- |      | KntRd|                    | KntRd|      | Val- | Sat- | Hue- |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | BRB  | RnBw | Brth |      |      | Plain|-------.    ,-------| Plain|      |      | Brth | RnBw | BRB  |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |  --  |  L4  |/       /         \      \ |  L4  |      |
    #                          `---------------------'           '------''-------------'
    [
        RGB_TOG, RGB_HUI, RGB_SAI, RGB_VAI, XXXXXXX, RGB_M_S,                 RGB_M_S, XXXXXXX, RGB_VAI, RGB_SAI, RGB_HUI, RGB_TOG,
        XXXXXXX, RGB_HUD, RGB_SAD, RGB_VAD, XXXXXXX, RGB_M_K,                 RGB_M_K, XXXXXXX, RGB_VAD, RGB_SAD, RGB_HUD, XXXXXXX,
        RGB_M_BR,RGB_M_R, RGB_M_B, XXXXXXX, XXXXXXX, RGB_M_P,                 RGB_M_P, XXXXXXX, XXXXXXX, RGB_M_B, RGB_M_R, RGB_M_BR,
                                     L3,    L1_L4_TAP,    KC.ENT,        KC.SPC,    L2_L4_TAP,    KC.RGUI,
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
