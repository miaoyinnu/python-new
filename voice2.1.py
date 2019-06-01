# -*- coding: utf-8 -*-
import pygame,re,time,itertools,random,threading,tkinter.messagebox,pyttsx3,tkinter
from tkinter import * # 引入字体模块
import tkinter.font as tkFont # Font来创建字体



rate,rate1 = 115,115
root = tkinter.Tk() #建立一个root object
root.title('                               China huiwei fighting ') # 窗口标题
root.geometry('450x400+500+100') # 窗口初始大小和位置
root.resizable(False, False) # 不允许改变窗口大小


var = tkinter.StringVar()

def closeWindow():
    
    root.flag = False
    root.destroy()
    pygame.mixer.init()
    pygame.mixer.music.pause()
root.protocol('WM_DELETE_WINDOW', closeWindow)
root.flag = False

students1 = ["1曹琳琳","2陈永婷","3崔紫芸","4邓心雨","5何伊尹","6黄晓琪","7柯春蕊","8李海丹","9李慧","10李燕婷","11林艳婷","12刘诗怡","13刘芷璇","14吕欣桦","15邵若曦","16苏梓欣","17谢丽敏","18许善薇","19翁凤姗","20张祺","21周乐瑶","22陈天健","23陈振华","24崔梓淇","25戴光添","26冯齐润","27冯智晖","28黄俊曦","29李明键","30李琪东","31李政林","32梁榜文","33梁嘉豪","34梁英東","35梁迎涛","36梁振源","37梁智勇","38梁梓霖","39林俊旭","40刘炽扬","41刘瀚天","42刘平台","43麦建辉","44潘粤豪","45庞志柠","46彭国彬",'48王国霖',"47彭林茂","49吴锦超","50徐中霖","51许志峰","52杨智贤","53周小宣","54杨晰"]
students = ["曹琳琳","陈永婷","崔紫芸","邓心雨","何伊尹","黄晓琪","柯春蕊","李海丹","李慧","李燕婷","林艳婷","刘诗怡","刘芷璇","吕欣桦","邵若曦","苏梓欣","谢丽敏","许善薇","张祺","周乐瑶","陈天健","陈振华","崔梓淇","戴光添","冯齐润","冯智晖","黄俊曦","李明键","李琪东","李政林","梁榜文","梁嘉豪","梁英東","梁迎涛","梁振源","梁智勇","梁梓霖","林俊旭","刘炽扬","刘瀚天","刘平台","麦建辉","潘粤豪","庞志柠","彭国彬",'王国霖',"彭林茂","吴锦超","徐中霖","许志峰","杨智贤","周小宣","杨晰"]




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

        time.sleep(0.005)
def btnStartClick():    # 每次单击“开始”按钮启动新线程
        btnStop.place(x=350, y=50, width=80, height=60)
        
        # btn_choice_more.place(x=310, y=200, width=150, height=60)
        global on_hit
        btnStart.place_forget()
        
        on_hit = True
        if on_hit == True:
            var.set('中国华为加油')
        else:
            on_hit = False

        pygame.mixer.init()
        track = pygame.mixer.music.load("D://pyfile/Working.mp3")
        pygame.mixer.music.play(1,0.1)
        pygame.mixer.music.set_volume(5.0)



        t = threading.Thread(target=switch)

        t.start()

lbFirst1 = tkinter.Label(root, text='                      我❤茂名一中                 ',font=('微软雅黑', 20),bg='green')
on_hit = False
Label = tkinter.Label(root,textvariable=var,bg='red',font=('微软雅黑',20))
var.set('我爱茂名一中')
Label.pack()

btnStart = tkinter.Button(root, text='Start', command=btnStartClick,font='Arial')

btnStart.place(x=15, y=50, width=80, height=60)
def choice_twice():
    for x in [0,1]:
        a = random.choice(students)
        engine = pyttsx3.init()
    
        rate1 = engine.getProperty('rate')
        rate1=190
        engine.setProperty('rate', rate1)
        engine.say(" %s " %a)


        engine.runAndWait()
def choice_three():

    for x in [0,1,3]:
        a = random.choice(students)
        engine = pyttsx3.init()
    
        rate1 = engine.getProperty('rate')
        rate1=190
        engine.setProperty('rate', rate1)
        engine.say(" %s " %a)


        engine.runAndWait()

btn_choice_more = tkinter.Button(root,text='批量抽三个',command=choice_three)
btn_choice_more.place(x=310, y=200, width=150, height=60)
btn_speed = tkinter.Button(root,text='批量抽两个',command=choice_twice)
btn_speed.place(x=15, y=200, width=80, height=60)
def btnStopClick():
    root.flag = False
    # 单击“停”按钮结束滚动显示
    global on_hit
    on_hit = False
    if on_hit == False:
        var.set('我爱茂名一中')
    else:
        on_hit = True
    
    btnStart.place(x=15, y=50, width=80, height=60)
    btnStop.place_forget()
    btn_choice_more.place_forget()
    # btn_speed.place_forget()
    pygame.mixer.music.pause()


    engine = pyttsx3.init()
    
    rate1 = engine.getProperty('rate')
    rate1=190
    engine.setProperty('rate', rate1)
    engine.say(" %s " %lbSecond['text'])

    engine.runAndWait()
    

    

    # tkinter.messagebox.showinfo(lbSecond['text'])






btnStop = tkinter.Button(root, text='Stop', command=btnStopClick,font='Arial')

btnStop.place(x=350, y=50, width=80, height=60)
btnStop.place_forget()

# 用来滚动显示学生名单的3个Label组件

# 可以根据需要进行添加，但要修改上面的线程函数代码

lbFirst = tkinter.Label(root, text='',font=('微软雅黑', 45))
lbFirst.place(x=120, y=276, width=200, height=80)

# 红色Label组件，表示中奖名单

lbSecond = tkinter.Label(root, text='',font=('微软雅黑', 50))

lbSecond['fg'] = 'red'

lbSecond.place(x=120, y=160, width=200, height=100)

lbThird = tkinter.Label(root, text='',font=('微软雅黑', 50))

lbThird.place(x=120, y=70, width=200, height=100)

root.mainloop() # 启动tkinter主程序
