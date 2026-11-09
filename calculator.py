import tkinter as tk

#main GUI code
root = tk.Tk()
root.title("Simple Calculator")

placeholder_text = "Enter the expression to be evaluated"
def erasePlaceholder(event):
    if exp.get() == placeholder_text:
        exp.delete(0,tk.END)

def placeHolder(event):
    if exp.get() == "":
        exp.insert(0,placeholder_text)

#input the mathematical expression
exp = tk.Entry(root,width=50,borderwidth=2)
exp.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipadx=10,ipady=10)

#place holder management
exp.insert(0,placeholder_text)
exp.bind("<FocusIn>", erasePlaceholder)
exp.bind("<FocusOut>", placeHolder)

#handle evaluation
def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    postfix = []

    for char in infix.replace(" ", ""):
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[char]:
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())
    
    return "".join(postfix)


def evaluate_postfix(postfix):
    stack = []

    for char in postfix:
        if char.isdigit():  # Push numbers onto the stack
            stack.append(float(char))
        else:  # Operator: pop two numbers and apply it
            b = stack.pop()
            a = stack.pop()
            if char == '+': stack.append(a + b)
            elif char == '-': stack.append(a - b)
            elif char == '*': stack.append(a * b)
            elif char == '/': stack.append(a / b)

    return stack.pop()

#handle button clicks
def button_click(value):
    if value == "AC":
        exp.delete(0,tk.END)
    elif value == "( )":
        if exp.get() == placeholder_text:
            exp.delete(0,tk.END)
        exp.insert(tk.END,"( )")
    elif value == "=":
        expression = exp.get()
        postfix = infix_to_postfix(expression)
        print(evaluate_postfix(postfix))

buttons = [
    ("AC", 1, 0, 10, 5),
    ("( )", 1, 1, 5, 5),
    ("%", 1, 2, 5, 5),
    ("/", 1, 3, 5, 10),
    ("7", 2, 0, 5, 5),
    ("8", 2, 1, 5, 5),
    ("9", 2, 2, 5, 5),
    ("*", 2, 3, 5, 10),
    ("4", 3, 0, 5, 5),
    ("5", 3, 1, 5, 5),
    ("6", 3, 2, 5, 5),
    ("-", 3, 3, 5, 10),
    ("1", 4, 0, 5, 5),
    ("2", 4, 1, 5, 5),
    ("3", 4, 2, 5, 5),
    ("+", 4, 3, 5, 10),
    ("0", 5, 0, 5, 5),
    (".", 5, 1, 5, 5),
    ("<-", 5, 2, 5, 5),
    ("=", 5, 3, 5, 10),
]

for text, r, c, px_l, px_r in buttons:
    # Use lambda with a default argument (t=text) to capture the current button's text correctly
    btn = tk.Button(
        root, 
        text=text, 
        borderwidth=2, 
        padx=10, 
        pady=10,
        command=lambda t=text: button_click(t)
    )
    btn.grid(row=r, column=c, columnspan=1, sticky="ew", padx=(px_l, px_r), pady=5)
    
if __name__ == "__main__":
    root.mainloop()
