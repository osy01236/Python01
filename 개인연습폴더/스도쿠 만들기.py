import random

BASE = 3
SIDE = BASE * BASE
HOLES = 45


def pattern(row, col):
    return (BASE * (row % BASE) + row // BASE + col) % SIDE


def shuffled(values):
    return random.sample(values, len(values))


def make_solution_board():
    row_groups = shuffled(range(BASE))
    col_groups = shuffled(range(BASE))

    rows = [group * BASE + row for group in row_groups for row in shuffled(range(BASE))]
    cols = [group * BASE + col for group in col_groups for col in shuffled(range(BASE))]
    nums = shuffled(range(1, SIDE + 1))

    return [[nums[pattern(row, col)] for col in cols] for row in rows]


def make_puzzle(solution, holes):
    board = [row[:] for row in solution]
    positions = random.sample(range(SIDE * SIDE), holes)

    for position in positions:
        row = position // SIDE
        col = position % SIDE
        board[row][col] = 0

    return board


def print_board(board):
    print()
    print("    1 2 3   4 5 6   7 8 9")

    for row in range(SIDE):
        if row % BASE == 0 and row != 0:
            print("   " + "-" * 21)

        print(f"{row + 1} |", end=" ")

        for col in range(SIDE):
            if col % BASE == 0 and col != 0:
                print("|", end=" ")

            value = board[row][col]
            if value == 0:
                print(".", end=" ")
            else:
                print(value, end=" ")
        print()

    print()


def is_valid_move(board, row, col, num):
    for index in range(SIDE):
        if index != col and board[row][index] == num:
            return False
        if index != row and board[index][col] == num:
            return False

    start_row = (row // BASE) * BASE
    start_col = (col // BASE) * BASE

    for box_row in range(start_row, start_row + BASE):
        for box_col in range(start_col, start_col + BASE):
            if (box_row != row or box_col != col) and board[box_row][box_col] == num:
                return False

    return True


def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True


def show_help():
    print("입력 방법")
    print("- 숫자 넣기: 행 열 숫자")
    print("  예) 3 4 7")
    print("- 지우기: c 행 열")
    print("  예) c 3 4")
    print("- 도움말: h")
    print("- 정답 보기: s")
    print("- 종료: q")
    print()


def main():
    solution = make_solution_board()
    board = make_puzzle(solution, HOLES)
    fixed = [[cell != 0 for cell in row] for row in board]

    print("스도쿠 게임을 시작합니다.")
    show_help()

    while True:
        print_board(board)

        if is_complete(board):
            print("축하합니다. 스도쿠를 완성했습니다.")
            break

        command = input("명령 입력 : ").strip().lower()

        if command == "q":
            print("게임을 종료합니다.")
            break

        if command == "h":
            show_help()
            continue

        if command == "s":
            print("정답을 보여줍니다.")
            print_board(solution)
            break

        parts = command.split()

        if len(parts) == 3 and parts[0] == "c":
            try:
                row = int(parts[1]) - 1
                col = int(parts[2]) - 1
            except ValueError:
                print("지우기는 c 행 열 형식으로 입력하세요.")
                continue

            if not (0 <= row < SIDE and 0 <= col < SIDE):
                print("행과 열은 1~9만 입력할 수 있습니다.")
                continue

            if fixed[row][col]:
                print("처음부터 있던 숫자는 지울 수 없습니다.")
                continue

            board[row][col] = 0
            print("지웠습니다.")
            continue

        if len(parts) == 3:
            try:
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
                num = int(parts[2])
            except ValueError:
                print("숫자는 공백으로 구분해서 입력하세요.")
                continue

            if not (0 <= row < SIDE and 0 <= col < SIDE and 1 <= num <= 9):
                print("행과 열은 1~9, 숫자는 1~9만 입력할 수 있습니다.")
                continue

            if fixed[row][col]:
                print("처음부터 있던 숫자는 바꿀 수 없습니다.")
                continue

            if is_valid_move(board, row, col, num):
                board[row][col] = num
                print("입력 완료")
            else:
                print("스도쿠 규칙에 맞지 않는 숫자입니다.")
            continue

        print("입력 형식이 올바르지 않습니다. h를 입력해 도움말을 보세요.")


if __name__ == "__main__":
    main()
