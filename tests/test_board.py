from src.board import Board


def test_valid_move_in_empty_board():
    board = Board()
    assert board.is_valid_move(0) is True
    assert board.is_valid_move(6) is True


def test_invalid_move_outside_board():
    board = Board()
    assert board.is_valid_move(-1) is False
    assert board.is_valid_move(7) is False


def test_drop_piece_success():
    board = Board()
    ok = board.drop_piece(0, "X")
    assert ok is True
    assert board.grid[5][0] == "X"


def test_column_gets_full_then_invalid():
    board = Board()
    for _ in range(6):
        assert board.drop_piece(0, "X") is True
    assert board.is_valid_move(0) is False
    assert board.drop_piece(0, "O") is False


def test_horizontal_win():
    board = Board()
    board.drop_piece(0, "X")
    board.drop_piece(1, "X")
    board.drop_piece(2, "X")
    board.drop_piece(3, "X")
    assert board.check_win("X") is True


def test_vertical_win():
    board = Board()
    board.drop_piece(2, "O")
    board.drop_piece(2, "O")
    board.drop_piece(2, "O")
    board.drop_piece(2, "O")
    assert board.check_win("O") is True


def test_diagonal_down_right_win():
    board = Board()

    # Baut diagonal \ für X
    board.drop_piece(0, "X")

    board.drop_piece(1, "O")
    board.drop_piece(1, "X")

    board.drop_piece(2, "O")
    board.drop_piece(2, "O")
    board.drop_piece(2, "X")

    board.drop_piece(3, "O")
    board.drop_piece(3, "O")
    board.drop_piece(3, "O")
    board.drop_piece(3, "X")

    assert board.check_win("X") is True


def test_diagonal_up_right_win():
    board = Board()

    # Baut diagonal / für X
    board.drop_piece(3, "X")

    board.drop_piece(2, "O")
    board.drop_piece(2, "X")

    board.drop_piece(1, "O")
    board.drop_piece(1, "O")
    board.drop_piece(1, "X")

    board.drop_piece(0, "O")
    board.drop_piece(0, "O")
    board.drop_piece(0, "O")
    board.drop_piece(0, "X")

    assert board.check_win("X") is True


def test_is_full_false_on_new_board():
    board = Board()
    assert board.is_full() is False


def test_is_full_true_when_everything_filled():
    board = Board()
    for c in range(board.cols):
        for _ in range(board.rows):
            board.drop_piece(c, "X")
    assert board.is_full() is True
