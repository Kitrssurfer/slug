from time import sleep

def run():
    if line2 == "run" or line3 == "run":
        if line1 == "print":
            print(line2)

        else:
            if line1 == "input":
                input(line2)

            else:
                if line1 == "if":
                    if line2 == True:
                        print("test working")
                    else:
                        if line1 == "if":
                            print("if statment error! At line 1")
                        else:
                            print("code error! At line 1")
                            


    if line3 == "run" or line4 == "run":
        if line1 == "print":
            print(line3)

        else:
            if line3 == "input":
                input(line4)

            else:
                if line3 == "if":
                    if line4 == True:
                        print("test working")
                    else:
                        
                        if line3 == "if":
                                print("if statment error! At line 1")
                        else:
                            print("code error! At line 1")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
if line3 == "run":
    run()
    
line4 = input("line 4: ")
if line4 == "run":
    run()

line5 = input("line 5: ")
if line5 == "run":
    run()

line6 = input("line 6: ")
if line6 == "run":
    run()

line7 = input("line 7: ")
if line7 == "run":
    run()

line8 = input("line 8: ")
if line8 == "run":
    run()

line9 = input("line 9: ")
if line9 == "run":
    run()

line10 = input("line 10: ")
if line10 == "run":
    run()
