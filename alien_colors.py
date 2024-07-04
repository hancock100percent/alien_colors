# 5-3. Alien Colors #1: Imagine an alien was just shot down 
# in a game. Create a variable called alien_color and assign 
# it a value of 'green', 'yellow', or 'red'.

# Turn your if-else chain from Exercise 5-4 into an if-elif-
# else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien

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

# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.


# begin guessing game
def guessing_game():
    print("Welcome to the Guessing Game!")
    print("Guess the color of the alien and win points")

    # Generate a green number between 1 and 100
    five_points = ('green')
    ten_points = ('yellow')
    fifteen_points = ('red')

    green = 10
    yellow = 10
    red = 15

    attempts = 0

    while True:
        guess = (input("Enter your guess (hint: it's a color): "))
        attempts += 1

        if guess == 'green':
            print("player earned 5 points.:")
        elif guess == 'yellow':
            print("player earned 10 points.:")
        elif guess == 'red':
            print("player earned 5 points.:")
        else:
            print("Not the correct color of the alien")
            print(f"You entered {attempts} attempts!")

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
