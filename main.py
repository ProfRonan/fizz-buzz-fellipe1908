print("Digite um numero: ")
num = int(input(">>"))
if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
else:
    if num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
