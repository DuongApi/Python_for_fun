# game_map = [
#     "1", "2", "3",
#     "4", "5", "6", 
#     "7", "8", "9"
# ]

player = {
    "X": "Player",
    "O": "Computer"
}

win_rule = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

cnt = 2

# for i in range(9):
#     print(game_map[i], end= "       ")
#     if cnt == i:
#         cnt += 3
#         print("\n")


lst = [0] * 9

A = []
B = []



def a_input():
    a = int(input("Player 1: "))
    if lst[a - 1] != 1:
        lst[a - 1] = 1
    else:
        print("Vui long nhap so khac")
        a_input()

def b_input():
    b = int(input("Player 2: "))
    if lst[b - 1] != 1:
        lst[b - 1] = 1
    else:
        print("Vui long nhap so khac")
        b_input()


while True:
    a_input()

    b_input()

    





print(lst)

