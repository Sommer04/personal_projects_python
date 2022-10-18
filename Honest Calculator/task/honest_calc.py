# write your code here
msg_0 = "Enter an equation"
memory = 0
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_list = ["Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]


def check (v1,v2,v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*" :
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-" ):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
        return
    else:
        return


def is_one_digit(v):

    if (-10 < v < 10) and v.is_integer():
        output = True
    else:
        output = False
    return output

def check_operation(q):
    global result
    if q == "+" or q == "-" or q == "*" or q == "/":
        check(x, y, q)
        if q == "+":
            result = x + y
            print(result)
        elif q == "-":
            result = (x - y)
            print(result)
        elif q == "*":
            result = x * y
            print(result)
        elif q == "/" and y != 0:
            result = x / y
            print(result)
        elif q == "/" and y == 0:
            print(msg_3)
            return

while True:
    try:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        elif y == "-M" or x == "-M":
            print()
        x = float(x)
        y = float(y)

        if (x is float) or (y is float):
            print(msg_1)
            continue

        check_operation(oper)

        if result == result:
            answer = input(msg_4)
            if answer == 'y':
                if is_one_digit(result):
                    msg_index = 0
                    while msg_index < 3:
                        print(msg_list[msg_index])
                        one_digit_answer = input()
                        if one_digit_answer == "y" and msg_index < 3:
                            msg_index += 1
                        elif one_digit_answer == "n":
                            break
                    else:
                        memory = result
                elif is_one_digit(result) == False:
                    memory = result
                print(msg_5)
                operation_resume = input()
            elif answer == 'n':
                print(msg_5)
                operation_resume = input()
            if operation_resume == 'y':
                continue
            elif operation_resume == 'n':
                break
            else:
                continue
        else:
           print(msg_2)
           continue
    except ValueError:
        print(msg_1)
        continue

