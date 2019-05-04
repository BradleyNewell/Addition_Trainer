import random

# Title stating options available to the user.

print('Enter "help" to get the answer\nEnter "end" when you are finished.')
running = True


# Function that will check the user input for keywords, if no keywords are found, it will then check the users input


def answer_check():
    if user_input == 'help':
        print(answer)

    # Else if statement which checks to see if the user has entered the keyword to stop the loop.

    elif user_input == 'end':
        global running
        running = False

    # Converts the user input to an integer

    else:
        user_int = int(user_input)
        if user_int == answer:
            print('Correct!')
        elif user_int != answer:
            print('Wrong, Try again')


while running:
    # Using the random python library the following lines generate two random numbers with a range of 1-100.

    nums1 = random.randrange(1, 100)
    nums2 = random.randrange(1, 100)

    # Calculates and stores the answer of the two random numbers generated above and is accessed by the answer_check()
    # function.

    answer = nums1 + nums2

    # Displays the two numbers the user must calculate and enter in to the command prompt.

    print('Add: %s + %s' % (nums1, nums2))

    # Collects the user input

    user_input = (input('= '))

    # Function call

    answer_check()
