# -*- coding: utf-8 -*-
import tkinter
import pyttsx3
import tkinter.messagebox
import random
import threading
import itertools
import time
import pygame
print("语音抽签软件 4.51测试版本 2019 3")
engine = pyttsx3.init()
engine.say("")

engine.runAndWait()
condition = "正在运行中"

root = tkinter.Tk()
pygame.mixer.init()

track = pygame.mixer.music.load("D:\py2\pybns\lldq.mp3")

pygame.mixer.music.play(2, 0.5)
pygame.mixer.music.set_volume(0.3)


root.title('语音抽签') # 窗口标题



root.geometry('300x200+300+200') # 窗口初始大小和位置



root.resizable(False, False) # 不允许改变窗口大小




def closeWindow():

    root.flag = False




    root.destroy()

    engine.runAndWait()


root.protocol('WM_DELETE_WINDOW', closeWindow)

# 模拟学生名单，可以加上数据库访问接口，从数据库中读取学生名单

students = ["1曹琳琳","2陈永婷","3崔紫芸","4邓心雨","5何伊尹","6黄晓琪","7柯春蕊","8李海丹","9李慧","10李燕婷","11林艳婷","12刘诗怡","13刘芷璇","14吕欣桦","15邵若曦","16苏梓欣","17谢丽敏","18许善薇","19翁凤姗","20张祺","21周乐瑶","22陈天健","23陈振华","24崔梓淇","25戴光添","26冯齐润","27冯智晖","28黄俊曦","29李明键","30李琪东","31李政林","32梁榜文","33梁嘉豪","34梁英東","35梁迎涛","36梁振源","37梁智勇","38梁梓霖","39林俊旭","40刘炽扬","41刘瀚天","42刘平台","43麦建辉","44潘粤豪","45庞志柠","46彭国彬","47彭林茂","48王国霖","49吴锦超","50徐中霖","51许志峰","52杨智贤","53周小宣","54杨晰"]

# 变量，用来控制是否滚动显示学生名单

root.flag = False


def switch():
    root.flag = True

    while root.flag:
        # 随机打乱学生名单

        t = students[:]

        random.shuffle(t)

        t = itertools.cycle(t)

        # 滚动显示

        lbFirst['text'] = lbSecond['text']

        lbSecond['text'] = lbThird['text']

        lbThird['text'] = next(t)

        # 数字可以修改，控制滚动速度

        time.sleep(0.1)
def btnStartClick():    # 每次单击“开始”按钮启动新线程

        pygame.mixer.init()

        track = pygame.mixer.music.load("D:\py2\pybns\mp3.mp3")

        pygame.mixer.music.play(2,1)
        pygame.mixer.music.set_volume(0.06)



        t = threading.Thread(target=switch)

        t.start()



btnStart = tkinter.Button(root, text='抽签', command=btnStartClick)

btnStart.place(x=30, y=10, width=80, height=20)


def btnStopClick():
    # 单击“停”按钮结束滚动显示
    pygame.mixer.music.pause()
    engine.say("请" + lbSecond['text'] + "同学回答问题")
    engine.runAndWait()
    root.flag = False

    time.sleep(0.1)
    tkinter.messagebox.showinfo('', '请 ' + lbSecond['text'] + " 同学回答问题")





btnStop = tkinter.Button(root, text='停止', command=btnStopClick)

btnStop.place(x=150, y=10, width=80, height=20)

# 用来滚动显示学生名单的3个Label组件

# 可以根据需要进行添加，但要修改上面的线程函数代码

lbFirst = tkinter.Label(root, text='')

lbFirst.place(x=80, y=60, width=100, height=20)

# 红色Label组件，表示中奖名单

lbSecond = tkinter.Label(root, text='')

lbSecond['fg'] = 'red'

lbSecond.place(x=80, y=90, width=100, height=20)

lbThird = tkinter.Label(root, text='')

lbThird.place(x=80, y=120, width=100, height=20)

# 启动tkinter主程序

root.mainloop()