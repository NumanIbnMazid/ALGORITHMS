"""
Keywords: Linear Data Structure, LIFO
Terms:
    - push: putting an element on the top of the stack
    - pop: removing the top element of the stack
Basic Operations:
    - push(x): add an element x to the top of the stack
    - pop(): remove the top element of the stack
    - isEmpty(): return True if the stack is empty
    - isFull(): return True if the stack is full
    - peek(): return the top element of the stack
Time Complexity:
    - push: O(1)
    - pop: O(1)
Notes:
    - In browsers - The back button in a browser saves all the URLs you have visited previously in a stack. Each time you visit a new page, it is added on top of the stack. When you press the back button, the current URL is removed from the stack, and the previous URL is accessed.
    - In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9) by converting the expression to prefix or postfix form.
"""

# creating a stack
def create_stack():
    stack = []
    return stack

# check if stack is empty
def check_empty(stack):
    return len(stack) == 0

# adding items to stack
def push(stack, item):
    stack.append(item)
    print("Pushed item: ", item)
    
# removing an element from stack
def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("stack after pushing elements: ", stack)
print("popped item: ", pop(stack))
print("stack after popping element: ", stack)