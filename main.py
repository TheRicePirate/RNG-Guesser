import time
from random import randrange
start = 'y'
while start != 'n':
    start_range = int(input("Input starting range integer: "))
    print("")
    end_range = int(input("Input end range integer: "))
    print("")
    print("Enter an integer in the range " + str(start_range) + " - " + str(end_range))
    secret_value = int(input("> "))
    print("")

    while secret_value > end_range or secret_value < start_range:
        print("Please input a secret value within the given range.")
        print("")
        print("Current range: " + str(start_range) + ", " + str(end_range))
        print("")
        reset_question = str(input("Would you like to change the range? (y/n): "))
        if reset_question == 'y':
            start_range = int(input("Input starting range integer: "))
            end_range = int(input("Input end range integer: "))
            secret_value = int(input("Enter a number from 1 to 100000: "))
            break
        else:
            print("")
            secret_value = int(input("Enter a number from 1 to 100000: "))
            if secret_value > end_range or secret_value < start_range:
                break

    time_start = time.time()
    number_chosen = randrange(start_range, end_range)
    print(number_chosen)
    tries = 1

    while number_chosen != secret_value:
        number_chosen = randrange(start_range, end_range)
        print(number_chosen)
        tries += 1
    else:
        time_end = time.time()
        runtime = time_end - time_start
        print("The number is " + str(secret_value) + " .")
        print(
            "The script guessed the secret value " + str(tries) + " times to obtain it within a span of approximately "
            + str(runtime) + " seconds.")

    print("Would you like to restart? (y/n)")
    start = str(input("> "))
    if start == 'n':
        break
