import tkinter as tk

BODY_PARTS = {
    "腮腺": (193, 215, 237, 247),
    "咽": (200, 255, 235, 278),
    "喉": (207, 333, 243, 348),
    "气管": (256, 380, 286, 403),
    "支气管": (207, 493, 260, 531),
    "右肺": (373, 502, 409, 524),
    "左肺": (132, 561, 162, 584)
}


class BodyClickApp:
    def __init__(self, root):
        self.root = root
        root.title("人体部位识别 - 点击出现名称")



        try:
            self.img = tk.PhotoImage(file="人体1.gif")
        except Exception as e:
            print("图片加载失败，请检查文件路径和格式:", e)
            return


        self.canvas = tk.Canvas(root, width=self.img.width(), height=self.img.height())
        self.canvas.pack(pady=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)


        self.label = tk.Label(root, text="点击图片上的人体部位", font=("Arial", 14), fg="blue")
        self.label.pack(pady=5)



        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        x, y = event.x, event.y
        for part_name, (x1, y1, x2, y2) in BODY_PARTS.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                self.show_floating_text(part_name, x, y)
                self.label.config(text=f"你点击了: {part_name}")
                return
        self.label.config(text="未点击到任何部位，再试试看~")
        self.show_floating_text("❌ 未识别部位", x, y, bg="red")

    def show_floating_text(self, text, x, y, bg="lightyellow", fg="white", duration=1200):

        offset_x, offset_y = 15, -20
        text_id = self.canvas.create_text(
            x + offset_x, y + offset_y,
            text=text,
            fill=fg,
            font=("Arial", 24, "bold"),
            anchor="nw",
            tags="floating"
        )
        self.root.after(duration, lambda: self.canvas.delete(text_id))

if __name__ == "__main__":
    root = tk.Tk()
    app = BodyClickApp(root)
    root.mainloop()