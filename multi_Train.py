import random


print('Enter "help" to get the answer\nEnter "end" when you are finished.')
running = True


def answer_check(user_answer):
    if user_answer == 'help':
        print(answer)
    elif user_answer == 'end':
        global running
        running = False
    else:
        try:
            user_int = int(user_input)
            if user_int == answer:
                print('Correct!')
            elif user_int != answer:
                print('Wrong, Try again')
        # Exception for Value Error
        except ValueError:
            print('Please enter a valid number or command.')
            pass


while running:
    nums1 = random.randrange(1, 10)
    nums2 = random.randrange(1, 10)

    answer = nums1 * nums2

    print('Multiply: %s x %s' % (nums1, nums2))

    user_input = (input('= '))

    answer_check(user_input)
