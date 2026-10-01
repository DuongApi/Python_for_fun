import random

## lựa chọn khi mới khởi động
def main():
    print("====" * 20)
    print("Chào mừng đến với scissors game!")
    print("Nhập 1 để chơi.")
    print("Nhập 2 để thoát.")
    while True:
        choice = int(input("Nhập lựa chọn của bạn: "))
        if choice in (1, 2):  # Kiểm tra xem người dùng nhập gì?
            return choice         # Trả lại biến choice và đưa ra ngoài kèm kết thúc loop
        else:
            print("Nhập số không hợp lệ, vui lòng nhập lại!")
choice_menu = main()   # Set giá trị qua việc lấy từ func
    
# Lựa chọn của người chơi trong game

def user_choice():
    print("====" * 20)
    print("Vui lòng chọn kéo, búa hoặc bao :)")
    while True:
        user_choice = input("Nhập lựa chọn của bạn (kéo/búa/bao): ")
        if user_choice in ("kéo", "búa", "bao"):
            return user_choice
        else:
            print("Vui lòng nhập lại lụa chọn hợp lệ")
user_choice = user_choice()

list_choice = ["kéo", "búa", "bao"]

## Xử lý logic

computer_choice = random.choice(list_choice)

a = f"máy chọn: {computer_choice}, bạn chọn: {user_choice}. "

if user_choice == computer_choice:
    print("hòa")
    main()
else:
    if user_choice == "kéo":
        if computer_choice == "lá":
            print(f"{a} => Bạn thắng")
        else:
            print(f"{a} =>Bạn thua")
    elif user_choice == "búa":
        if computer_choice == "lá":
            print(f"{a} =>Bạn thua")
        else:
            print(f"{a} =>Bạn thắng")
    else:
        if computer_choice == "kéo":
            print(f"{a} =>Bạn thua")
        else:
            print(f"{a} =>Bạn thắng")
    





