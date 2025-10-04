def main() :
    Confirmation = input("Would like to know what type of Operations are available (y or n): ")
    if Confirmation == "y":
        Message = """
        + for Addition
        - for Subtraction
        * for multiplication
        / for division
        """
        print(Message)
    else : 
        print("Alright")
    User_InputA = int(input("Enter a Number1: "))
    User_InputB = int(input("Enter a Number2: "))
    Operation = input ("Enter a Operator: ")
    Answer = 0

    if Operation == "+" :
        Answer = User_InputA + User_InputB
    elif Operation == "-" :
        Answer = User_InputA - User_InputB
    elif Operation == "*" :
        Answer = User_InputA * User_InputB
    elif Operation == "/" :
        if User_InputB == 0:
            print("Don't Enter 0 for 2nd Number in division")
            main()
            return
        else:
            Answer = User_InputA / User_InputB
    else :
        print("No such operation exists")
        main()
        return

    print(f"Your answer is: {Answer}")

main()



