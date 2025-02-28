def check_in_range(num):
    if num in range(1, 10):
        return f"{num} is in the range."
    else:
        return f"{num} is not in the range."

print(check_in_range(5))
5 is in the range.
print(check_in_range(10))
10 is not in the range.
