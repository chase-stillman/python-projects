#this program is a very difficult game in which two numbers are randomly generated using the random library in Python, then their product and sum is found. the program will tell the user the product, which must be then used to determine the sum of the two numbers. the range of numbers is currently set to 128 each, but can of course be lowered to make the game a little more achievable, while still challenging.
import random
#function to find random numbers and their sum and product
def find_random_nums():
    num1 = random.randrange(1,128)
    num2 = random.randrange(1,128)
    numsadded = num1 + num2
    nums_product = num1 * num2
    return num1, num2, numsadded, nums_product

#finding user input, counting their amount of attempts using a while loop and conditionals
def user_input(numsadded, num1, num2):
    count = 0
    max_attempts = 8
    while count < max_attempts:
        guess = int(input("Enter guess: "))
        count += 1
        if guess > numsadded:
            print("go lower")
        elif guess < numsadded:
            print("go higher")
        else:
            print("correct!")
            print("You guessed the sum in", str(count) ,"guesses.")
            guess_the_nums(num1, num2)
            return
    print("Max attempts reached. The correct sum was", str(numsadded))

def guess_the_nums(num1,num2):
    num1_guess = int(input("Enter the first number: "))
    num2_guess = int(input("Enter the second number: "))

    if (num1_guess == num1 or num1_guess) == num2 and (num2_guess == num2 or num2_guess == num1):
        print("You win!")
    else:
        print("You lose. :(")
        print("The numbers are", str(num1), "and", str(num2))
def main():
    num1, num2, numsadded, nums_product = find_random_nums()
    print("Algebra Guessing Game - Find 2 numbers.")
    print("The product of the two numbers is", str(nums_product))
    print("Guess the sum of the numbers.")
    user_input(numsadded, num1, num2)

if __name__ == "__main__":
    main()
