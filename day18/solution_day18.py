import re


def evaluate_expression(expression_str):
    tokens = re.findall(r'\d+|.', expression_str.replace(' ', ''))
    return evaluate_expression_aux(tokens)


def evaluate_expression_aux(tokens):
    '''
    Evaluates the outcome of a list of tokens:
    Tokens are: numbers, '(', ')', '+' and '*'
    '''
    while len(tokens) > 0:
        token = tokens.pop(0)
        if re.match(r'\d+', token):
            token = int(token)
            try:
                result = perform_operation(result, operator, token)
            except NameError:
                # No operation pending
                result = token
        elif token == '+' or token == '*':
            operator = token
        elif token == '(':
            bracket_token = evaluate_expression_aux(tokens)
            try:
                result = perform_operation(result, operator, bracket_token)
            except NameError:
                # No operation pending
                result = bracket_token
        elif token == ')':
            return result
        else:
            raise ValueError
    return result


def evaluate_expression_B(expression_str):
    tokens = re.findall(r'\d+|.', expression_str.replace(' ', ''))
    return evaluate_expression_aux_B(tokens)


def perform_operation(lhs, operator, rhs):
    if operator == "+":
        return lhs + rhs
    elif operator == "*":
        return lhs * rhs


def evaluate_expression_aux_B(tokens):
    '''
    Evaluate expression with rules B.
    Returns: expression value + expression length, needed for replacing
    bracketed expressions.
    '''
    if len(tokens) == 1:
        return int(tokens[0]), 1

    # Deal with top-level brackets first
    for i, token in enumerate(tokens):
        if tokens[i] == '(':
            # find closing bracket
            value, expression_length = evaluate_expression_aux_B(tokens[i+1:])
            tokens[i:(i + expression_length + 2)] = [value]
            value, length = evaluate_expression_aux_B(tokens)
            return value, length + expression_length + 1
        elif tokens[i] == ')':
            value, length = evaluate_expression_aux_B(tokens[:i])
            return value, length

    for i, token in enumerate(tokens):
        if tokens[i] == '+':
            tokens[i-1:i+2] = [int(tokens[i - 1]) + int(tokens[i + 1])]
            value, length = evaluate_expression_aux_B(tokens)
            return value, length + 2

    for i, token in enumerate(tokens):
        if tokens[i] == '*':
            tokens[i-1:i+2] = [int(tokens[i - 1]) * int(tokens[i + 1])]
            value, length = evaluate_expression_aux_B(tokens)
            return value, length + 2

    raise ValueError




if __name__ == "__main__":
    path = "./day18/input.txt"
    with open(path) as f:
        solution18A = sum([evaluate_expression(line.strip()) for line in f])
    print("Solution 18A")
    print(solution18A)

    with open(path) as f:
        solution18B = sum([evaluate_expression_B(line.strip())[0] for line in f])
    print("Solution 18B")
    print(solution18B)
