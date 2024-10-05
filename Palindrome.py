def palindrome(s):


    processed_str = s.replace(" ", "").lower()  
    return processed_str == processed_str[::-1]

value = input("Enter a string: ")
if palindrome(value):
    print(f"'{value}' is a palindrome.")
else:
    print(f"'{value}' is not a palindrome.")