import stack as st 
import tokenizer as tkn
import infixToPostfix as itp

#define lists with the operators and digits
operators  = tkn.operators
digits = tkn.digits     

if __name__ == '__main__':
    #initialize the stack
    stack = st.Stack()

    #infinite loop for continuously taking inputs
    while True: 
        expression = input("Please enter an expression ('q' to exit, 'h' for help): ") #prompt
        if expression == 'q': #exit condition
            print("Bye! have a great time!")
            break

        elif expression == 'clr': #clearing answer 
            stack.stack.clear()

        elif expression == 'ans': #showing current answer in stack
            stack.display()

        elif expression == 'h':   #show commands
            print(f"""'q' = Exit
'clr' = Clear answer
'ans' = sho current answer in stack
'h' = help
If you want to continue from the previous answer, just start the current expression with an operator
Current Answer value in the stack: {stack.stack}""")
            
        else:
            infix = tkn.tokenizeInfix(expression)
            if infix[0] not in tkn.operatorsInfix or infix[0] == '(':
                stack.stack.clear()

            postfix = itp.infixToPostfix(expression)
            tokens = tkn.tokenize(postfix) #tokenizes the expression into operators and operands

            if tokens != 'VOID': #token list validization condition
                for token in tokens: #iterate through each token
                    if  token not in operators:  #if token is not an operator (it is an operand), then push it into the stack
                        stack.push(float(token)) 
                    else:                 
                        #If the length of the stack is less than 2, then there aren't enough operands to operate on, so throw an error     
                        if len(stack.stack) < 2:   
                            print("Syntax Error!")
                            stack.stack.clear()
                            break

                        #Pop the top two elements from the stack
                        a = stack.pop()
                        b = stack.pop()

                        #Perform operations on a and b
                        if token == '+':
                            stack.push(a + b) 
                        elif token == '-':
                            stack.push(b - a)
                        elif token == '*':
                            stack.push(b * a)
                        elif token == '/':
                            if a != 0:
                                stack.push(b / a)
                            else:
                                print("Math Error! Division by Zero is undefined!") #throw error is division by zero
                                break
                        elif token == '^':
                            stack.push(b ** a)
                        elif token == '&':
                            stack.push(int(a) & int(b))
                        elif token == '|':
                            stack.push(int(a) | int(b))
                        elif token == 'v':
                            stack.push(int(a) ^ int(b))      

            #If stack has one element after all operations, it means that the answer and expression was valid. So display the answer        
            if len(stack.stack) <= 1:    
                stack.display()
        
            #If length is more than one, then it means the expression was not valid, throw an error
            elif len(stack.stack) > 1:
                print("Syntax Error!")
                stack.stack.clear()
                    
#For more updates, like and subscribe, but wait, I don't have a youtube channel!😅😅