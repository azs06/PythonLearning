number = 23
running = True

while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('Congratulation, you guessed it')
        running = False
    elif guess < number:
        print('No, it is a bit higher than that')
    else:
        print('No it is a bit lower than that')
else:
    print('Done')
