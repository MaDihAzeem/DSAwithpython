def calculator():
    while True:
        print("  ------------calculator menu-------------     ")
        print("1.ADD")
        print("2.sub")
        print("3.mul")
        print("4.divi")
        choice=int(input("enter your choice"))
        if choice==0:
            print("exit:")
            break
        elif choice==1:
            n1=float(input("enter first no:"))
            n2=float(input("enter seconf no:"))
            print("sum:",n1+n2)
        elif choice==2:
            n1=float(input("enter first no:"))
            n2=float(input("enter seconf no:"))
            print("sub:",n1-n2)
        elif choice==3:
            n1=float(input("enter first no:"))
            n2=float(input("enter seconf no:"))
            print("product:",n1*n2)
        elif choice==4:
            n1=float(input("enter first no:"))
            n2=float(input("enter seconf no:"))
            print("divi:",n1/n2)
        else:
            print("error")
calculator()            

           


