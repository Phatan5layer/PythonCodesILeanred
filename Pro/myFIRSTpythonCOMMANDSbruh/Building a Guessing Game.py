secret_word = "Lion"
guess = ""
guess_count = 0  # guessing tries starts at 0
guess_limit = 3  # Total guesses
out_of_guess = False  #If the user has not run out of guesses , they will keep playing

while guess != secret_word and not(out_of_guess): # Keep looping as long as the "users *guess* is not equal*(!=)* tp the *secret_word*"
      if guess_count < guess_limit:
            guess = input("enter guess; ")  # Asking user to enter the secret_word
            guess_count += 1
      # it's to increment/add the guess count
      else:
            out_of_guess = True # it's to increment/add the guess count


if out_of_guess:
      print("U LOSE , DIE")
else:
       print("You win king")




