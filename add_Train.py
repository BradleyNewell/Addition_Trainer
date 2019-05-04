import random


print('Enter "help" to get the answer\nEnter "end" when you are finished.')
running = True


def answer_check():
    if user_input == 'help':
        print(answer)
    elif user_input == 'end':
        global running
        running = False

    else:
        user_int = int(user_input)

        if user_int == answer:
            print('Correct!')
        elif user_int != answer:
            print('Wrong, Try again')


while running:
    nums1 = random.randrange(1, 100)
    nums2 = random.randrange(1, 100)

    answer = nums1 + nums2

    print('Add: %s + %s' % (nums1, nums2))

    user_input = (input('= '))

    answer_check()
