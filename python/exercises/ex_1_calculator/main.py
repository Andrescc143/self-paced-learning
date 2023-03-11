from calculator import operations, utilities

while True:
    user_opt = input("Select an operation (number):\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n\n")
    
    if user_opt:        
        num_to_op = utilities.num_to_operate()
    
        if user_opt == "1":          
            if num_to_op:      
                print(f"Addition result: {operations.addition(*num_to_op)}\n\n")

        elif user_opt == "2":
            if num_to_op:
                print(f"Subtraction result: {operations.subtraction(*num_to_op)}\n\n")
                
        elif user_opt == "3":
            if num_to_op:
                print(f"Division result: {operations.division(*num_to_op)}\n\n")
        
        elif user_opt == "4":
            if num_to_op:
                print(f"Multiplication result: {operations.multiplication(*num_to_op)}\n\n")
        else:
            print("Wrong input, try again")
    else:
        print("See you later !")
        break
    