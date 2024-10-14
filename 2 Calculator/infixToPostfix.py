import stack as st
import tokenizer as tkn

operators = tkn.operatorsInfix
digits = tkn.digits

#Dictionaries containing the precedence
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
}
associativity = {
    '+': 'L',
    '-': 'L',
    '*': 'L',
    '/': 'L',
    '^': 'R',
}

def infixToPostfix(exp):
    output = []
    operatorStack = st.Stack()
    tokens = tkn.tokenizeInfix(exp)
    temp = ''
    discard = ''
    top = ''
    for token in tokens:
        if token not in operators:
            output.append(token)
        else:
            if token == '(':
                operatorStack.push(token)
            elif token == ')':
                while len(operatorStack.stack) != 0 and operatorStack.get_top() != '(':
                    temp = operatorStack.pop()
                    output.append(temp)
                
                # Pop the '(' from the stack
                if len(operatorStack.stack) != 0 and operatorStack.get_top() == '(':
                    operatorStack.pop()
                else:
                    print("Error: Mismatched parentheses")
                    return "Invalid Expression"
                
            else:
                while len(operatorStack.stack) != 0:
                    top = operatorStack.get_top()

                    if top == '(':  # Stop at left parenthesis
                        break

                    if (precedence[top] > precedence[token]) or (precedence[top] == precedence[token] and associativity[token] == 'L'):
                        temp = operatorStack.pop()
                        output.append(temp)
                    else:
                        break
                operatorStack.push(token)

    while len(operatorStack.stack) != 0:
        temp = operatorStack.pop()
        output.append(temp)

    postfix = ' '.join(output)
    return postfix

if __name__ == '__main__':  
    expression = '(2 + 2) * 2 / 2^2^2'
    p = infixToPostfix(expression)
    print(p)

