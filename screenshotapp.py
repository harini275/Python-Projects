import time
import pyautogui
import tkinter as tk

def screenshot():
    name=int(round(time.time()*1000))
    name=r'D:\python project\screenshot data\{}.png'.format(name)
    img=pyautogui.screenshot('test.png')
    img.show()

root=tk.Tk()
frame=tk.Frame(root)

frame.pack()

button=tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)

close=tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()
