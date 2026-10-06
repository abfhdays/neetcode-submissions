class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "/", "*"])
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operators:

                b = stack.pop()  
                a = stack.pop()  

                if tokens[i] == "+":
                    value = a + b

                elif tokens[i] == "-":
                    value = a - b

                elif tokens[i] == "*":
                    value = a * b

                elif tokens[i] == "/":
                    value = int(a / b)  # truncate toward zero

                stack.append(value)

            else:
                stack.append(int(tokens[i]))

        return stack[0]