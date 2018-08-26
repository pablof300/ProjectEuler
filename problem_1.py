numbers = []
sum = 0

for number in range(0,1000):
    if number % 3 == 0 | number % 5 == 0:
        numbers.append(number)

for number in numbers:
    sum = sum + number

print("The sum is " + str(sum))
