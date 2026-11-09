import tkinter as tk

#main GUI code
root = tk.Tk()
root.title("Simple Calculator")

def erasePlaceholder(event):
    if exp.get() == "Enter the expression to be evaluated":
        exp.delete(0,tk.END)

def placeHolder(event):
    if exp.get() == "":
        exp.insert(0,"Enter the expression to be evaluated")

#input the mathematical expression
exp = tk.Entry(root,width=50,borderwidth=2)
exp.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipadx=10,ipady=10)

#place holder management
exp.insert(0,"Enter the expression to be evaluated")
exp.bind("<FocusIn>", erasePlaceholder)
exp.bind("<FocusOut>", placeHolder)

##ROWS
#row1 = AC, (), %, /
clearBtn = tk.Button(root, text="AC", borderwidth=2, padx=10, pady=10)
clearBtn.grid(
    row=1,
    column=0,
    columnspan=1,
    sticky="ew",
    padx=(10,5),
    pady=5
)
bracketBtn = tk.Button(root, text="( )", borderwidth=2, padx=10, pady=10)
bracketBtn.grid(
    row=1,
    column=1,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
modBtn = tk.Button(root, text="%", borderwidth=2, padx=10, pady=10)
modBtn.grid(
    row=1,
    column=2,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
divBtn = tk.Button(root, text="/", borderwidth=2, padx=10, pady=10)
divBtn.grid(
    row=1,
    column=3,
    columnspan=1,
    sticky="ew",
    padx=(5,10),
    pady=5
)

#row2 7, 8, 9, x
btn_7 = tk.Button(root, text="7", borderwidth=2, padx=10, pady=10)
btn_7.grid(
    row=2,
    column=0,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
btn_8 = tk.Button(root, text="8", borderwidth=2, padx=10, pady=10)
btn_8.grid(
    row=2,
    column=1,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
btn_9 = tk.Button(root, text="9", borderwidth=2, padx=10, pady=10)
btn_9.grid(
    row=2,
    column=2,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
multiply = tk.Button(root, text="x", borderwidth=2, padx=10, pady=10)
multiply.grid(
    row=2,
    column=3,
    columnspan=1,
    sticky="ew",
    padx=(5,10),
    pady=5
)

#row3 4, 5, 6, -
btn_4 = tk.Button(root, text="4", borderwidth=2, padx=10, pady=10)
btn_4.grid(
    row=3,
    column=0,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
btn_5 = tk.Button(root, text="5", borderwidth=2, padx=10, pady=10)
btn_5.grid(
    row=3,
    column=1,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
btn_6 = tk.Button(root, text="6", borderwidth=2, padx=10, pady=10)
btn_6.grid(
    row=3,
    column=2,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
subtract = tk.Button(root, text="-", borderwidth=2, padx=10, pady=10)
subtract.grid(
    row=3,
    column=3,
    columnspan=1,
    sticky="ew",
    padx=(5,10),
    pady=5
)

#row4 1, 2, 3, +
btn_1 = tk.Button(root, text="1", borderwidth=2, padx=10, pady=10)
btn_1.grid(
    row=4,
    column=0,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
btn_2 = tk.Button(root, text="2", borderwidth=2, padx=10, pady=10)
btn_2.grid(
    row=4,
    column=1,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
btn_3 = tk.Button(root, text="3", borderwidth=2, padx=10, pady=10)
btn_3.grid(
    row=4,
    column=2,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
addition = tk.Button(root, text="+", borderwidth=2, padx=10, pady=10)
addition.grid(
    row=4,
    column=3,
    columnspan=1,
    sticky="ew",
    padx=(5,10),
    pady=5
)

#row5 0, . , backspace, =
# #row2 7, 8, 9, x
btn_0 = tk.Button(root, text="0", borderwidth=2, padx=10, pady=10)
btn_0.grid(
    row=5,
    column=0,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
dotBtn = tk.Button(root, text=".", borderwidth=2, padx=10, pady=10)
dotBtn.grid(
    row=5,
    column=1,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
backSpace = tk.Button(root, text="<-", borderwidth=2, padx=10, pady=10)
backSpace.grid(
    row=5,
    column=2,
    columnspan=1,
    sticky="ew",
    padx=5,
    pady=5
)
equals = tk.Button(root, text="=", borderwidth=2, padx=10, pady=10)
equals.grid(
    row=5,
    column=3,
    columnspan=1,
    sticky="ew",
    padx=(5,10),
    pady=5
) 

if __name__ == "__main__":
    root.mainloop()
