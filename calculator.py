import re
import tkinter as tk

# main GUI code
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x500")

# flex container
flex_container = tk.Frame(root)
flex_container.pack(fill="x", padx=10, pady=10, ipady=10)

# --- FLEXBOX GRID BALANCER ---
# This ensures all 4 columns inside the frame scale up evenly together
for i in range(4):
    flex_container.columnconfigure(i, weight=1)

placeholder_text = "Enter the expression to be evaluated"


def erasePlaceholder(event):
    if exp.get() == placeholder_text:
        exp.delete(0, tk.END)


def placeHolder(event):
    if exp.get() == "":
        exp.insert(0, placeholder_text)


# input the mathematical expression
exp = tk.Entry(flex_container, borderwidth=2)
exp.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10, sticky="ew")

# place holder management
exp.insert(0, placeholder_text)
exp.bind("<FocusIn>", erasePlaceholder)
exp.bind("<FocusOut>", placeHolder)


# handle evaluation
def infix_to_postfix(infix):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    postfix = []

    tokens = re.findall(r"\d+\.\d+|\d+|[+\-*/()]", infix.replace(" ", ""))

    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            postfix.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (
                stack
                and stack[-1] != "("
                and precedence.get(stack[-1], 0) >= precedence[token]
            ):
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
        if token.replace(".", "", 1).isdigit():
            stack.append(float(token))
        else:
            if len(stack) < 2:
                return "Error"
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    return "Div by 0"
                stack.append(a / b)

    return stack.pop() if stack else 0


# handle button clicks
def button_click(value):
    current = exp.get()
    if value == "AC":
        exp.delete(0, tk.END)
    elif value == "( )":
        if current == placeholder_text:
            exp.delete(0, tk.END)
        exp.insert(tk.END, "()")
    elif value == "=":
        expression = current
        postfix = infix_to_postfix(expression)
        final_answer = evaluate_postfix(postfix)
        
        if isinstance(final_answer, float) and final_answer.is_integer():
            final_answer = int(final_answer)

        display_result = tk.Label(
            flex_container, font=("Arial", 12, "bold"), fg="darkgreen", text=final_answer
        )
        display_result.grid(
            row=6, column=0, columnspan=4, sticky="ne", padx=(0, 10), pady=10
        )
    elif value == "<-":
        if current and current != placeholder_text:
            exp.delete(len(current) - 1, tk.END)
    else:
        if current == placeholder_text:
            exp.delete(0, tk.END)
        exp.insert(tk.END, value)


buttons = [
    ("AC", 1, 0, 10, 5),
    ("( )", 1, 1, 5, 5),
    ("%", 1, 2, 5, 5),
    ("/", 1, 3, 5, 10),
    ("7", 2, 0, 10, 5),
    ("8", 2, 1, 5, 5),
    ("9", 2, 2, 5, 5),
    ("*", 2, 3, 5, 10),
    ("4", 3, 0, 10, 5),
    ("5", 3, 1, 5, 5),
    ("6", 3, 2, 5, 5),
    ("-", 3, 3, 5, 10),
    ("1", 4, 0, 10, 5),
    ("2", 4, 1, 5, 5),
    ("3", 4, 2, 5, 5),
    ("+", 4, 3, 5, 10),
    ("0", 5, 0, 10, 5),
    (".", 5, 1, 5, 5),
    ("<-", 5, 2, 5, 5),
    ("=", 5, 3, 5, 10),
]

for text, r, c, px_l, px_r in buttons:
    btn = tk.Button(
        flex_container,
        text=text,
        borderwidth=2,
        padx=10,
        pady=10,
        command=lambda t=text: button_click(t),
    )
    btn.grid(row=r, column=c, columnspan=1, sticky="ew", padx=(px_l, px_r), pady=5)

if __name__ == "__main__":
    root.mainloop()
