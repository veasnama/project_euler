# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Solution

def Fibonacci(num):
    
    if num > 2 :
        return Fibonacci(num - 1) + Fibonacci(num - 2)
    else:
        return num;


def compute_sum(number_of_range):
    if number_of_range <= 0:
        print("Number must be positive") 

    else:
        fab_even_sum = 0
        for n in range(1,number_of_range):
            fib_num = Fibonacci(n)
            print(fib_num)
            if fib_num < 4000000:
                if fib_num % 2 == 0:
                    fab_even_sum += fib_num
                else:
                    print("Not even number") 
            else:
                print("Condition is unmet")
                break; 
        print(f"The result = {fab_even_sum}")
compute_sum(10)
