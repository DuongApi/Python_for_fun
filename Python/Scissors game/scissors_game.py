import random

WIN_RULE = {
    "búa" : "kéo",
    "giấy" : "búa",
    "kéo" : "giấy"
}

SHORT_NAME = {
    "b" : "búa", "1" : "búa", "búa": "búa",
    "k" : "kéo", "2" : "kéo", "kéo": "kéo",
    "g" : "giấy", "3": "giấy", "giấy" : "giấy"
}

def join():
    print("=====" * 20)
    print("Chào mừng bạn đến với scissors game!")
    print("Nhập 1 để chơi")
    print("Nhập 2 để thoát game")
    while True:
        choice = input("Hãy nhập lựa chọn của bạn: ").strip()
        if choice in ("1", "2"):
            return int(choice)
        else:
            print("Chỉ có thể nhập 1 hoặc 2! Vui lòng nhập lại")

def user_choice():
    print("=====" * 20)
    print("Hãy nhập lựa chọn của bạn: ")
    print("Nhập b hoặc 1 để chọn búa")
    print("Nhập k hoặc 2 để chọn kéo")
    print("Nhập g hoặc 3 để chọn giấy")
    while True:
        user_choice = input("Hãy nhập lựa chọn của bạn: ").strip().lower()
        if user_choice in SHORT_NAME:
            return SHORT_NAME[user_choice]
        else:
            print("Vui lòng nhập lại lựa chọn phù hợp")

def in_game():
    user = user_choice()
    com_choice = list(WIN_RULE.keys())
    computer_choice =  random.choice(com_choice)
    print("=====" * 20)
    print(f"bạn chọn: {user} | Máy chọn: {computer_choice}")
    if user == computer_choice:
        print("hòa")
    elif WIN_RULE[user] == computer_choice:
        print("Bạn đã thắng!")
    else:
        print("Bạn đã thua!")

def main():
    while True:
        choice = join()
        if choice == 2:
            print("Cảm ơn bạn đã sử dụng dịch vụ.")
            break
        while True:
            in_game()
            chon = input("bạn muốn chơi ván khác(y/n): ").strip().lower()
            if chon not in ("y", "yes"):
                print("Cảm ơn bạn đã sử dụng dịch vụ!")
                break

if __name__ == "__main__":
    main()







    
    




