import tkinter as tk
from tkinter import messagebox

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("進位轉換器 - 支援 2, 10, 16 進位")
        self.root.geometry("400x300")

        # UI 組件
        tk.Label(root, text="輸入數值:").pack(pady=5)
        self.entry_input = tk.Entry(root)
        self.entry_input.pack(pady=5)

        tk.Label(root, text="選擇輸入進位:").pack()
        self.input_base = tk.IntVar(value=10)
        tk.Radiobutton(root, text="2 進位", variable=self.input_base, value=2).pack()
        tk.Radiobutton(root, text="10 進位", variable=self.input_base, value=10).pack()
        tk.Radiobutton(root, text="16 進位", variable=self.input_base, value=16).pack()

        tk.Button(root, text="開始轉換", command=self.convert).pack(pady=10)

        self.result_text = tk.StringVar(value="轉換結果將顯示於此")
        tk.Label(root, textvariable=self.result_text, justify="left", font=("Courier", 10)).pack(pady=10)

    # 自定義：將字串轉換為十進位整數
    def to_decimal(self, s, base):
        s = s.upper().strip()
        digits = "0123456789ABCDEF"
        res = 0
        for char in s:
            val = digits.find(char)
            if val == -1 or val >= base:
                raise ValueError("無效的字元")
            res = res * base + val
        return res

    # 自定義：將十進位整數轉為目標進位字串
    def from_decimal(self, n, base):
        if n == 0: return "0"
        digits = "0123456789ABCDEF"
        res = ""
        temp_n = n
        while temp_n > 0:
            res = digits[temp_n % base] + res
            temp_n //= base
        return res

    def convert(self):
        raw_val = self.entry_input.get()
        try:
            # 1. 先統一轉成十進位（中介）
            dec_val = self.to_decimal(raw_val, self.input_base.get())
            
            # 2. 再從十進位轉出其他進位
            b2 = self.from_decimal(dec_val, 2)
            b10 = str(dec_val)
            b16 = self.from_decimal(dec_val, 16)

            self.result_text.set(f"2進位: {b2}\n10進位: {b10}\n16進位: {b16}")
            
            # 加分項：檢查是否超出 255
            if dec_val > 255:
                self.root.configure(bg='#e6fffa') # 輕微變色提示支援大數
        except Exception as e:
            messagebox.showerror("錯誤", "請輸入正確的進位數值！")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()