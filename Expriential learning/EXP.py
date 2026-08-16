def is_balanced(expression):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in '([{':
            stack.append(char)

        elif char in ')]}':
            if not stack:
                return False

            if stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


expression = input("Enter an expression: ")

if is_balanced(expression):
    print("Balanced Parentheses")
else:
    print("Not Balanced Parentheses")