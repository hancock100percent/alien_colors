# 5-3. Alien Colors #1: Imagine an alien was just shot down 
# in a game. Create a variable called alien_color and assign 
# it a value of 'green', 'yellow', or 'red'.

# alien_colors = ('green')

# Write an if statement to test whether the alien’s color is green. 
# If it is, print a message that the player just earned 5 points
# # Using a for loop to print the statement five times
# # print(f"\n\tSPACE HOLDER")     """"""
# print(f"\n\tSPACE HOLDER") 
# # print(f"\n\tSPACE HOLDER")     """"""
# print(f"\n\tSPACE HOLDER") 


def convert_to_phonetic(word):
    letters_to_words = {
        'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
        'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
        'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
        'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
        'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray',
        'y': 'Yankee', 'z': 'Zulu',
    }

for _ in range(5):
    print(f"\n\tSPACE HOLDER")

# print simple image
def create_simple_image():
    # Define the dimensions of the image grid
    width = 5
    height = 5
    
    # Create an empty grid represented by a list of dictionaries
    image = []
    for _ in range(height):
        row = {'.'}, width  # Initialize each row with dots
        image.append(row)
    
    # Print the image
    for row in image:
        print(' ', row)

# Call the function to create and display the image
create_simple_image()



# alien_colors = ['green']

# if alien_colors == green:
#     print('player just earned 5 points')

# begin guessing game
def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess what it is?")

    # Generate a green number between 1 and 100
    alien_colors = ('green')
    attempts = 0

    while True:
        guess = (input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess == alien_colors:
            print(f"Congratulations! You've guessed the number {alien_colors} correctly in {attempts} attempts!")
        elif guess != alien_colors:
            print("NOPE! Try again.")
        else:
            print("unexpected input")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

# Start the game
guessing_game()



# # alien_colors = ['mushrooms', 'extra cheese']
# if 'mushrooms' in alien_colors:
#     print("Adding mushrooms.")
# elif 'pepperoni' in alien_colors:
#     print("Adding pepperoni.")
# elif 'extra cheese' in alien_colors:
#     print("Adding extra cheese.")
#     print("\nFinished making your pizza!")