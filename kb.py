import board

from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins

class KMKKeyboard(_KMKKeyboard):
    i2c = board.I2C
    num_pixels = 27
    rgb_pin = pins[0]
    data_pin = pins[1]
    sda_pin = pins[4]
    scl_pin = pins[5]
    diode_orientation = DiodeOrientation.COLUMNS

    col_pins = (
        pins[19],
        pins[18],
        pins[17],
        pins[16],
        pins[15],
        pins[14],
    )

    row_pins = (
        pins[6],
        pins[7],
        pins[8],
        pins[9],
    )

    # fmt:off
    coord_mapping = [
         0,  1,  2,  3,  4,  5,    29, 28, 27, 26, 25, 24,
         6,  7,  8,  9, 10, 11,    35, 34, 33, 32, 31, 30,
        12, 13, 14, 15, 16, 17,    41, 40, 39, 38, 37, 36,
                    21, 22, 23,    47, 46, 45,
    ]
    # fmt:on
