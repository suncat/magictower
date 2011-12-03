import pygame
from pygame.locals import USEREVENT

STEP = CELL_SIZE = 80
MAP_ROWS = 6
MAP_COLS = 8
TEXTBOARD_WIDTH = 162
GAMEBOARD_WIDTH = MAP_COLS*CELL_SIZE
SCREEN_WIDTH = GAMEBOARD_WIDTH + TEXTBOARD_WIDTH
TEXTBOARD_HEIGHT = GAMEBOARD_HEIGHT = SCREEN_HEIGHT = MAP_ROWS*CELL_SIZE

ALLMAP = (
    ["00020003", "01111111", "01010201", "20000101", "11111101", "00002001"],
    ["61711003", "61217010", "21011210", "22002010", "11112110", "40000000"],
    ["00080080", "81111110", "01110310", "07776118", "11111110", "40080080"],
    ["7db81a03", "c18a101a", "111d1800", "17c8861d", "11111119", "409a7008"],
    ["981890d3", "1adc1a11", "181a1g16", "ca1a1f1b", "111a101b", "40e900d8"],
    ["111j1iii", "kaaa1i1i", "11d11iii", "bhh91l1d", "11d111dd", "400ab003"],
    ["9bdhhh99", "1110111d", "ca101369", "ac1g11bd", "1d1f911d", "400a90a0"],
    ["0o0h0h0a", "o1111110", "01mmpq1a", "onmmpq10", "3111111h", "40a0a0h0"],
    ["1w1x1c13", "1d1srs1a", "1v11d11v", "1u19rbaa", "1t1111d1", "40oasaoq"],
    ["11111111", "1syaays1", "1y1111y1", "1z1001z1", "1y1001y1", "40B00BA3"],
    ["q1p11Co3", "E1EE11u1", "oo1u1bE1", "u1FoEC0E", "qu11111u", "40C0o0DF"],
    ["IG1C1Euq", "1EuduF1z", "JG1H1013", "11111E11", "Fr1qC01C", "400E1Gd6"],
    )
