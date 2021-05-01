import math
import random

res = 0
n1 = ""
op = ""
n2 = ""
mem = "Empty"

def helpme():
    print("Type + for Addition")
    print("Type - for Subtraction")
    print("Type * for Multiplication")
    print("Type / for Division")
    print("Type ^ for Powers")
    print("Type sqrt for Square Roots ")
    print("Type ! for Factorial (Inputs Cannot Be Negative)")
    print("Type Abs for Absolute Value")
    print("Type d/r for Degrees To Radians")
    print("Type r/d for Radians To Degrees")
    print("Type pi for Returns PI")
    print("Type e for Returns 'e'")
    print("Type tau for Returns TAU (2xPI)")
    print("Type M+ for Save input to memory")
    print("Type MR for Recall Memory")
    print("Type M- for Clear Memory")
    print("Type sin for Sine")
    print("Type cos for Cosine")
    print("Type tan for Tangent")
    print("Type asin for Arc Sine")
    print("Type acos for Arc Cosine")
    print("Type atan for Arc Tangent")
    print("Type log10 for Log(10) of Input")
    print("Type log Returns The Apropriate Log of the Input (input1 is the log power)")
    print("Type rand Returns A Random Number Between 0 and 1")
    print("Type randint Returns A Random Number Between The Two Inputs")
    print("Type exit To terminate the program")

def userinput(textPrompt):

    cnum = math.nan

    while True:
        num = input(textPrompt)
        try:

            float(num)
        except ValueError:

            print("ERROR: Invalid Num")
        else:

            cnum = float(num)
            break
    return cnum


while True:
    print("Type 'help' for operations names")

    while True:
        op = input("What operation do you want to perform? ")

        if op == "help":
            helpme()
        elif op == "pi":
            print(math.pi)
        elif op == "e":
            print(math.e)
        elif op == "tau":
            print(math.pi*2)
        elif op == "MR":
            print(str(mem))
        elif op == "M-":
            mem = "Empty"
            print("Memory Cleared")
        elif op == "rand":
            print(random.random())

        elif op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "sqrt" or op == "!" or op == "Abs" or op == "d/r" or op == "r/d" or op == "M+" or op == "M-" or op == "MR" or op == "sin" or op == "cos" or op == "tan" or op == "asin" or op == "acos" or op == "atan" or op == "log10" or op == "log" or op == "randint" or op=="exit":
            break
        else:
            print("ERROR: Invalid op")
    if (op=="exit"):
        break;

    while True:
        n1 = userinput("First Number? ")
        # Catch asin and acos out of bounds error case
        if (op == "asin" or op == "acos") and (n1 > 1 or n1 < -1):
            print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
        elif op == "!" and n1 < 0:
            print("ERROR: Math: Factorials only accept inputs > 0")
        else:
            break


    if not (op=="sqrt" or op=="!" or op=="Abs" or op=="d/r" or op=="r/d" or op=="M+" or op=="sin" or op=="cos" or op=="tan" or op=="asin" or op=="acos" or op=="atan" or op=="log10" or op=="exit"):
        # Loop for 2nd number input
        while True:
            n2 = userinput("Second Number? ")
            
            if  op == "/" and n2 == "0":
                print("ERROR: Math: Canot divide by 0!")
            else:
                break


    if op == "+":
        res = n1 + n2
        print("Your Answer: "+str(res))
    elif op == "-":
        res = n1 - n2
        print("Your Answer: "+str(res))
    elif op == "*":
        res = n1 * n2
        print("Your Answer: "+str(res))
    elif op == "/":
        res = n1 / n2
        print("Your Answer: "+str(res))
    elif op == "^":
        res = math.pow(n1,n2)
        print("Your Answer: "+str(res))
    elif op == "sqrt":
        res = math.sqrt(n1)
        print("Your Answer: "+str(res))
    elif op == "!":
        res = math.factorial(n1)
        print("Your Answer: "+str(res))
    elif op == "Abs":
        res = math.fabs(n1)
        print("Your Answer: "+str(res))
    elif op == "d/r":
        res = math.radians(n1)
        print("Your Answer: "+str(res))
    elif op == "r/d":
        res = math.degrees(n1)
        print("Your Answer: "+str(res))
    elif op == "M+":
        mem = n1
        print("Number Stored")
    elif op == "sin":
        res = math.sin(n1)
        print("Your Answer: "+str(res))
    elif op == "cos":
        res = math.cos(n1)
        print("Your Answer: "+str(res))
    elif op == "tan":
        res = math.tan(n1)
        print("Your Answer: "+str(res))
    elif op == "asin":
        res = math.asin(n1)
        print("Your Answer: "+str(res))
    elif op == "acos":
        res = math.acos(n1)
        print("Your Answer: "+str(res))
    elif op == "atan":
        res = math.atan(n1)
        print("Your Answer: "+str(res))
    elif op == "log10":
        res = math.log10(n1)
        print("Your Answer: "+str(res))
    elif op == "log":
        res = math.log(n2, n1)
        print("Your Answer: "+str(res))
    elif op == "randint":
        res = random.randint(n1, n2)
        print("Your Answer: "+str(res))
    elif op == "exit":
        break
