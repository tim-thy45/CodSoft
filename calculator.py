import tkinter as tk
calculation=""
def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")
def evaluate_calculation():
    global calculation
    
    try:
        result=str(eval(calculation))
        calculation=""
        text_result.delete(1.0,"end")
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
def add_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)


root=tk.Tk()
root.title("Calc+")
root.config(bg='grey16')
#root.geometry("300x275")
text_result=tk.Text(root,height=2,width=16,font=("American Typewriter",24),fg="snow",bg="grey36")
text_result.grid(columnspan=5)


btn_1=tk.Button(root,text="1",command=lambda: add_calculation(1),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_1.grid(row=2,column=1,pady=10)
btn_2=tk.Button(root,text="2",command=lambda: add_calculation(2),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_2.grid(row=2,column=2,pady=10)
btn_3=tk.Button(root,text="3",command=lambda: add_calculation(3),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_3.grid(row=2,column=3,pady=10)
btn_4=tk.Button(root,text="4",command=lambda: add_calculation(4),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_4.grid(row=3,column=1,pady=10)
btn_5=tk.Button(root,text="5",command=lambda: add_calculation(5),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_5.grid(row=3,column=2,pady=10)
btn_6=tk.Button(root,text="6",command=lambda: add_calculation(6),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_6.grid(row=3,column=3,pady=10)
btn_7=tk.Button(root,text="7",command=lambda: add_calculation(7),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_7.grid(row=4,column=1,pady=10)
btn_8=tk.Button(root,text="8",command=lambda: add_calculation(8),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_8.grid(row=4,column=2,pady=10)
btn_9=tk.Button(root,text="9",command=lambda: add_calculation(9),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_9.grid(row=4,column=3,pady=10)
btn_0=tk.Button(root,text="0",command=lambda:add_calculation(0),width=3,font=("American Typewriter",16),bg="grey45",fg="snow")
btn_0.grid(row=5,column=2,pady=10)
btn_plus=tk.Button(root,text="+",command=lambda:add_calculation("+"),width=3,font=("American Typewriter",16),bg="chocolate1",fg="snow")
btn_plus.grid(row=2,column=4,pady=10)
btn_minus=tk.Button(root,text="-",command=lambda:add_calculation("-"),width=3,font=("American Typewriter",16),bg="chocolate1",fg="snow")
btn_minus.grid(row=3,column=4,pady=10)
btn_prod=tk.Button(root,text="*",command=lambda:add_calculation("*"),width=3,font=("American Typewriter",16),bg="chocolate1",fg="snow")
btn_prod.grid(row=4,column=4,pady=10)
btn_div=tk.Button(root,text="/",command=lambda:add_calculation("/"),width=3,font=("American Typewriter",16),bg="chocolate1",fg="snow")
btn_div.grid(row=5,column=4,pady=10)
btn_op=tk.Button(root,text="(",command=lambda:add_calculation("("),width=3,font=("American Typewriter",16),bg="chocolate1",fg="snow")
btn_op.grid(row=5,column=1,pady=10)
btn_cl=tk.Button(root,text=")",command=lambda:add_calculation(")"),width=3,font=("American Typewriter",16),bg="chocolate1",fg="snow")
btn_cl.grid(row=5,column=3,pady=10)
btn_eq=tk.Button(root,text="=",command=evaluate_calculation,width=9,font=("American Typewriter",16),bg="goldenrod3",fg="snow")
btn_eq.grid(row=6,column=3,columnspan=2,pady=10)
btn_clr=tk.Button(root,text="CLR",command=clear_field,width=9,font=("American Typewriter",16),bg="DarkOliveGreen3",fg="snow")
btn_clr.grid(row=6,column=1,columnspan=2,pady=10)
root.mainloop()
