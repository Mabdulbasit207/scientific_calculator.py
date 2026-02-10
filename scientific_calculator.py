class Calculator:
    def addition (self ,num1, num2):
        return num1 + num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 / num2
    def exponent(self, num1, num2):
        return num1 // num2
    def remainder(self, num1, num2):
        return num1 % num2
    def power(self, num1, num2):
        return num1 ** num2

def inp_usage(num):
    usage = []
    for _ in range(num):
        out_inp = float(input("Enter a number: "))
        usage.append(float(out_inp))
    return usage

obj = Calculator()

num1, num2 = inp_usage(2)
o_input = input("choose operation: + - * / % % ")

if o_input == "+":
    res = obj.addition(num1,num2)
    print(res)

elif o_input == "-":
    res= obj.subtraction(num1,num2)
    print(res)
elif o_input == "*":
    res = obj.multiplication(num1,num2)
    print(res)
elif o_input == "/":
    res=obj.division(num1,num2)
    print(res)
elif o_input == "^":
    res=obj.exponent(num1,num2)
    print(res)
elif o_input == "%":
    res=obj.remainder(num1,num2)
    print(res)
elif o_input == "**":
    res=obj.power(num1,num2)
    print(res)












