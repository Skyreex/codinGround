secret = "dreamville"
guess_count = 0
guess_limit = 3
outta_guesses = False
guess = ""
while guess != secret and not(outta_guesses):
    if guess_count < guess_limit:
        guess = input("guess : ")
    else:
        outta_guesses = True
    guess_count += 1
if outta_guesses:
    print("You lose")
else:
    print("You win")