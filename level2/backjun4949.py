while True:
    st = input()
    if st == ".":
        break
    stack = []
    boolean = True
    for s in st:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']':
            if not stack:
                boolean = False
                break
            c = stack.pop()
            if c != '[':
                boolean = False
                break
        elif s == ')':
            if not stack:
                boolean = False
                break
            c = stack.pop()
            if c != '(':
                boolean = False
                break
    if not stack and boolean:
        print("yes")
    else:
        print("no")