import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Kéo Búa Bao Pro")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")

        # Dữ liệu logic
        self.choices = {"Búa": "✊", "Kéo": "✌️", "Giấy": "✋"}
        self.win_rule = {"Búa": "Kéo", "Giấy": "Búa", "Kéo": "Giấy"}
        
        self.user_score = 0
        self.computer_score = 0

        # --- Giao diện ---
        
        # Tiêu đề
        self.title_label = tk.Label(root, text="KÉO BÚA BAO", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=20)

        # Hiển thị tỉ số
        self.score_label = tk.Label(root, text="Bạn: 0 | Máy: 0", font=("Helvetica", 14), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        # Khu vực hiển thị kết quả ván đấu
        self.result_frame = tk.Frame(root, bg="#f0f0f0")
        self.result_frame.pack(pady=20)

        self.vs_label = tk.Label(self.result_frame, text="Sẵn sàng chưa?", font=("Helvetica", 12), bg="#f0f0f0")
        self.vs_label.pack()

        self.battle_label = tk.Label(self.result_frame, text="❓ VS ❓", font=("Helvetica", 30), bg="#f0f0f0")
        self.battle_label.pack(pady=10)

        # Khu vực các nút bấm
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.btn_bua = tk.Button(self.button_frame, text="✊ Búa", font=("Helvetica", 12), width=10, 
                                 command=lambda: self.play("Búa"), bg="#ffcccb")
        self.btn_bua.grid(row=0, column=0, padx=5)

        self.btn_keo = tk.Button(self.button_frame, text="✌️ Kéo", font=("Helvetica", 12), width=10, 
                                 command=lambda: self.play("Kéo"), bg="#ccffcc")
        self.btn_keo.grid(row=0, column=1, padx=5)

        self.btn_giay = tk.Button(self.button_frame, text="✋ Giấy", font=("Helvetica", 12), width=10, 
                                  command=lambda: self.play("Giấy"), bg="#ccccff")
        self.btn_giay.grid(row=0, column=2, padx=5)

        # Nút Reset
        self.reset_btn = tk.Button(root, text="Chơi lại từ đầu", command=self.reset_game, font=("Helvetica", 10))
        self.reset_btn.pack(pady=10)

    def play(self, user_choice):
        # Máy chọn ngẫu nhiên
        computer_choice = random.choice(list(self.choices.keys()))

        # Hiển thị Emoji lên màn hình
        self.battle_label.config(text=f"{self.choices[user_choice]} VS {self.choices[computer_choice]}")

        # Kiểm tra thắng thua
        if user_choice == computer_choice:
            result_text = "HÒA RỒI!"
            color = "orange"
        elif self.win_rule[user_choice] == computer_choice:
            result_text = "BẠN THẮNG! 🎉"
            color = "green"
            self.user_score += 1
        else:
            result_text = "MÁY THẮNG! 💀"
            color = "red"
            self.computer_score += 1

        # Cập nhật giao diện
        self.vs_label.config(text=result_text, fg=color)
        self.score_label.config(text=f"Bạn: {self.user_score} | Máy: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Bạn: 0 | Máy: 0")
        self.vs_label.config(text="Sẵn sàng chưa?", fg="black")
        self.battle_label.config(text="❓ VS ❓")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()
