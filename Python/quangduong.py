import random

computer = random.randint(1, 3)

quy_uoc = {
    1: "keo", 
    2: "bua",
    3: "bao"
}

def start():
    print("~~~~~~~~~~~~~~~~~~  ROCK PAPER SCISSORS ~~~~~~~~~~~~~~~~~~")
    print("Nhap 1 de choi")
    print("Nhap 2 de thoat")

def menu():
    print("1 = keo")
    print("2 = bua")
    print("3 = bao")

def game():
    if user == computer:
        print("hoa")

    elif user != computer:
        if user == 1:
            if computer == 2:
                print("thua")

            else:
                print("thang")

        elif user == 2:
            if computer == 1:
                print("thang")
            else:
                print("thua")

        else: 
            if computer == 2:
                print("thang")
            else:
                print("thua")


while True:
    start()

    chon = int(input())

    if chon == 1:
        menu()
        user = int(input())
        game()
    else:
        break

    

