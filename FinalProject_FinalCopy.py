# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:         Jackson Murphy, Jenna Leonard, Hayden Moore, Aswin Nair
# Section:      481
# Assignment:   Team Project -  Part 2
# Date:         24 November 2020

# imports necessary modules to use in functions
import csv
from numpy import random
from math import sqrt

# ---------- Function Definitions ----------


def awarded_candies(active_user):
    """ Random choice between 1, 3, 5, 10 to determine number of candies. -Aswin Nair"""

    candy_nums = [1, 3, 5, 10]  # Possible number of candies that can be awarded

    # Opens current user's file for reading, used to get the lines
    datFile = open(active_user + '.csv', 'r', newline='')
    sheet_reader = csv.reader(datFile, delimiter=',')

    file_lines = []

    for lines in sheet_reader:
        file_lines.append(lines)
    datFile.close()

    # The awarded candies row is modified appropriately
    awarded_candies = random.choice(candy_nums)
    file_lines[4][1] = str(awarded_candies + int(file_lines[4][1]))

    # Opens current user's file for writing, used to add modified lines back to file
    datFile = open(active_user + '.csv', 'w', newline='')
    sheet_writer = csv.writer(datFile, delimiter=',')

    for line in file_lines:
        sheet_writer.writerow(line)
    datFile.close()

    print('You have been awarded', awarded_candies, 'candies!')


def mini_game():
    """ Mini game (guess 2 numbers between certain range, 2 random correct answers) to determine if user catches a
    pokemon; if successful, award candies. -Aswin Nair"""
    # returns True or False depending on whether user wins mini-game

    print("To catch a pokemon, you have to guess one of two random numbers in the given range.\nYou will have three "
          "attempts, and you get two guesses per attempt.\nEach attempt gets progressively harder as the two numbers "
          "will change for each attempt,\nand the range will increase each time as a penalty for failing the "
          "previous attempt.\n")

    #  2 random numbers between 1 and 10
    random_num_one = random.randint(1, 10)
    random_num_two = random.randint(1, 10)
    guess_counter = 1

    # user gets TWO guess attempts per try (i.e. 2 guesses for 1-10, 2 guesses for 1-15, etc.)
    # user's first guess attempt
    attempt_one_guess = int(input('This is attempt one: Guess a number between 1 and 10. What is guess '
                                  + str(guess_counter) + '? \n'))

    # if user's guess is equal to either of the the two random numbers
    if attempt_one_guess == random_num_one or attempt_one_guess == random_num_two:
        print('You have guessed right!')
        return True

    # if first guess is wrong, user gets one more guess until game gets harder (i.e. number range increases)
    else:
        print('Incorrect guess. You have one more guess until the game gets harder.\n')
        guess_counter += 1
        attempt_one_guess = int(input('This is attempt one: Guess a number between 1 and 10. What is guess '
                                      + str(guess_counter) + '? \n'))

        if attempt_one_guess == random_num_one or attempt_one_guess == random_num_two:
            print('You have guessed right!')
            return True
        else:
            print('Incorrect guess. You are now on attempt two.\n')

    # game gets harder since user lost first round
    # 2 random numbers between 1 and 15
    random_num_one = random.randint(1, 15)
    random_num_two = random.randint(1, 15)
    guess_counter = 1

    attempt_two_guess = int(input('This is attempt two: Guess a number between 1 and 15. What is guess '
                                  + str(guess_counter) + '? \n'))
    if attempt_two_guess == random_num_one or attempt_two_guess == random_num_two:
        print('You have guessed right!')
        return True
    else:
        print('Incorrect guess. You have one more guess until the game gets harder.\n')
        guess_counter += 1
        attempt_two_guess = int(input('This is attempt two: Guess a number between 1 and 15. What is guess '
                                      + str(guess_counter) + '? \n'))

        if attempt_two_guess == random_num_one or attempt_two_guess == random_num_two:
            print('You have guessed right!')
            return True
        else:
            print('Incorrect guess. You are now on attempt three.\n')

    random_num_one = random.randint(1, 20)
    random_num_two = random.randint(1, 20)
    guess_counter = 1

    attempt_three_guess = int(input('This is attempt three: Guess a number between 1 and 20. What is guess '
                                    + str(guess_counter) + '? \n'))
    if attempt_three_guess == random_num_one or attempt_three_guess == random_num_two:
        print('You have guessed right!')
        return True
    else:
        print('Incorrect guess. You have one more guess until the game gets harder.\n')
        guess_counter += 1
        attempt_three_guess = int(input('This is attempt three: Guess a number between 1 and 20. What is guess '
                                        + str(guess_counter) + '? \n'))

        if attempt_three_guess == random_num_one or attempt_three_guess == random_num_two:
            print('You have guessed right!')
            return True

        else:
            print('Incorrect guess. You are out of attempts. No Pokemon were caught.\n')
            return False


def leveling(active_name):
    """ Allows user to level up Pokemon using candy and current level, increasing CP appropriately. -Jenna Leonard"""

    # open the user file
    user_file = open(str(active_name) + '.csv', 'r')
    sheet_reader = csv.reader(user_file, delimiter=',')
    file_lines = []

    # create a loop to read the number of candies, cp, and current level
    for lines in sheet_reader:
        file_lines.append(lines)
    user_file.close()

    # find variable values
    level = int(file_lines[3][1])  # assuming 1 is the current pokemon
    cp = int(file_lines[2][1])
    candies_num = int(file_lines[4][1])
    current_poke = file_lines[1][1]

    # read from the poke list
    data = open('PokeList.csv', 'r', newline='')
    data_read = csv.reader(data, delimiter=',')

    # read from the csv file find the max CP
    num = 0
    max_CP = 0
    for val in data_read:
        if current_poke != val[1]:
            num += 1
        elif current_poke == val[1]:
            max_CP = val[3]

    # close the pokemon file
    data.close()

    # calculate the leveling for specific levels
    if level < 30 and candies_num >= 1:
        cp = cp + round((cp * .0094) / (.095 * sqrt(level)))     # CP calculation for a Pokemon with level 1 - 29
        level += 1
        candies_num -= 1
        # do not let the CP reach above maximum
        if cp > int(max_CP):
            cp = int(max_CP)

    elif level >= 30 and candies_num >= 2:
        cp = cp + round((cp * .0045) / (.095 * sqrt(level)))     # CP calculation for a Pokemon with level 30 or higher
        level += 1
        candies_num -= 2
        # do not let the CP reach above maximum
        if cp > int(max_CP):
            cp = int(max_CP)

    # print to let user know they cannot level up again
    if level < 30 and candies_num == 0:
        print('You do not have enough candies to level up again.')
    elif level >= 30 and candies_num == 1:
        print('\n\nYou do not have enough candies to level up again.')

    # replace the old candies num, cp numbs, and level num with the new calculated ones
    file_lines[3][1] = str(level)
    file_lines[2][1] = str(cp)
    file_lines[4][1] = str(candies_num)

    # rewrite the file with the new information
    write = open(str(active_name) + '.csv', 'w', newline='')
    sheet_writer = csv.writer(write, delimiter=',')
    for line in file_lines:
        sheet_writer.writerow(line)
    write.close()


def quit():
    """ Allows user to quit at various points in the game. -Jenna Leonard"""

    ask_user = input('Would you like to quit playing (yes or no)?: ')

    # return False when user selects option to quit
    if ask_user.lower() == 'yes':
        return False
    elif ask_user.lower() == 'no':
        return True


def account_switch():
    """ Gives user option to switch accounts. -Hayden Moore"""

    print()
    print('--------------------------------------       ACCOUNT SWITCH       ---------------------------------------')

    # user must type in what account they want to play as
    switched_account = str(input('Type the username for the account you wish to switch to: '))
    print()

    return switched_account


def pokemon_selection_menu(active_user):
    """ Allows user to view active Pokemon and change to another one. -Collaboration"""

    # open file to read
    user_file = open(str(active_user) + '.csv', 'r')
    sheet_reader = csv.reader(user_file, delimiter=',')
    # --------------------------------------------------------------
    file_lines = []

    for lines in sheet_reader:  # create a loop to read the number of candies, cp, and current level
        file_lines.append(lines)

    # close file
    user_file.close()

    # find variable values
    current_pokemon_name = file_lines[1][1]
    level_of_pokemon = file_lines[3][1]  # assuming 1 is the current pokemon
    cp_number = file_lines[2][1]
    num_candies = file_lines[4][1]

    # ----------------- Creates Pokemon Selection Menu ------------------
    print('---------------------------------------  POKEMON SELECTION MENU  ------------------------------------------')
    print(current_pokemon_name)
    print()
    print('Current CP: '.ljust(15), round(int(cp_number)))
    print('Current Level: '.ljust(10), level_of_pokemon)
    print('Candies: '.ljust(15), num_candies)
    print()
    print('-----------------------------------------------------------------------------------------------------------')
    # -------------------------------------------------------------------

    # determines the number of Pokemon a user has
    num_pokemon = len(file_lines[1]) - 1

    # if user has 4 or less pokemon
    if num_pokemon <= 4:
        for i in range(1, num_pokemon + 1):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")       # prints # and pokemon name
        for k in range(1, num_pokemon + 1):
            if k == 1:
                print()
                print('  ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")   # prints CP
            else:
                print('  ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")

        print()

    # if user has between 5 and 8 pokemon
    if 5 <= num_pokemon <= 8:
        for i in range(1, 5):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(1, 5):
            if k == 1:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
        print()
        print()

        for i in range(5, num_pokemon + 1):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(5, num_pokemon + 1):
            if k == 5:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")

        print()

    # if user has between 9 and 12 pokemon
    if 9 <= num_pokemon <= 12:
        for i in range(1, 5):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(1, 5):
            if k == 1:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
        print()
        print()

        for i in range(5, 9):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(5, 9):
            if k == 5:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
        print()
        print()

        for i in range(9, num_pokemon + 1):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(9, num_pokemon + 1):
            if k == 9:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")

        print()

    # if user has more than 12 pokemon
    if num_pokemon > 12:
        for i in range(1, 5):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(1, 5):
            if k == 1:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
        print()
        print()

        for i in range(5, 9):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(5, 9):
            if k == 5:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
        print()
        print()

        for i in range(9, 13):
            print(str(i) + '. ' + str(file_lines[1][i]).rjust(3), end="        ")
        for k in range(9, 13):
            if k == 9:
                print()
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")
            else:
                print('   ' + 'CP: ' + str(file_lines[2][k]).rjust(3), end="        ")

        print()

    # user must select a new pokemon from the list of their pokemon
    new_pokemon = int(input('Please choose a new Pokemon from the selection menu (1 - 12): '))

    # while loop accounts for incorrect user input (i.e. numbers not between 1 and 12)
    while (new_pokemon > 12) or (new_pokemon < 1):
        print('Please enter a valid selection (1 - 12).')
        new_pokemon = int(input('Please choose a new Pokemon from the selection menu (1 - 12): '))


def battling(active_user):
    """ Enables two users to battle, winner receives random # of candies. -Aswin Nair"""

    # open file
    user_file = open(str(active_user) + '.csv', 'r')
    sheet_reader = csv.reader(user_file, delimiter=',')
    file_lines = []

    for lines in sheet_reader:  # create a loop to read the number of candies, cp, and current level
        file_lines.append(lines)

    # close file
    user_file.close()

    # user 1's Pokemon name and CP retrieved from file
    users_pokemon_name = file_lines[1][1]
    cp1_number = file_lines[2][1]

    # user 1's HP (health) calculated using a specific formula
    poke1hp = (1.5 * int(cp1_number)) - 30
    # -------------------------------------------------------
    # user must type in who their opponent (user 2) is
    opponent_name = input('Enter the name of your opponent: ')

    user_file = open(str(user2) + '.csv', 'r')
    sheet_reader = csv.reader(user_file, delimiter=',')
    file_lines = []

    for lines in sheet_reader:  # create a loop to read the number of candies, cp, and current level
        file_lines.append(lines)
    user_file.close()

    opponent_poke_name = file_lines[1][1]
    cp2_number = file_lines[2][1]
    poke2hp = (1.5 * int(cp2_number)) - 30
    # -------------------------------------------------------

    # while loop runs until one of the Pokemon from either user has a health less than 0
    # water beats fire; grass beats water; fire beats grass
    while (poke1hp > 0) and (poke2hp > 0):

        print('User 1\'s Pokemon HP =', poke1hp)
        print('User 2\'s Pokemon HP =', poke2hp)
        print()

        # both users have the option to choose which move they want
        user1_choice = input('User 1, Enter your choice of move (Fire, Water, Grass): ')
        user2_choice = input('User 2, Enter your choice of move (Fire, Water, Grass): ')
        print()

        if user1_choice.lower() == 'fire' and user2_choice.lower() == 'grass':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 1\'s move is super effective on User 2\'s. User 1 does more damage!')

            # pokemon's health lowered depending on user's move
            poke1hp -= 10
            poke2hp -= 40

        elif user1_choice.lower() == 'fire' and user2_choice.lower() == 'water':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 2\'s move is super effective on User 1\'s. User 2 does more damage!')

            poke1hp -= 40
            poke2hp -= 10

        elif user1_choice.lower() == 'fire' and user2_choice.lower() == 'fire':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 1 and 2\'s moves are the same. Equal damage done!')

            # pokemon's health decrease by same amount since same battle move was chosen
            poke1hp -= 20
            poke2hp -= 20

        elif user1_choice.lower() == 'grass' and user2_choice.lower() == 'water':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 1\'s move is super effective on User 2\'s. User 1 does more damage!')

            poke1hp -= 10
            poke2hp -= 40

        elif user1_choice.lower() == 'grass' and user2_choice.lower() == 'fire':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 2\'s move is super effective on User 1\'s. User 2 does more damage!')

            poke1hp -= 40
            poke2hp -= 10

        elif user1_choice.lower() == 'grass' and user2_choice.lower() == 'grass':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 1 and 2\'s moves are the same. Equal damage done!')

            poke1hp -= 20
            poke2hp -= 20

        elif user1_choice.lower() == 'water' and user2_choice.lower() == 'fire':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 1\'s move is super effective on User 2\'s. User 1 does more damage!')

            poke1hp -= 10
            poke2hp -= 40

        elif user1_choice.lower() == 'water' and user2_choice.lower() == 'grass':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 2\'s move is super effective on User 1\'s. User 2 does more damage!')

            poke1hp -= 40
            poke2hp -= 10

        elif user1_choice.lower() == 'water' and user2_choice.lower() == 'water':
            print('User 1 has chosen', user1_choice)
            print('User 2 has chosen', user2_choice)
            print('User 1 and 2\'s moves are the same. Equal damage done!')

            poke1hp -= 20
            poke2hp -= 20

    # if either of the Pokemon have a health (HP) greater than 0 after the loop, they win a random # of candies
    if poke1hp > 0:
        print(active_user, ' and ', users_pokemon_name, ' has won the battle!', sep='')
        awarded_candies(active_user)
    elif poke2hp > 0:
        print(opponent_name, ' and ', opponent_poke_name, ' has won the battle!', sep='')
        awarded_candies(opponent_name)


def catch_pokemon(active_user):
    """ Opens file and makes user play mini game. If the user wins, as in they caught a Pokemon,
    then candies are awarded and caught Pokemon is appended to user's file. -Aswin Nair"""

    if mini_game():

        # call awarded_candies
        awarded_candies(active_user)

        random_pokemon = []

        # random number to determine which Pokemon user caught
        pokemon_num = random.randint(0, 150)

        # open list of Pokemon
        pokeFile = open('PokeList.csv', 'r', newline='')
        sheet_reader = csv.reader(pokeFile, delimiter=',')

        for index, lines in enumerate(sheet_reader):

            # if the index of said pokemon = the random number, user gets that pokemon
            if index == pokemon_num:
                random_pokemon.append(lines[1])
                random_pokemon.append(lines[2])

        # close file
        pokeFile.close()

        print('The pokemon you have caught is ' + random_pokemon[0] + '!\n')

        readFile = open(active_user+'.csv', 'r', newline='')
        sheet_reader = csv.reader(readFile, delimiter=',')
        file_lines = []

        for lines in sheet_reader:
            file_lines.append(lines)
        readFile.close()

        file_lines[1].append(random_pokemon[0])
        file_lines[2].append(random_pokemon[1])

        # add new Pokemon to user's file
        writeFile = open(active_user + '.csv', 'w', newline='')
        sheet_writer = csv.writer(writeFile, delimiter=',')

        for line in file_lines:
            sheet_writer.writerow(line)
        writeFile.close()


def current_pokemon(active_user):
    """ Fn allows user to view current Pokemon and its characteristics (i.e. CP, level, etc).
    User also has option to level up. -Jenna Leonard"""

    # read in current_poke, current_level, CP, and candies from the file
    # use a while loop? so they can keep picking levels if want to

    user_choice = 0
    while user_choice != 2:
        user_file = open(str(active_user) + '.csv', 'r')
        sheet_reader = csv.reader(user_file, delimiter=',')
        # --------------------------------------------------------------
        file_lines = []

        for lines in sheet_reader:  # create a loop to read the number of candies, cp, and current level
            file_lines.append(lines)
        user_file.close()

        # find variable values
        current_poke = file_lines[1][1]
        level = file_lines[3][1]  # assuming 1 is the current pokemon
        CP = file_lines[2][1]
        candies = file_lines[4][1]

        print('\n--------------------------------------    CURRENT POKEMON    --------------------------------------')
        print('Current Pokemon:', current_poke, '\n')
        print('Current CP:', CP)
        print('Current Level:', level)
        print('Candies:', candies)
        print('\n1 - Level Up (uses candies).')
        print('2 - Exit to the Main Menu.')

        # try-except statement accounts for Value Error (i.e. if integer is typed instead of 1 or 2)
        user_choice = 0
        while user_choice == 0:
            try:
                user_choice = int(input('\nWhich option would you like to choose? (1 or 2): '))
                if user_choice == 1:
                    # call leveling
                    leveling(active_user)
            except ValueError:
                print("Invalid option, choose a number that is either 1 or 2.")


def main_menu():
    """ Prints out descriptive menu and allows user to select an option (battle, catch, view, etc.). -Jackson Murphy"""

    # -------- Creates Main Menu --------
    print('------------------- Pokemon! Gotta Catch \'Em All! -------------------')
    print('Main Menu'.rjust(38))
    print('1: View Current Pokemon Character.')
    print('2: Catch a New Pokemon!')
    print('3: Go Battling!')
    print('4: Select a New Pokemon.')
    print('5: Switch Accounts.')
    print('6: Create a New Player Account.')
    print('7: Quit')
    print('----------------------------------------------------------------------')
    # -----------------------------------

    user_selection = None

    # while loop runs until user gives necessary input to continue
    while user_selection not in {1, 2, 3, 4, 5, 6, 7}:

        # try-except statement will catch a ValueError if the user inputs something
        # that cannot be processed as an integer
        try:
            user_selection = int(input('Please enter a numerical selection (1 - 7) from the options above: '))
        except ValueError:
            print('ONLY type an integer from 1 to 7!')

    # returns user's selection from the main menu
    return user_selection


def pokemon_assignment():
    """ Assigns players a Pokemon randomly or give them an option of a low-level one. -Hayden Moore"""

    # open list of Pokemon
    with open('PokeList.csv', 'r') as pokeFile:
        low_level_pokes = []
        poke_reader = csv.reader(pokeFile)

        # for loop runs through every pokemon in list
        for i in poke_reader:
            if i[0] != 'Index' and int(i[2]) < 100:        # if the index is a Pokemon and the min CP is less than 100
                low_level_pokes.append(i)
    assigned_poke = low_level_pokes[random.randint(0, len(low_level_pokes)) - 1]

    # new users get assigned a low-level Pokemon with CP less than 100
    return assigned_poke


def player_creation():
    """ Fn that creates new user and their new Pokemon file. -Hayden Moore"""

    print('--------------------------------------        PLAYER CREATION        --------------------------------------')

    # asks user to entire a unique username
    user_name = str(input('Enter a username: '))

    # pokemon_assignment() called to give new username a low-level pokemon
    user_first_poke = pokemon_assignment()

    print('You have been assigned the pokemon:', user_first_poke[1])
    user_info = user_first_poke + [user_name]

    # open user's file (username.csv, where username is what they type in)
    with open(user_name + '.csv', 'w', newline='') as userFile:

        # writes into user's file giving 10 candies, a starting level of 1 and a random CP between the max and min of
        # their low level Pokemon
        csv_writer = csv.writer(userFile, delimiter=',')
        first_line = [user_name]
        second_line = ['Pokemon name', user_info[1]]
        third_line = ['CP', str(random.randint(int(user_info[2]), int(user_info[3])))]
        fourth_line = ['Level', '1']
        fifth_line = ['Number of candies', '10']
        csv_writer.writerow(first_line)
        csv_writer.writerow(second_line)
        csv_writer.writerow(third_line)
        csv_writer.writerow(fourth_line)
        csv_writer.writerow(fifth_line)

    # returns the first part of their file (no .csv)
    return user_name


# ------------------------------------------

# -------------- Main Program --------------

# Have user create player profile
# Call player_creation()
user1 = player_creation()

# Call pokemon_assignment() inside player_creation() to assign pokemon to player
# Repeat once to create a second player
user2 = player_creation()

current_user = user1

go_again = True

# While loop repeats until (go_again == False)
while go_again:

    print()
    print('The current active user is', current_user)

    # Generate main menu by calling function main_menu()
    # Ask user for a numerical selection (1 - 7)
    user_menu_num = main_menu()

    # Depending on user’s input, call the respective function:
    # If 1, call current_pokemon() to display relevant info on pokemon (CP, # of candies, etc.)
    if user_menu_num == 1:
        current_pokemon(current_user)

    # If 2, call catch_pokemon() to catch a random pokemon
    elif user_menu_num == 2:
        catch_pokemon(current_user)

    # If 3, call battling() to battle between two pokemon and award candies
    elif user_menu_num == 3:
        battling(current_user)

    # If 4, call pokemon_selection_menu() to change pokemon
    elif user_menu_num == 4:
        pokemon_selection_menu(current_user)

    # If 5, call account_switch() to change account
    elif user_menu_num == 5:
        switched_user_name = account_switch()
        current_user = switched_user_name

    # If 6, call player_creation() to create a new account
    elif user_menu_num == 6:
        player_creation()

    # If 7, call quit() to end program
    elif user_menu_num == 7:
        go_again = quit()

# ------------------------------------------

# signed Jackson Murphy, Jenna Leonard, Hayden Moore, Aswin Nair
