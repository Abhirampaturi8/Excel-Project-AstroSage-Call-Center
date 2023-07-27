import tkinter.messagebox as tmsg
import time
from tkinter import *

def getvals(event):
    value = event.widget.cget('text')
    if value=='Clr':
        sc_variable.set('')
    elif value=='=':
        try:
            result = eval(sc_variable.get())
            sc_variable.set(result)
            screen.update()
        except Exception as e:
            sc_variable.set('Error - Wait for 3 sec')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(3)
            sc_variable.set('')
            screen.update()
            status_var.set('Ready..')
            screen.update()
    else:
        sc_variable.set(f'{sc_variable.get()}{value}')

def term_of_use():
    tmsg.showinfo('Terms of Use ','IF YOU LIVE IN (OR IF YOUR PRINCIPAL PLACE OF BUSINESS IS IN) THE UNITED STATES, PLEASE READ THE BINDING ARBITRATION CLAUSE AND CLASS ACTION WAIVER IN SECTION 11. IT AFFECTS HOW DISPUTES ARE RESOLVED.')

def send_feedback():
    ans=tmsg.askquestion('Feedback Hub','Was your experience good with us ? ')
    if ans=='yes':
        tmsg.showinfo('Feedback','Please Rate us on PlayStore')
    else:
        tmsg.showinfo('Feedback','We will contact you soon to know about your bad experience')

root=Tk()
canvas_width=555
canvas_height=620
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('Scientific Calculator')
# root.call('wm', 'iconphoto', root._w, PhotoImage(file='calculator.png'))

my_menu=Menu(root)
m1=Menu(my_menu,tearoff=0,fg='red')
m1.add_command(label='Terms of Use',command=term_of_use)
m1.add_command(label='Send Feedback',command=send_feedback)
root.config(menu=my_menu)
my_menu.add_cascade(label=' About ',menu=m1)
my_menu.add_command(label='Exit',command=quit)

sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='lucida 35 bold',fg='black',bg='white',borderwidth=10)
screen.pack(pady=30)

buttons = [
    ['7', '8', '9', '*', 'sin', '('],
    ['4', '5', '6', '-', 'cos', ')'],
    ['1', '2', '3', '+', 'tan', '='],
    ['.', '0', 'sinh', 'cosh', 'tanh', 'pi']
]

for i in range(len(buttons)):
    f=Frame(root)
    f.pack()
    for j in range(len(buttons[i])):
        btn_text = buttons[i][j]
        b = Button(f, text=btn_text, font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='grey', width=3)
        b.grid(row=i, column=j)
        b.bind('<Button-1>', getvals)

# Frame for Clear button
f=Frame(root)
f.pack()
b = Button(f, text='Clr', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='grey', width=3)
b.grid(row=0, column=0)
b.bind('<Button-1>', getvals)

status_var = StringVar()
status_var.set('Ready..')
Label(root, textvariable=status_var, relief=SUNKEN, anchor='w', borderwidth=3, bg='yellow', fg='red').pack(side=BOTTOM, fill=X)

root.mainloop()

