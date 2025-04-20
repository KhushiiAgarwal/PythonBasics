# Given a string expr consisting of different types of parenthesis '(', ')', '{', '}', '[', ']', 
# check and return whether the expression forms a valid balanced parenthesis expression. 
# In a valid balanced parenthesis, each opening parenthesis type must have its corresponding closing parenthesis.

chars = input("Enter string: ")
stack = []
def isValid(chars):
    str = chars
    for i in str:
        if i=='(' or i=='{' or i=='[' :
            stack.append(i)
        else:
            if stack and ((stack[-1] == '(' and i == ')') or(stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}')): #check if stack is non-empty & top element is open bracket
                stack.pop()
            else:
                return False
    return not stack
print(isValid(chars))

        

