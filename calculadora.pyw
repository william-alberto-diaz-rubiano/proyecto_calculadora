from tkinter import *
import parser

root=Tk()
root.config(bg="#A4A4A4")
root.title("calculator")
calculator_frame=Frame(root,padx=30,pady=30,background="#A4A4A4")
calculator_frame.pack()

operation="" 
result=0

"""fila 1 pantalla"""
number_secreen=StringVar()

screen=Entry(calculator_frame,font=("Lucida Grande",10,"normal"), textvariable=number_secreen,width=30)
screen.grid(row=0,column=0,padx=5,pady=10,columnspan=7,sticky=W+E)
screen.config(bg="white",fg="black",justify="right")

""" teclado"""
i=0
def get_number(n):
    global i
    screen.insert(i,n)
    i=i+1

"""traer un operador"""

def get_operation(operator):
    global i
    operator_length=len(operator)
    screen.insert(i,operator)
    i=i+operator_length
    print(i)

"""limpiar pantalla"""

def clear_screen():
    screen.delete(0,END)

"""borrar un solo elemento"""
def undo():
    screen_state=screen.get()
    print(screen_state)
    if len(screen_state)>0:
        screen_new_state=screen_state[:-1]
        clear_screen()
        screen.insert(0,screen_new_state)
    else:
        clear_screen()

"""funcion para el igual"""
def equal():
    screen_state=screen.get()
    try:
        math_expression=parser.expr(screen_state).compile()
        result=eval(math_expression)
        clear_screen()
        screen.insert(0,result)
    except:
        clear_screen()
        screen.insert(0,"Error")

        


"""fila 2"""
Button_7=Button(calculator_frame,text="7",width=7,command=lambda:get_number("7"),bg="#ffffff")
Button_7.grid(row=2,column=1)
Button_8=Button(calculator_frame,text="8",width=7,command=lambda:get_number("8"),bg="#ffffff")
Button_8.grid(row=2,column=2)
Button_9=Button(calculator_frame,text="9",width=7,command=lambda:get_number("9"),bg="#ffffff")
Button_9.grid(row=2,column=3)
Button_div=Button(calculator_frame,text="/",width=7,command=lambda:get_operation("/"),bg="#ffffff")
Button_div.grid(row=2,column=4)
Button_cuad=Button(calculator_frame,text="^2",width=7,command=lambda:get_operation("**2"),bg="#ffffff")
Button_cuad.grid(row=2,column=5)
Button_AC=Button(calculator_frame,text="AC",width=7,command=lambda:clear_screen(),bg="#ffffff")
Button_AC.grid(row=2,column=6)



"""fila 3"""
Button_4=Button(calculator_frame,text="4",width=7,command=lambda:get_number("4"),bg="#ffffff")
Button_4.grid(row=3,column=1)
Button_5=Button(calculator_frame,text="5",width=7,command=lambda:get_number("5"),bg="#ffffff")
Button_5.grid(row=3,column=2)
Button_6=Button(calculator_frame,text="6",width=7,command=lambda:get_number("6"),bg="#ffffff")
Button_6.grid(row=3,column=3)
Button_mult=Button(calculator_frame,text="x",width=7,command=lambda:get_operation("*"),bg="#ffffff")
Button_mult.grid(row=3,column=4)
Button_mod=Button(calculator_frame,text="%",width=7,command=lambda:get_operation("%"),bg="#ffffff")
Button_mod.grid(row=3,column=5)
Button_del=Button(calculator_frame,text="🠔",width=7,command=lambda:undo() ,bg="#ffffff")
Button_del.grid(row=3,column=6)



"""fila 4"""
Button_1=Button(calculator_frame,text="1",width=7,command=lambda:get_number("1"),bg="#ffffff")
Button_1.grid(row=4,column=1)
Button_2=Button(calculator_frame,text="2",width=7,command=lambda:get_number("2"),bg="#ffffff")
Button_2.grid(row=4,column=2)
Button_3=Button(calculator_frame,text="3",width=7,command=lambda:get_number("3"),bg="#ffffff")
Button_3.grid(row=4,column=3)
Button_add=Button(calculator_frame,text="+",width=7,command=lambda:get_operation("+"),bg="#ffffff")
Button_add.grid(row=4,column=4)
Button_parent_left=Button(calculator_frame,text="(",width=7,command=lambda:get_operation("("),bg="#ffffff")
Button_parent_left.grid(row=4,column=5)
Button_exp=Button(calculator_frame,text="exp",width=7,command=lambda:get_operation("**"),bg="#ffffff")
Button_exp.grid(row=4,column=6)

"""fila 5"""

Button_0=Button(calculator_frame,text="0",width=7,command=lambda:get_number("0"),bg="#ffffff")
Button_0.grid(row=5,column=1)
Button_point=Button(calculator_frame,text=".",width=7,command=lambda:get_operation("."),bg="#ffffff")
Button_point.grid(row=5,column=2)
Button_subtr=Button(calculator_frame,text="-",width=7,command=lambda:get_operation("-"),bg="#ffffff")
Button_subtr.grid(row=5,column=3)
Button_parent_right=Button(calculator_frame,text=")",width=7,command=lambda:get_operation(")"),bg="#ffffff")
Button_parent_right.grid(row=5,column=4)
Button_equal=Button(calculator_frame,text="=",width=7,command=lambda:equal(),bg="#ffffff")
Button_equal.grid(row=5,column=5,columnspan=2, sticky=W+E)




root.mainloop()