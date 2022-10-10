import math
from tkinter import *

root = Tk()
root.title("my calculator")
#root.iconbitmap('C:/Users/codei/Documents/alvina.ico')
e = Entry(root, font="verdana 13",justify=RIGHT, width=50, borderwidth=5)
e.insert(0, "o")
e.delete(0, END)
e.grid(row=0,column=0, columnspan =8, padx=10, pady=10)
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_equals():
    second_number=e.get()
    e.delete(0, END)
    try:
        if smath=="addition":
            result =f_num + int(second_number)
            e.insert(0, result)
        if smath=="divide":
            result =f_num / int(second_number)
            e.insert(0, result)
        if smath=="multiply":
            result = f_num * int(second_number)
            e.insert(0,result)
        if smath=="substraction":
            result = f_num - int(second_number)
            e.insert(0, result)
        if smath=="pie":
            result=math.pi * int(f_num)
            e.insert(0, result)
        if smath=="siness":
            mseen=math.sin(f_num)
            result=round(mseen, 4)
            e.insert(0, str(result))
        if smath=="tanns":
            jseen=math.tan(f_num)
            result=round(jseen, 4)
            e.insert(0, str(result))
        if smath=="cosiness":
            oseen=math.cos(f_num)
            result=round(oseen, 4)
            e.insert(0, str(result))
        if smath =="percentage":
            result= "{:.3%}".format(int(f_num))
            e.insert(0, str(result))
        if smath=="log":
            result= math.log(int(f_num), 10)
            e.insert(0,str(result))
        if smath=="squaroot":
            seen=math.sqrt(f_num)
            result=round(seen, 2)
            e.insert(0, str(result))
        if smath=="cuberoot":
            seenk=(f_num**1/3)
            result=round(seenk, 4)
            e.insert(0, str(result))
        if smath=="square":
            result= f_num**2
            e.insert(0, str(result))
        if smath=="cube":
            result=f_num**3
            e.insert(0, str(result))
        #if smath == "answer":
        #    e.insert('end', result)
    except ValueError and NameError:
        mjk="syntax error"
        e.insert(0, str(mjk))




def button_add():
    first_number=e.get()
    global f_num
    global smath
    smath="addition"
    f_num = int(first_number)
    e.delete(0, END)
def button_substract():
    first_number=e.get()
    global f_num
    global smath
    smath="substraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number=e.get()
    global f_num
    global  smath
    smath="multiply"
    f_num = int(first_number)
    e.delete(0, END)
def button_divide():
    first_number=e.get()
    global f_num
    global smath
    smath="divide"
    f_num = int(first_number)
    e.delete(0, END)
def button_square():
    first_number=e.get()
    global f_num
    global smath
    smath="square"
    f_num = int(first_number)
    e.delete(0, END)
def button_cube():
    first_number=e.get()
    global f_num
    global smath
    smath="cube"
    f_num = int(first_number)
    e.delete(0, END)
def button_sine():
    first_number=e.get()
    kk="sine"
    global f_num
    global smath
    smath="siness"
    f_num = int(first_number)
    e.insert(0, str(kk))
def button_cos():
    first_number=e.get()
    global f_num
    global smath
    smath="cosiness"
    f_num = int(first_number)
def button_tan():
    first_number=e.get()
    global f_num
    global smath
    smath="tanns"
    f_num = int(first_number)
def button_delete():
    length=(len(e.get()))
    e.delete(length-1, END)
def button_squaroot():
    first_number=e.get()
    global f_num
    global smath
    smath="squaroot"
    f_num = int(first_number)
    e.insert(0, "√")
def button_cuberoot():
    first_number=e.get()
    global f_num
    global smath
    smath="cuberoot"
    f_num = int(first_number)
    e.insert(0, "∛")
def button_clears():
    e.delete(0, END)
def button_pie():
    first_number=e.get()
    mm = 'π'
    global smath
    global f_num
    smath="pie"
    f_num=(first_number)
    e.insert(0, str(mm))
def button_percentage():
    first_number = e.get()
    mkk = '%'
    global smath
    global f_num
    smath = "percentage"
    f_num = (first_number)
    e.insert(0, str(mkk))


def  button_log():
    first_number = e.get()
    mkt = 'log'
    global smath
    global f_num
    smath = "log"
    f_num = (first_number)
    e.insert(0, str(mkt))

def button_answer(jill):
    global smath
    smath="answer"
    





button_1 = Button(root, text="1", padx=30, pady=15, bg="#CE9393",fg="green", command=lambda:button_click("1"))
button_2 = Button(root, text="2", padx=30, pady=15,bg="#CE9393",fg="green", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=15,bg="#CE9393",fg="green", command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(9))

button_answer = Button(root, text="ans", padx=24, pady=15,bg="#F0C358", fg="green", command=lambda: button_equals)

button_equals = Button(root, text="=", padx=66, pady=15,bg="#F0C358",fg="green", command=button_equals)
button_0 = Button(root, text="0", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(0))
button_delete = Button(root, text="del", padx=23, pady=41,bg="#F0C358",fg="green", command=button_delete)

button_substraction = Button(root, text="-", padx=29, pady=15,bg="#CE9393",fg="green", command=button_substract)
button_addition = Button(root, text="+", padx=27, pady=15,bg="#CE9393",fg="green", command=button_add)
button_divide = Button(root, text="÷", padx=29, pady=15,bg="#CE9393",fg="green",  command=button_divide)

button_square = Button(root, text="square", padx=14, pady=15,bg="#CE9393",fg="green", command=button_square)
button_cube = Button(root, text="cube", padx=16, pady=15,bg="#CE9393",fg="green", command=button_cube)
button_sine = Button(root, text="sine", padx=21.4, pady=15,bg="#B7F8F2",fg="green", command=button_sine)

button_cos = Button(root, text="cos", padx=23, pady=15,bg="#B7F8F2",fg="green", command=button_cos)
button_tan = Button(root, text="tan", padx=20, pady=15,bg="#B7F8F2",fg="green", command=button_tan)
button_multiply = Button(root, text="x", padx=28.9, pady=15,bg="#CE9393",fg="green",  command=button_multiply)

button_squaroot = Button(root, text="√", padx=28, pady=15,bg="#B7F8F2",fg="green", command=button_squaroot)
button_cuberoot = Button(root, text="∛", padx=24.4, pady=15,bg="#B7F8F2",fg="green", command=button_cuberoot)
button_openb = Button(root, text="(", padx=29.5, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click("("))

button_closeb = Button(root, text=")", padx=30, pady=15,bg="#B7F8F2",fg="green", command=lambda: button_click(")"))
button_clears = Button(root, text="clr", padx=22.6, pady=15,bg="#B7F8F2",fg="green", command=button_clears)
button_pie = Button(root, text="π", padx=27.5, pady=15,bg="#B7F8F2",fg="green", command=button_pie)




button_log = Button(root, text="log", padx=23, pady=15, bg="#CE9393",fg="green", command=button_log)
button_percentage = Button(root, text="%", padx=27, pady=15, bg="#CE9393",fg="green", command=button_percentage)
button_dot = Button(root, text=".", padx=30, pady=15, bg="#B7F8F2",fg="green", command=lambda:button_click("."))

button_percentage.grid(row=1, column=7)
button_dot.grid(row=2, column=7)
button_log.grid(row=1, column=3)




button_1.grid(row=1, column =0)
button_2.grid(row=1, column =1)
button_3.grid(row=1, column =2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column =1)
button_6.grid(row=2, column =2)

button_7.grid(row=3, column =0)
button_8.grid(row=3, column =1)
button_9.grid(row=3, column =2)

button_equals.grid(row=4, column =0, columnspan=2)
button_0.grid(row=4, column =2)

button_answer.grid(row=4, column=7)
button_delete.grid(row=3, column =7)
button_pie.grid(row=3,column=4)
button_substraction.grid(row=2, column =3)
button_addition.grid(row=4, column =3,)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=1, column =4)

button_square.grid(row=1, column =5)
button_cube.grid(row=1, column =6)
button_sine.grid(row=2, column =4)

button_cos.grid(row=2, column =5)
button_tan.grid(row=2, column =6)
button_cuberoot.grid(row=3, column =4)

button_squaroot.grid(row=3, column =5)
button_cuberoot.grid(row=3, column =6)
button_openb.grid(row=4, column =4)

button_closeb.grid(row=4, column =5)
button_clears.grid(row=4, column =6)
root.configure(bg="grey")
root.mainloop()