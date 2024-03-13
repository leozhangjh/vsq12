import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

# 创建主窗口
root = tk.Tk()
root.title('文字识别')

# 创建Label用于显示识别结果
result_label = tk.Label(root, text='识别结果:')
result_label.pack()

# 创建Canvas用于显示图片
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def open_image():
    # 打开文件对话框选择图片
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.gif;*.bmp')])
    if file_path:
        # 读取图片并显示在Canvas上
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        
        # 使用pytesseract进行文字识别
        text = pytesseract.image_to_string(image)
        result_label.config(text='识别结果:\n' + text)

# 创建按钮用于打开图片
open_button = tk.Button(root, text='打开图片', command=open_image)
open_button.pack()

# 运行主循环
root.mainloop()
