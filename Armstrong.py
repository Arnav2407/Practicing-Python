num = int(input("Enter a number: "))
power = len(str(num))
sum_of_powers = sum(int(digit) ** power for digit in str(num))
if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
