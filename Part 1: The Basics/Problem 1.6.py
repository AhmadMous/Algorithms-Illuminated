powers_of_2 = [2 ** i for i in range(8)]

# Finds next power of 2
def next_2s_power(r):
    if r in powers_of_2:
        return r

    for power in powers_of_2:
        if r < power:
            return power
    

# Calculates the number of digits of a number
def digit_len(number):
    counter = 1
    while (number // 10) != 0:
        number = number // 10
        counter += 1
    return counter


# Prepares numbers by splitting them into proper forms
def prep_numbers(number1, number2, number1_len, number2_len):

    # Allows us to treat the numbers as if their length is 2 ** k
    n = max(number1_len, number2_len)
    n = next_2s_power(n)

    # Splits the numbers according to half the length which is 2 ** k
    splitter = (n + 1) // 2
    split_numbers = tuple()

    # Splits each number into 2 halves then concatanates them to tuple which we will return
    for number in number1, number2:
        split_numbers += (number // (10 ** splitter), number % (10 ** splitter))

    split_numbers += (n,)
    return split_numbers


# Find product of a number using the Karatsuba recursive multiplication algorithm
def Karatsuba_mult(num1, num2):

    # Get the number of digits of each input number
    num1_len, num2_len  = digit_len(num1), digit_len(num2)

    # Base case where we are multiplying single digits
    if num1_len == 1 and num2_len == 1:
        return num2 * num1

    # Extract the parts and the "length" of the number in proper form
    a, b, c, d, n = prep_numbers(num1, num2, num1_len, num2_len)

    p = a + b
    q = c + d

    # Recursively calculate ac, bd, and pq
    ac = Karatsuba_mult(a, c)
    bd = Karatsuba_mult(b, d)
    pq = Karatsuba_mult(p, q)

    adbc = pq - ac - bd

    return (10 ** n) * ac  + (10 ** (n // 2)) * adbc + bd

number_1 = 3141592653589793238462643383279502884197169399375105820974944592
number_2 = 2718281828459045235360287471352662497757247093699959574966967627
print(Karatsuba_mult(number_1, number_2))

print(Karatsuba_mult(20220, 1))