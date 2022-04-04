from tkinter import *

root = Tk()

#VARIABLES
width =80
height= 80


#FUNCTION
def value(number):
	old_value= field.get()
	field.delete(0,END)	
	field.insert(0,old_value + str(number))
	
def clear():
	field.delete(0,END)
	
def add():
	global first_value
	global function
	function='add'
	first_value= int(field.get())
	field.delete(0,END)
	
def subtract():
	global first_value
	global function
	function='minus'
	first_value = int(field.get())
	field.delete(0,END)
	
def multiply():
	global first_value
	global function
	function='mult'
	first_value = int(field.get())
	field.delete(0,END)
	
def div():
	global first_value
	global function
	function='div'
	first_value = int(field.get())
	field.delete(0,END)
	
def equal_to():
	second_value=int(field.get())
	field.delete(0,END)
	if function == 'add':
		field.insert(0, first_value + second_value)
	elif function == 'minus':
		field.insert(0, first_value - second_value)
	elif function == 'mult':
		field.insert(0, first_value * second_value)
	elif function == 'div':
		field.insert(0, first_value / second_value)
#LABELS
field=Entry(root, width=40,font='Ariel 24')

#BUTTONS
num0 = Button(root, padx=width,pady=160, text='0',command=lambda: value(0))
num1 = Button(root, padx=width,pady=height, text='1',command=lambda: value(1))
num2 = Button(root, padx=width,pady=height, text='2',command=lambda: value(2))
num3 = Button(root, padx=width,pady=height, text='3',command=lambda: value(3))
num4 = Button(root, padx=width,pady=height, text='4',command=lambda: value(4))
num5 = Button(root, padx=width,pady=height, text='5',command=lambda: value(6))
num6 = Button(root, padx=width,pady=height, text='6',command=lambda: value(6))
num7 = Button(root, padx=width,pady=height, text='7',command=lambda: value(7))
num8 = Button(root, padx=width,pady=height, text='8',command=lambda: value(8))
num9 = Button(root, padx=width,pady=height, text='9',command=lambda: value(9))
add = Button(root, padx=width,pady=height, text='+',command=add)
subt = Button(root, padx=width,pady=height, text='_',command=subtract)
div = Button(root, padx=width,pady=height, text='/',command=div)
mult = Button(root, padx=width,pady=height, text='*',command=multiply)
equal = Button(root, padx=width,pady=160, text='=',command=equal_to)
clear = Button(root, padx=160,pady=height, text='clr',command=clear)
xterm= Button(root, padx=width,pady=height, text='exit',command=root.quit)
#num0 = Button(root, padx=10,pady=10, text='0',command=lambda: value())





#OUTPUT
field.grid(row=0,column=0, columnspan=160)

num1.grid(row=  3 , column=0  )
num2.grid(row= 3 , column= 1 )
num3.grid(row= 3 , column=  2)

num4.grid(row=2  , column=  0)
num5.grid(row=2  , column=1  )
num6.grid(row= 2 , column=  2)

num7.grid(row= 1 , column= 0 )
num8.grid(row=1  , column= 1 )
num9.grid(row=  1, column=  2)

add.grid(row=1  , column=3)
subt.grid(row=2  , column=  3)
mult.grid(row=4  , column=1 )
div.grid(row= 4 , column=  2)

num0.grid(row=  4, column=  0,rowspan=2)
equal.grid(row=  3, column=  3, rowspan=2)
clear.grid(row=5  , column=  1, columnspan=2)
xterm.grid(row=5  , column= 3)









root.mainloop()
