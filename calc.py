import tkinter as tk
from tkinter import *
from tkinter import ttk

def click_action():
    label2.config(text=None)
    num1=in1.get()
    in1.delete(0)
    num2=in2.get()
    in2.delete(0)
    first_number_int=int(num1)
    second_number_int=int(num2)
    add=first_number_int+second_number_int
    label2.config(text=add)
    

root = Tk()
root.title('Calculator')
root.geometry("600x400")

label = Label(root, text="CALCULATOR!", font=30)
label.pack()

label2 = Label(root, text=None, font=30)
label2.pack()

click_button = Button(root, text="Add", width=8)
click_button.pack()

in1 = tk.Entry(root)
in2 = tk.Entry(root)
in1.pack()
in2.pack()


click_button.config(command=click_action)

root.mainloop()
#frm = ttk.Frame(root,)
#frm.grid()
#ttk.Label(frm, text="CALCULATOR!").grid(column=0, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#root.mainloop()


#print ("Calculator!")
#first_number=input("Write first number: ")
#first_number_int=int(first_number)
#second_number=input("Write second number: ")
#second_number_int=int(second_number)
#add=first_number_int+second_number_int
#sub=first_number_int-second_number_int
#mul=first_number_int*second_number_int
#div=first_number_int/second_number_int
#print (first_number+"+"+second_number+"="+str(add))
#print (first_number+"-"+second_number+"="+str(sub))
#print (first_number+"*"+second_number+"="+str(mul))
#print (first_number+"/"+second_number+"="+str(div))