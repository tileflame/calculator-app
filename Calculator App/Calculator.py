
import tkinter as tk
import math
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("800x600")
display = tk.Entry(
    window,
    font=("GentySans",24),
    width=30
)
def calculate():
    expression = display.get()

    try:
        answer = eval(expression)

        display.delete(0, tk.END)

        display.insert(0, answer)

    except:
        display.delete(0, tk.END)

        display.insert(0, "Error")
button7 = tk.Button(
    window,
    text="7",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "7")
)

button8 = tk.Button(
    window,
    text="8",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "8")
)
button9 = tk.Button(
    window,
    text="9",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "9")
)
button6 = tk.Button(
    window,
    text="6",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "6")
)
button5 = tk.Button(
    window,
    text="5",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "5")
)
button4 = tk.Button(
    window,
    text="4",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "4")      
)
button3 = tk.Button(
    window,
    text="3",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "3")
)
button2 = tk.Button(
    window,
    text="2",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "2")
)
button1 = tk.Button(
    window,
    text="1",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "1")
)
button0 = tk.Button(
    window,
    text="0",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "0")
)
button_plus = tk.Button(
    window,
    text="+",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "+")
)
button_minus = tk.Button(
    window,
    text="-",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "-")
)
button_multiply = tk.Button(
    window,
    text="*",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "*")
)
button_divide = tk.Button(
    window,
    text="/",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "/")
)
button_equals = tk.Button(
    window,
    text="=",
    font=("GentySans",20),
    width=5,
    height=2,
    command=calculate
)
button_clear = tk.Button(
    window,
    text="AC",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.delete(0, tk.END)
)
button_dot = tk.Button(
    window,
    text=".",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, ".")
)
button_exponent = tk.Button(
    window,
    text="^",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "**")
)
button_sqrt = tk.Button(
    window,
    text="√",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "**0.5")
)
button_left_paren = tk.Button(
    window,
    text="(",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "(")
)
button_right_paren = tk.Button(
    window,
    text=")",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, ")")
)
button_In = tk.Button(
    window,
    text="In",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "In(")
)
button_sin = tk.Button(
    window,
    text="sin",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "math.sin(")
)
button_cos = tk.Button(
    window,
    text="cos",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "math.cos(")
)
button_tan = tk.Button(
    window,
    text="tan",
    font=("GentySans",20),
    width=5,
    height=2,
    command=lambda: display.insert(tk.END, "math.tan(")
)

button_In.grid(row=1, column=3)
button_sin.grid(row=3, column=5)
button_cos.grid(row=1, column=5)
button_tan.grid(row=2, column=5)
button_left_paren.grid(row=1, column=6)
button_right_paren.grid(row=2, column=6)
button_exponent.grid(row=3, column=3)
button_sqrt.grid(row=2, column=3)
button_clear.grid(row=4, column=0)
button_dot.grid(row=4, column=2)
button_plus.grid(row=1, column=4)
button_minus.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)
button_equals.grid(row=4, column=3)
button7.grid(row=1, column=2)
button8.grid(row=1, column=1)
button9.grid(row=1, column=0)
button6.grid(row=2, column=0)
button5.grid(row=2, column=1)
button4.grid(row=2, column=2)
button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)   
button0.grid(row=4, column=1)
display.grid(row=0, column=0, columnspan=5)
#This is the code for the UI, will add later the equations.


#This is the basic math involved in a calculator. It can add, subtract, multiply, and divide two numbers.
#On the future I will add more features to this calculator, such as the ability to calculate sqaure roots, exponents, and more complex operations.
#Maybe I can even make it be able to graph functions.
window.configure(bg="#202124")
window.mainloop()