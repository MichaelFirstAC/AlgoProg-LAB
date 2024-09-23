'''RAAAAAHHHH'''

# Factorial Calc
# Hey chat, in case you just joined. Calc stands for calculator
def factorial_user_input():
    try:
        # Taking thingymajig
        n = int(input("Factorial calc. Enter your thingymajig: "))
        
        # function
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        
        # Display the resultsss
        print(f"The factorial of {n} is {factorial(n)}. Stupid.")
    
    except ValueError:
        print("Bruh. Enter a valid integer. Idiot.")

# Calling it
factorial_user_input()
