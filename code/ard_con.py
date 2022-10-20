f = open("input.txt", "r")

S = f.readline()
mas = S.split()
stack = []
l = 1
for it in mas:
    if it.isdecimal():
        stack.append(int(it))
    elif len(stack) >= 2:
        a2 = stack.pop()
        a1 = stack.pop()
        #if a2 == 0:
            #print('ERROR')
            #exit()

        if it == "/":
            if a2 == 0:
                l = 0
            if a2 != 0:
                res =  a1 // a2
        elif it == "+":
            res =  a1 + a2
        else:
            res =  a1 - a2
        stack.append(res)
    else:
        print('ERROR')
        l = 0
        exit()


with open("output.txt", "w") as F:
    if len(stack) == 1:
        F.write(str(*stack))
    elif len(stack) != 1:
        F.write("ERROR")
    elif l == 0:
        F.write("ERROR")