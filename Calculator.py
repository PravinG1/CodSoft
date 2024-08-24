# Simple calculator
while True:
    print("**Menu**")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    print("---------------------------------------------------------------------\n")
    ch = int(input("Enter your choice:"))
    print("-------------------------------------------------")
    if (ch==1):
        num1 = int(input("\nEnter the 1st number:"))
        num2 = int(input("Enter the 2nd number:"))
        print(f"\nAddition of : {num1} + {num2}={num1+num2}\n")
        print("----------------------------------------------------")
    elif(ch==2):
        num1 = int(input("\nEnter the 1st number:"))
        num2 = int(input("Enter the 2nd number:"))
        print(f"\nSubstraction of : {num1} - {num2}= {num1-num2}\n")
        print("----------------------------------------------------")
    elif(ch==3):
        num1 = int(input("\nEnter the 1st number:"))
        num2 = int(input("Enter the 2nd number:"))
        print(f"\nMultiplication of : {num1} * {num2} = {num1*num2}\n")
        print("----------------------------------------------------")
    elif(ch==4):
        num1 = int(input("\nEnter the 1st number:"))
        num2 = int(input("Enter the 2nd number:"))
        ans = num1 / num2
        print(f"\nDivision of : {num1} / {num2} = {ans:.2f}\n")
        print("----------------------------------------------------")
    elif(ch==5):
        print("Exiting....Thank You...!")
        break
    else:
        print("Please enter valid choice...!")
