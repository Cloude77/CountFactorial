import threading

# Define a dictionary for memoization
memo = {}


def factorial(n):
    if n in memo:
        return memo[n]

    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i

    # Store the result in the memo dictionary
    memo[n] = result
    return result


def calculate_factorial(number):
    try:
        n = int(number)
        if n < -1000 or n > 1000:
            result = factorial(n)
            # Convert the result to a string to extract the first 5 digits
            result_str = str(result)
            first_5_digits = result_str[:5]
            return f"Factorial: {result}, First 5 digits: {first_5_digits}"
        elif n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0:
            return 1
        else:
            # Split the calculation into two threads
            half_n = n // 2
            thread1 = threading.Thread(target=lambda: print(f"Thread 1: {factorial(half_n)}"))
            thread2 = threading.Thread(target=lambda: print(f"Thread 2: {factorial(n - half_n)}"))

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()

            result = factorial(n)
            # Convert the result to a string to extract the first 5 digits
            result_str = str(result)
            first_5_digits = result_str[:5]
            return f"Factorial: {result}, First 5 digits: {first_5_digits}"
    except ValueError:
        return "Invalid input. Please enter a valid number."


if __name__ == "__main__":
    user_input = input("Enter a number to calculate its factorial: ")
    result = calculate_factorial(user_input)
    print(result)
