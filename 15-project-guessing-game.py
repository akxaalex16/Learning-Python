secret_number = 16
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_guess = int(input("Guess:"))
    guess_count += 1
    
    if user_guess == secret_number:
        print(f"Yes! {secret_number} is the correct number")
        break
else: 
    print("Sorry, you lost")
        