def calculator(a,b,c):
    if c == "+":
        print(f"{a}+{b}={a + b}")
    elif c == "-" :
        print(f"{a}-{b}={a - b}")
    elif c == "*" :
        print(f"{a}*{b}={a * b}")
    elif c == "//" :
        print(f"{a}/{b}={a // b}")
    else:
        print("Please enter correct value")