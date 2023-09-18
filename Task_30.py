list_1 = []

def is_number(msg: str):
    while True:
        num = input(msg)
        if num.isdigit():
            num = int(num)
            return num
        
beginning_number = is_number("Input a first number: ")
step = is_number("Input a common difference: ")
amount = is_number("Input the number of elements: ")
for i in range(amount):
    sum =  beginning_number + (i* step)
    list_1.append(sum)

print(list_1)