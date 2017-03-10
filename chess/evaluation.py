from piece_types import *

# Piece-square tables are from
# http://chessprogramming.wikispaces.com/Simplified+evaluation+function
# with some slight changes.
# Piece values:
# PAWN = 100
# BISHOP = KNIGHT = 300
# ROOK = 500
# QUEEN = 900

LOSING = -300000
DRAW = 0

PST_EMPTY = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
PST_W_KING = [
    [20,  30,  10,  00,  00,  10,  30,  20],
    [20,  20,  00,  00,  00,  00,  20,  20],
    [-10, -20, -20, -20, -20, -20, -20, -10],
    [-30, -30, -40, -50, -50, -40, -30, -30],
    [-30, -30, -40, -50, -50, -40, -30, -30],
    [-30, -30, -40, -50, -50, -40, -30, -30],
    [-30, -30, -40, -50, -50, -40, -30, -30],
    [-30, -30, -40, -50, -50, -40, -30, -30]
]
PST_W_QUEEN = [
    [900, 900, 900, 900, 900, 900, 900, 900],
    [900, 900, 900, 900, 900, 900, 900, 900],
    [900, 900, 900, 900, 900, 900, 900, 900],
    [900, 900, 900, 900, 900, 900, 900, 900],
    [900, 900, 900, 900, 900, 900, 900, 900],
    [900, 900, 900, 900, 900, 900, 900, 900],
    [900, 900, 900, 900, 900, 900, 900, 900],
    [900, 900, 900, 900, 900, 900, 900, 900]
]
PST_W_ROOK = [
    [500, 500, 500, 505, 505, 500, 500, 500],
    [495, 500, 500, 500, 500, 500, 500, 495],
    [495, 500, 500, 500, 500, 500, 500, 495],
    [495, 500, 500, 500, 500, 500, 500, 495],
    [495, 500, 500, 500, 500, 500, 500, 495],
    [495, 500, 500, 500, 500, 500, 500, 495],
    [505, 510, 510, 510, 510, 510, 510, 505],
    [500, 500, 500, 500, 500, 500, 500, 500]
]
PST_W_BISHOP = [
    [280, 290, 290, 290, 290, 290, 290, 280],
    [290, 305, 300, 300, 300, 300, 305, 290],
    [290, 310, 310, 310, 310, 310, 310, 290],
    [290, 300, 310, 310, 310, 310, 300, 290],
    [290, 305, 305, 310, 310, 305, 305, 290],
    [290, 300, 305, 310, 310, 305, 300, 290],
    [290, 300, 300, 300, 300, 300, 300, 290],
    [280, 290, 290, 290, 290, 290, 290, 280]
]
PST_W_KNIGHT = [
    [250, 260, 270, 270, 270, 270, 260, 250],
    [260, 280, 300, 305, 305, 300, 280, 260],
    [270, 305, 310, 315, 315, 310, 305, 270],
    [270, 300, 315, 320, 320, 315, 300, 270],
    [270, 305, 315, 320, 320, 315, 305, 270],
    [270, 300, 310, 315, 315, 310, 300, 270],
    [260, 280, 300, 300, 300, 300, 280, 260],
    [250, 260, 270, 270, 270, 270, 260, 250]
]
PST_W_PAWN = [
    [000, 000, 000, 000, 000, 000, 000, 000],
    [105, 110, 110,  80, 80, 110,  110, 105],
    [105,  95,  90, 100, 100, 90,   95, 105],
    [100, 100, 100, 120, 120, 100, 100, 100],
    [105, 105, 110, 125, 125, 110, 105, 105],
    [110, 110, 120, 130, 130, 120, 110, 110],
    [150, 150, 150, 150, 150, 150, 150, 150],
    [000, 000, 000, 000, 000, 000, 000, 000]
]
PST_B_KING = [[-i for i in row] for row in reversed(PST_W_KING)]
PST_B_QUEEN = [[-i for i in row] for row in reversed(PST_W_QUEEN)]
PST_B_ROOK = [[-i for i in row] for row in reversed(PST_W_ROOK)]
PST_B_BISHOP = [[-i for i in row] for row in reversed(PST_W_BISHOP)]
PST_B_KNIGHT = [[-i for i in row] for row in reversed(PST_W_KNIGHT)]
PST_B_PAWN = [[-i for i in row] for row in reversed(PST_W_PAWN)]
PST = {
    0:       PST_EMPTY,
    KING:    PST_W_KING,
    QUEEN:   PST_W_QUEEN,
    ROOK:    PST_W_ROOK,
    BISHOP:  PST_W_BISHOP,
    KNIGHT:  PST_W_KNIGHT,
    PAWN:    PST_W_PAWN,
    -KING:   PST_B_KING,
    -QUEEN:  PST_B_QUEEN,
    -ROOK:   PST_B_ROOK,
    -BISHOP: PST_B_BISHOP,
    -KNIGHT: PST_B_KNIGHT,
    -PAWN:   PST_B_PAWN
}

__all__ = ["PST", "LOSING", "DRAW"]