def third():
    #print("hello")
    try:
        print("begin third")
        n = int(input("enter n:"))
        if n == 1:
            5 / 0
        elif n == 2:
            int("qwert")        #ValueError
        else:
            a + b                   #NameError
        print("hello")
    except (ZeroDivisionError, ValueError, NameError) as exc:
        print("exception was handled:")
        print(exc)
        print(repr(exc))
        print(exc.args)
        100
    print("end third")



def second():
    print("begin second")
    third()
    print("end second")

def first():
    print("begin first")
    second()
    print("end first")

def main():
    print("begin main")
    first()
    print("end main")

main()