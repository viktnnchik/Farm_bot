#Библиотеки
from tkinter import *
import webbrowser
import pyautogui
import time
import tkinter as tk


#Переменные для checkbox

auto = False
plant = True

#Длина поля
xLenght = 7
yLenght = 6

#Функции

def change_color(step=0):
    g = abs((step*8) % 512 - 255)
    b = 255 - g
    lbl.configure(fg=f"#00{g:0>2x}{b:0>2x}")
    lblZ.configure(fg=f"#00{g:0>2x}{b:0>2x}")
    window.after(5000 * 8 // 256, lambda: change_color(step+1))

def change():
    if var.get() == 0:
        lbl = Label(window, text="Данная программа была сделанна на голом энтузиазме.").place(x=0, y=0, bordermode=OUTSIDE)
        lbl1 = Label(window, text="Программа абсолютно бесплатна,в случае если вы ").place(x=0, y=20,bordermode=OUTSIDE)
        lbl2 = Label(window, text="хотите поддержать проект напишите разработчику").place(x=0, y=40, bordermode=OUTSIDE)
        lbl4 = Label(window, text="!!!Обязательно прочитайте файл :Прочитай меня!!!").place(x=0, y=60,bordermode=OUTSIDE)

        lbl3 = Label(window, text="Контакты:").place(x=390, y=0, bordermode=OUTSIDE)

        btn1 = Button(window, text="начать", command=planting).place(x=345, y=320, bordermode=OUTSIDE)
        btn2 = Button(window, text="ВЫХОД", command=window.destroy).place(x=400, y=320, bordermode=OUTSIDE)

        lbl3 = Label(window, text="Введите частоту - 0.15 оптимальная").place(x=10, y=110, bordermode=OUTSIDE)
        number = Entry(window, textvariable=message, width=20).place(x=10, y=130, )
        btn = Button(text='ОК', command=get_num, font='5', padx='25', pady='5').place(x=10, y=150, bordermode=OUTSIDE)

        lbl3 = Label(window, text="Расстояние вдаль (недоступно)").place(x=10, y=180, bordermode=OUTSIDE)
        number = Entry(window, textvariable=message, width=20).place(x=10, y=200, )
        btn = Button(text='ОК', font='5', padx='25', pady='5').place(x=10, y=220, bordermode=OUTSIDE)

        lbl3 = Label(window, text="Расстояние в ширину (недоступно)").place(x=10, y=250, bordermode=OUTSIDE)
        number = Entry(window, textvariable=message, width=20).place(x=10, y=270, )
        btn = Button(text='ОК', font='5', padx='25', pady='5').place(x=10, y=290, bordermode=OUTSIDE)


        lblFood = Label(window, text="Нужно ли есть?").place(x=350, y=200, bordermode=OUTSIDE)
        TakeFood = Radiobutton(text="Принимать", variable=food, value=0).place(x=350, y=220, bordermode=OUTSIDE)
        NoTakeFood = Radiobutton(text="Не принимать", variable=food, value=1).place(x=350, y=240, bordermode=OUTSIDE)

    else:
        lbl = Label(window, text="This program was made on pure enthusiasm.").place(x=0, y=0, bordermode=OUTSIDE)
        lbl1 = Label(window, text="The program is absolutely free, if you ").place(x=0, y=20,bordermode=OUTSIDE)
        lbl2 = Label(window, text="if you want to support the project write to the developer").place(x=0, y=40, bordermode=OUTSIDE)
        lbl4 = Label(window, text="!!!Be sure to read the file :Read me!!!").place(x=0, y=60, bordermode=OUTSIDE)

        lbl3 = Label(window, text="Contacts:").place(x=390, y=0, bordermode=OUTSIDE)

        btn1 = Button(window, text="start", command=planting).place(x=360, y=320, bordermode=OUTSIDE)
        btn2 = Button(window, text="exit", command=window.destroy).place(x=400, y=320, bordermode=OUTSIDE)

        lbl3 = Label(window, text="Enter frequency - 0.15 optimal").place(x=10, y=110, bordermode=OUTSIDE)
        number = Entry(window, textvariable=message, width=20).place(x=10, y=130, )
        btn = Button(text='ОК', command=get_num, font='5', padx='25', pady='5').place(x=10, y=150, bordermode=OUTSIDE)

        lbl3 = Label(window, text="Distance into the distance (not available)").place(x=10, y=180, bordermode=OUTSIDE)
        number = Entry(window, textvariable=message, width=20).place(x=10, y=200, )
        btn = Button(text='ОК', font='5', padx='25', pady='5').place(x=10, y=220, bordermode=OUTSIDE)

        lbl3 = Label(window, text="Width Distance (not available)").place(x=10, y=250, bordermode=OUTSIDE)
        number = Entry(window, textvariable=message, width=20).place(x=10, y=270, )
        btn = Button(text='ОК', font='5', padx='25', pady='5').place(x=10, y=290, bordermode=OUTSIDE)

        lblFood = Label(window, text="Do you need to eat?").place(x=350, y=200, bordermode=OUTSIDE)
        TakeFood = Radiobutton(text="Take", variable=food, value=0).place(x=350, y=220, bordermode=OUTSIDE)
        NoTakeFood = Radiobutton(text="No take", variable=food, value=1).place(x=350, y=240, bordermode=OUTSIDE)

def get_num():
    str_speed = message.get()
    b = 0
    speed = float(str_speed) + b
    print("The value of c = ", speed)
    print(str_speed)

def vk():
   webbrowser.open('https://vk.com/gn1dor', new=2)

def tg():
   webbrowser.open('https://t.me/gn1dor', new=2)

def ds():
   webbrowser.open('https://discord.gg/ZPXbfUYqHs', new=2)

def planting():
    str_speed = message.get()
    b = 0
    speed = float(str_speed) + b
    back = False
    for i in range(xLenght):
        if back is False:
            time.sleep(2)
            for i in range(yLenght):
                pyautogui.mouseUp()
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.PAUSE = speed
                pyautogui.keyDown('w')
                pyautogui.keyUp('w')
            pyautogui.PAUSE = speed
            pyautogui.keyDown('d')
            pyautogui.keyUp('d')
            pyautogui.keyDown('s')
            pyautogui.keyUp('s')
            back = not back
        else:
            for i in range(yLenght):
                pyautogui.mouseUp()
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.PAUSE = speed
                pyautogui.keyDown('s')
                pyautogui.keyUp('s')
            pyautogui.PAUSE = speed
            pyautogui.keyDown('d')
            pyautogui.keyUp('d')
            pyautogui.keyDown('w')
            pyautogui.keyUp('w')
            back = not back

#Интерфейс


window = Tk()
window.title("Bots by gn1dor - autofarm")
window.geometry('450x350')
window.resizable(width=False,height=False)
window['background']='#2EA966'

btn3 = Button(window, text="vk", command=vk).place(x=400, y=20, bordermode=OUTSIDE)
btn4 = Button(window, text="tg", command=tg).place(x=380, y=20, bordermode=OUTSIDE)
btn5 = Button(window, text="ds", command=ds).place(x=420, y=20, bordermode=OUTSIDE)

message = StringVar()
var = IntVar()
var.set(0)

food = IntVar()
food.set(0)

red = Radiobutton(text="RU", variable=var, value=0).place(x=390, y=130, bordermode=OUTSIDE)
green = Radiobutton(text="EN",variable=var, value=1).place(x=390, y=150, bordermode=OUTSIDE)
button = Button(text="change",command=change).place(x=390, y=170, bordermode=OUTSIDE)


buttonFood = Button(text="change").place(x=350, y=260, bordermode=OUTSIDE)

logo = PhotoImage(file="./assets/logo.png")
window.iconbitmap(r'./assets/logo.ico')

label = tk.Label(image=logo, compound="top")
label.pack(anchor=CENTER)

lbl = tk.Label(window, text="BOTS BY GN1DOR", font="-size 20")
lblZ = tk.Label(window, text="AUTOFARM", font="-size 20")

lbl.pack(anchor=CENTER)
lblZ.pack(anchor=CENTER)
window.after(1, change_color)

window.mainloop()
