def filter(numbers):
    return [num for num in numbers if num % 2 == 0]


numbers = [11, 22, 16, 5, 60, 3]
print(filter(numbers))  
