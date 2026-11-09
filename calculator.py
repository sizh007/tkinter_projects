import tkinter as tk
import re

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

    tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/()]', infix.replace(" ", ""))

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())
    
    return " ".join(postfix)


def evaluate_postfix(postfix_str):
    if not postfix_str:
        return 0
        
    stack = []
    tokens = postfix_str.split()

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            if len(stack) < 2:
                return "Error"
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': 
                if b == 0: return "Div by 0"
                stack.append(a / b)

    return stack.pop() if stack else 0

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
        final_answer = evaluate_postfix(postfix)
        display_result = tk.Label(root, font=("Arial", 12, "bold"), fg="darkgreen", text=final_answer)
        display_result.grid(row=6, column=0, columnspan=4, sticky="ne", padx=(0,10), pady=10)
    elif value == "<-":
        exp.delete(len(exp.get()) - 1, tk.END)
    else:
        if exp.get() == placeholder_text:
            exp.delete(0,tk.END)
        exp.insert(tk.END, value)

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
