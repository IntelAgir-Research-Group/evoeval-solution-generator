
def correct_bracketing_advanced(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket in '([{':
            stack.append(bracket)
        elif bracket in ')]}':
            if not stack:
                return False
            if bracket == ')' and stack[-1] != '(':
                return False
            if bracket == ']' and stack[-1] != '[':
                return False
            if bracket == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return not stack

if __name__ == '__main__':
    inputs = [['('], ['()'], ['(()())'], [')(()'], ['[{()}]'], ['[{()}'], ['{[()]}'], ['{[(])}'], ['{(([{()}]))}'], ['(((([]{()}))))'], ['{()}[]{[()]()}'], ['[({})]({[()]})[{}]'], ['{[([{()}])]}'], ['{}{}{}[][][][]()()()'], ['{()}'], ['{[()]}[()]{()}[{}]'], ['{[()]}(([])){}{}{[[]]}'], ['{()}{[()]({{}})[{}]}'], ['{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}'], ['{[]{()}}[(([]))]'], ['{[({[{[()]}])]}]'], ['{[(((([])){}))]}'], ['{[()]({[(())]})}'], ['{[(((())))]}'], ['{[(((((((((((()))))))))))))]}'], ['{[()]({[{[]}]})}'], ['{[(()(()))]}'], ['{[((((()))))]}'], ['{[((()))]}[()]{()}'], ['{[((()))(()())()]}'], ['(({{[[()]]}}))'], ['{[((()))]}'], ['[({{[()]}})]'], ['({[()]})[{[()]}]'], ['{[()][()]{}([])}'], [''], ['(((((((((())))))))))'], ['{((())[][])}[{}]({})'], ['()[]{}{[()]()}'], ['()()()()(((((([]))))){{{{{{}}}}}}'], ['(((((({{{{{{[[[[[[]]]]]]}}}}}}))))))'], ['{[()]}{[()]}{[()]}'], ['{[()]}(){}[][]'], ['{[()]}{[((()))]}{[({{}})]}'], ['(((((((((({{{[[[()]]]}}})))))))))))'], ['({[()]}{[()]}[()]{[()]})'], ['({[()]})({[()]})[()]({[()]})'], ['({[()]})({[()]}[()]({[()]}))'], ['({[()]})({[()]})[()]({[()]}))'], ['[({[()]})({[()]})[()]({[()]})]'], ['[[[[[[[[[[[]]]]]]]]]]]'], ['{(((((((((((())))))))))))}'], ['{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}'], ['({[()]}{}[()][]{[()]})'], ['({[()]}{}[()][]{[()]}){[()]}{[()]}'], ['({[()]}{[()]}[()]({[()]}))'], ['{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}{[()]}'], ['({[()]}{[()]}[()]({[()]}))'], ['{{[[(())]]}}'], ['[]{}()[]{}()'], ['(([([])]))'], ['{[}()]'], ['({[({({})})]})'], ['((([]))){}[]'], ['(())({{[[]]}}){}'], ['{[()]}()[][]{}'], ['(]{}'], [')(((([])))[]{}[]{{}}'], ['[[[]]]({{}})'], ['((((((()))))))'], ['{({({({({})})})})}'], [''], ['([{'], [')]}'], ['({[]})'], ['{[()]}{[()]}'], ['(((((((((('], ['}}}}}}}}'], ['[[[[[[[[[['], ['()[]{}'], ['{(})'], ['{()}[]'], ['{()}[{()}]'], ['({[({[({[})]})]})]'], ['({[({[({[})]})]})'], ['({[({[({[})]})]})]']]
    number_of_executions = 2666666
    inputs_len = len(inputs)

    execution_counter = 0
    inputs_counter = 0

    while execution_counter != number_of_executions:
        a = correct_bracketing_advanced(*inputs[inputs_counter])
        inputs_counter += 1

        if inputs_counter == inputs_len:
            inputs_counter = 0
            execution_counter += 1

