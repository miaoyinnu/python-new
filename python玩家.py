import random
from tkinter import *
num = random.randint(1,54)
num = str("")

#关闭所有窗口
def close_all_window():
    window.destroy()

#关闭窗口提示
def close_window():
    window.destroy()
def choujiang():
    num = random.randint(1,54)
    if num>=1 and num<=54:
        label = Label(window, text= str(num), font=("微软雅黑", 18))
        label.place(x=120, y=50)
    else:
        label = Label(window, text="", font=("微软雅黑", 18))
        label.place(x=120, y=50)



#“好的”窗口


window = Tk()
window.title("随机抽号") #窗口标题
window.geometry("360x640+550+50") #窗口大小
window.protocol("WM_DELETE_WINDOW", close_window) #窗口关闭

label = Label(window, text="", font=("微软雅黑", 24))
label.place(x=70, y=100)
btn1 = Button(window, text="抽奖", width=15, height=2,command=choujiang)
btn1.place(x=110, y=200)
#显示窗口，消息循坏
window.mainloop()

print(num)