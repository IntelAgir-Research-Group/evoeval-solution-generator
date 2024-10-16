
def is_nested(string):
    stack = []
    for bracket in string:
        if bracket == '[':
            stack.append(bracket)
        elif bracket == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack