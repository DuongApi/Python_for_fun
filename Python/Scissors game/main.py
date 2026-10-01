import random

def get_menu_choice():
    """Hiển thị menu và nhận lựa chọn bắt đầu hoặc thoát từ người dùng."""
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
    """Nhận lựa chọn hợp lệ từ người chơi."""
    print("=" * 40)
    while True:
        choice = input("Nhập lựa chọn của bạn (kéo / búa / bao): ").strip().lower()
        if choice in ("kéo", "búa", "bao"):
            return choice
        print("Lựa chọn không hợp lệ! Vui lòng nhập lại (kéo, búa hoặc bao).")

def play_game():
    """Logic chính của một ván chơi."""
    choices = ["kéo", "búa", "bao"]
    
    user = get_user_choice()
    computer = random.choice(choices)
    
    print(f"\n=> Bạn chọn: {user} | Máy chọn: {computer}")
    
    # Xử lý kết quả
    if user == computer:
        print("Kết quả: HÒA! 🤝\n")
    elif (
        (user == "kéo" and computer == "bao") or 
        (user == "búa" and computer == "kéo") or 
        (user == "bao" and computer == "búa")
    ):
        print("Kết quả: BẠN THẮNG! 🎉\n")
    else:
        print("Kết quả: BẠN THUA! 😢\n")

def main():
    """Hàm điều phối vòng lặp toàn bộ chương trình."""
    while True:
        menu_choice = get_menu_choice()
        
        if menu_choice == 2:
            print("Cảm ơn bạn đã chơi game. Hẹn gặp lại!")
            break
        
        # Cho phép chơi liên tục khi chọn 1
        while True:
            play_game()
            
            # Hỏi người dùng có muốn tiếp tục chơi ván mới không
            cont = input("Bạn có muốn chơi tiếp ván này không? (c/k): ").strip().lower()
            if cont != 'c':
                print("\nQuay lại màn hình chính...\n")
                break

if __name__ == "__main__":
    main()