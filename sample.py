import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk

cnt = 1

def pushed():
    global cnt
    if cnt % 3 == 0:
        textarea.insert(tk.END, 'ぶりゅりゅりゅゆ…')
        cnt += 1
    elif cnt % 10 == 0:
        canvas.place(x=110, y=30)
        messagebox.showinfo('【悲報】', '達也の肛門は破壊されました')
        cnt += 1
    else:
        textarea.insert(tk.END, 'ぶりッ…')
        cnt += 1


root = tk.Tk()
root.title('tkinter sample')
root.geometry("640x480")

textarea = tk.Text(root, width=200)
textarea.pack()

img = ImageTk.PhotoImage(file='unti.jpg')

canvas = tk.Canvas(root, width=400, height=400)
canvas.create_image(200, 200, image=img)

label2 = tk.Label(root, text="スイッチを押すと達也が脱糞します")
label2.place(x=270, y=350)

button = tk.Button(root, text='達也が漏らスイッチ', command=pushed)
button.place(x=290, y=380)

root.mainloop()