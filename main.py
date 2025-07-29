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
L4 = KC.MO(4) # Aerospace
L5 = KC.MO(5) # LEDS

# Define tap dance for L1/L4 and L2/L4
# Single tap for L1 or L2, double tap either for L4
L1_L4_TAP = KC.TD(L1, L4)
L2_L4_TAP = KC.TD(L2, L4)

# Create shorter Aerospace key names
AERO_1 = KC.LOPT(KC.N1)
AERO_2 = KC.LOPT(KC.N2)
AERO_3 = KC.LOPT(KC.N3)
AERO_4 = KC.LOPT(KC.N4)
AERO_5 = KC.LOPT(KC.N5)
AERO_6 = KC.LOPT(KC.N6)
AERO_7 = KC.LOPT(KC.N7)
AERO_8 = KC.LOPT(KC.N8)
AERO_9 = KC.LOPT(KC.N9)
AERO_0 = KC.LOPT(KC.N0)
AERO_A = KC.LOPT(KC.A)
AERO_S = KC.LOPT(KC.S)
AERO_D = KC.LOPT(KC.D)
AERO_F = KC.LOPT(KC.F)
AERO_G = KC.LOPT(KC.G)
AERO_Z = KC.LOPT(KC.Z)
AERO_X = KC.LOPT(KC.X)
AERO_C = KC.LOPT(KC.C)
AERO_V = KC.LOPT(KC.V)
AERO_B = KC.LOPT(KC.B)
AERO_N = KC.LOPT(KC.N)
AERO_M = KC.LOPT(KC.M)
AERO_LT = KC.LOPT(KC.H)
AERO_RT = KC.LOPT(KC.L)
AERO_UP = KC.LOPT(KC.K)
AERO_DN = KC.LOPT(KC.J)
AERO_COM = KC.LOPT(KC.COMM)
AERO_DOT = KC.LOPT(KC.DOT)
AERO_SLH = KC.LOPT(KC.SLSH)
AERO_TAB = KC.LOPT(KC.TAB)
RAYCAST = KC.LOPT(KC.SPC)

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

    # L3 - Braces
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |      |      |      |      |      |                    |      |  [   |  ]   |      |      | Bksp |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LCtl |      |      |      |      |      |                    |      |  (   |  )   |      |  |   |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |      |      |      |      |      |-------.    ,-------|      |  {   |  }   |      |  \   | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L1  | / Enter /       \ Spac \  |  L2  | RCmd |
    #                          |  --  |  L4  |/       /         \      \ |  L4  |      |
    #                          `---------------------'           '------''-------------'
    [
        KC.TAB,  XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LBRC, KC.RBRC, XXXXXXX, XXXXXXX, KC.BSPC,
        KC.LCTL, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LPRN, KC.RPRN, XXXXXXX, KC.PIPE, XXXXXXX,
        KC.LSFT, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                XXXXXXX, KC.LCBR, KC.RCBR, XXXXXXX, KC.BSLS, KC.RSFT,
                                      L3,    L1_L4_TAP,    KC.ENT,        KC.SPC,   L2_L4_TAP,    KC.RGUI,
    ],
    
    # L4 - Aerospace (all keys have ALT/OPT applied above)
    # ,-----------------------------------------.                    ,-----------------------------------------.
    # | Tab  |  1   |  2   |  3   |  4   |  5   |                    |  6   |  7   |  8   |  9   |  0   |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # |      |  A   |  S   |  D   |  F   |  G   |                    | Left | Down |  Up  | Right|  ;   |      |
    # |------+------+------+------+------+------|                    |------+------+------+------+------+------|
    # | LSft |  Z   |  X   |  C   |  V   |  B   |-------.    ,-------|  N   |  M   |  ,   |  .   |  /   | RSft |
    # `-----------------------------------------/       /     \      \-----------------------------------------'
    #                          |  L3  |  L4  | / Enter /       \ Ray  \  |  L4  | RCmd |
    #                          |      |  --  |/       /         \ Cast \ |  --  |      |
    #                          `---------------------'           '------''-------------'
    [
        AERO_TAB, AERO_1,  AERO_2,  AERO_3,  AERO_4,  AERO_5,                 AERO_6,   AERO_7,   AERO_8,  AERO_9,  AERO_0,  XXXXXXX,
        XXXXXXX,  AERO_A,  AERO_S,  AERO_D,  AERO_F,  AERO_G,                 AERO_LT,  AERO_DN,  AERO_UP, AERO_RT, KC.SCLN, XXXXXXX,
        KC.LSFT,  AERO_Z,  AERO_X,  AERO_C,  AERO_V,  AERO_B,                 AERO_N,   AERO_M,  AERO_COM, AERO_DOT, AERO_SLH, KC.RSFT,
                                         L3,    L1_L4_TAP, KC.ENT,        RAYCAST,    L2_L4_TAP,    KC.RGUI,
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
