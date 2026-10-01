import random

def get_menu_choice():
    print("=" * 40)
    print("Chào mừng đến với trò chơi Kéo - Búa - Bao!")
    print("1. Chơi game")
    print("2. Thoát")
    while True:
        try:
            choice = int(input("Nhập lựa chọn của bạn (1 hoặc 2): "))
            if choice in (1, 2):
                return choice
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        except ValueError:
            print("Vui lòng chỉ nhập số (1 hoặc 2)!")

def get_user_choice():
    print("=" * 40)
    while True:
        choice = input("Nhập lựa chọn của bạn (kéo / búa / bao): ").strip().lower()
        if choice in ("kéo", "búa", "bao"):
            return choice
        print("Lựa chọn không hợp lệ! Vui lòng nhập lại (kéo, búa hoặc bao).")

def play_game():
    choices = ["kéo", "búa", "bao"]
    
    user = get_user_choice()
    computer = random.choice(choices)
    
    print(f"\n=> Bạn chọn: {user} | Máy chọn: {computer}")

    if user == computer:
        print("Kết quả: HÒA!\n")
    elif (
        (user == "kéo" and computer == "bao") or 
        (user == "búa" and computer == "kéo") or 
        (user == "bao" and computer == "búa")
    ):
        print("Kết quả: BẠN THẮNG!\n")
    else:
        print("Kết quả: BẠN THUA!\n")

def main():
    while True:
        menu_choice = get_menu_choice()
        
        if menu_choice == 2:
            print("Cảm ơn bạn đã chơi game. Hẹn gặp lại!")
            break
        
        while True:
            play_game()

            cont = input("Bạn có muốn chơi tiếp ván này không? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Quay lại màn hình chính...\n")
                break

if __name__ == "__main__":
    main()
