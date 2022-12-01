def Rcalculator(a,b,r):
    if r == "+":
        return (a + b)
    elif r == "-":
        return (a - b)
    elif r == "*":
        return (a * b)
    elif r == "/":
        return (a / b)
    else:
        return "Please enter a proper operator"
print(Rcalculator(22, 33, "a"))