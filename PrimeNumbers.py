def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):   
        if n % i == 0:
            return False
    return True

def primes(first_value, last_value):
    return [num for num in range(first_value, last_value + 1) if is_prime(num)]


first_value = int(input("Enter the first value: "))  
last_value = int(input("Enter the last value: "))    


print(f"Prime numbers are: {primes(first_value, last_value)}")
