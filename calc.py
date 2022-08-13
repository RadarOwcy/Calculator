import tkinter as tk
from tkinter import *
from tkinter import ttk

def click_action():
    label2.config(text=None)
    num1=in1.get()
    #in1.delete(0)
    num2=in2.get()
    #in2.delete(0)
    first_number_int=int(num1)
    second_number_int=int(num2)
    add=first_number_int+second_number_int
    label2.config(text=add)

def next_num():
    label2.config(text="number" )

    
val_key_padx=3
val_key_pady=3

root = Tk()
root.title('Calculator')
root.geometry("200x180")

frame_row_zero = tk.Frame()
label2 = Label(frame_row_zero, text="Click something", font=30)
label2.pack()
frame_row_zero.pack(side=TOP,padx=5,pady=5)

#first row

frame_row_first = tk.Frame()

clean_button = Button(frame_row_first, text="C", width=5)
clean_button.pack(side=LEFT, padx=val_key_padx)

number0_button = Button(frame_row_first, text="0", width=5)
number0_button.pack(side=LEFT, padx=val_key_padx)

eqa_button = Button(frame_row_first, text="=", width=5)
eqa_button.pack(side=LEFT, padx=val_key_padx)

plus_button = Button(frame_row_first, text="+", width=5)
plus_button.pack(side=LEFT, padx=val_key_padx)



#second row

frame_row_second = tk.Frame()

number1_button = Button(frame_row_second, text="1", width=5)
number1_button.pack(side=LEFT, padx=val_key_padx)

number2_button = Button(frame_row_second, text="2", width=5)
number2_button.pack(side=LEFT, padx=val_key_padx)

number3_button = Button(frame_row_second, text="3", width=5)
number3_button.pack(side=LEFT, padx=val_key_padx)

minus_button = Button(frame_row_second, text="-", width=5)
minus_button.pack(side=LEFT, padx=val_key_padx)



#third row

frame_row_third = tk.Frame()

number4_button = Button(frame_row_third, text="4", width=5)
number4_button.pack(side=LEFT, padx=val_key_padx)

number5_button = Button(frame_row_third, text="5", width=5)
number5_button.pack(side=LEFT, padx=val_key_padx)

number6_button = Button(frame_row_third, text="6", width=5)
number6_button.pack(side=LEFT, padx=val_key_padx)

div_button = Button(frame_row_third, text="/", width=5)
div_button.pack(side=LEFT, padx=val_key_padx)



#fourth row

frame_row_fourth = tk.Frame()

number7_button = Button(frame_row_fourth, text="7", width=5)
number7_button.pack(side=LEFT, padx=val_key_padx)

number8_button = Button(frame_row_fourth, text="8", width=5)
number8_button.pack(side=LEFT, padx=val_key_padx)

number9_button = Button(frame_row_fourth, text="9", width=5)
number9_button.pack(side=LEFT, padx=val_key_padx)

multi_button = Button(frame_row_fourth, text="*", width=5)
multi_button.pack(side=LEFT, padx=val_key_padx)



#label = Label(root, text="CALCULATOR!", font=30)
#label.pack()

frame_row_fourth.pack(side=BOTTOM, pady=val_key_pady)
frame_row_third.pack(side=BOTTOM, pady=val_key_pady)
frame_row_second.pack(side=BOTTOM, pady=val_key_pady)
frame_row_first.pack(side=BOTTOM, pady=val_key_pady)











#in1 = tk.Entry(root)
#in2 = tk.Entry(root)
#in1.pack()
#in2.pack()


#click_button.config(command=click_action)

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