#This program is a small representation of the famous Fibonacci sequence, a sequence which continues by adding a term n-1 to the current term n, to find the next term, n+1
def get_term_input():
    while True:
        term = int(input("Enter an amount of terms in the Fibonacci sequence: "))
        if term > 0:
            return term
        else:
            term = int(input("Please enter a term of the Fibonacci sequence greater than 0"))

def fibonacci():
    term = get_term_input()
    fib_sequence = [0,1]
    while len(fib_sequence) < term:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print("First", term, "terms of the Fibonacci sequence: ", fib_sequence)

fibonacci()


