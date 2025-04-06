from sudoku import sudoku_ins

test_PN_grid = [
    [[0] * 9 for _ in range(9)],
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
    ],
]
test_PN_answer = [
    [[list(range(1, 10)) for _ in range(9)] for _ in range(9)],
    [
        [[] for _ in range(9)],  # 第一行已填满
        [
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
        ],
        [
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ],
    ],
]

test_LRC_grid = [
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 0],  # 最后一格必须是9
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
        [0] * 9,
    ],
]
test_LRC_answer = [
    [
        [[], [], [], [], [], [], [], [], [9]],
        [
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 9],
            [1, 2, 3, 4, 5, 6, 9],
            [1, 2, 3, 4, 5, 6, 9],
        ],
        [
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 9],
            [1, 2, 3, 4, 5, 6, 9],
            [1, 2, 3, 4, 5, 6, 9],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ],
        [
            [2, 3, 4, 5, 6, 7, 8, 9],
            [1, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ],
    ]
]


def test_possibleNumberInference():
    for gird, answer in zip(test_PN_grid, test_PN_answer):
        assert sudoku_ins.possibleNumberInference(gird) == answer


def test_lastRemainingCellInference():
    for grid, answer in zip(test_LRC_grid, test_LRC_answer):
        assert sudoku_ins.lastRemainingCellInference(grid) == answer
