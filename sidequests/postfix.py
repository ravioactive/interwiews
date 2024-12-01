def infix_to_postfix(expression):
    """Converts an infix expression to postfix."""

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for char in expression:
        print(f'{char=}, {stack=}, {output=}')
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the '('
        else:
            while stack and stack[-1] != '(' and \
                precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
                print(f'\tinside {char=}, {stack=}, {output=}')
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def infix_to_postfix_mine(s: str):
        priority: dict[str, int] = {'-':1,'+':1,'*':2,'/':2,'^':3}

        i, m, output, stack = 0, len(s), [], []
        while i<m:
            print(f'{s[i]=}, {stack=}, {output=}')
            if s[i].isdigit():
                start = i
                while i<m and s[i].isdigit():
                    i+=1
                output.append(s[start:i])
            else:
                while stack and priority.get(stack[-1]) >= priority.get(s[i]):
                    print(f'\tinside {s[i]=}, {stack=}, {output=}')
                    output.append(stack.pop())
                    
                stack.append(s[i])
                i+=1

        while stack:
            output.append(stack.pop())
        
        return output

expression = "1+2*3-4-5*6+7"
print(infix_to_postfix(expression))
print(infix_to_postfix_mine(expression))