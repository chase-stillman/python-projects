#finding positive integer, ensuring that there is no input of 0
def get_pos_int():
    while True:
        num = int(input("How many words would you like to enter?"))
        if num > 0:
            return num
        else:
            print("Please enter an integer greater than 0")
#function to call the positive integer
def main():
    list = []
    num = get_pos_int()
#using the positive integer in a range function
    for i in range(num):
        word = input("Enter a word:")
        list.append(word)
#assigning shortest and longest words to use in conditionals
    shortest = list[0]
    longest = list[0]
    total_len = 0
#using conditionals in a loop to find the shortest and longest words
    for i in list:
        if len(i) < len(shortest):
            shortest = i
        elif len(i) > len(longest):
            longest = i
        total_len += len(i)
#printing the outputs
    print("Shortest:", shortest)
    print("Longest:", longest)
    print("Average (arithmetic mean) length of words:", (total_len/len(list)))
#calling the main function
if __name__ == "__main__":
    main()



