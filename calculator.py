num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
operator=input("choose the operator")

match operator:
    case "+":
        print("the sum is ",num1 + num2)
    case "-":
        print("the subtract is",num1 - num2)
    case "*" : 
        print("the multiply is ",num1 * num2)
    case "/":
        print("the divide is  " , num1 / num2)
    case "%":
        print("the remender is ",num1 % num2)
    case "**":
        print("the answer of power is", num1 ** num2)        
    case "_":
        print("enter the valid operator")                 