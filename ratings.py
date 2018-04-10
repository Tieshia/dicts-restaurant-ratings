import sys
import random
import os


def create_restaurant_ratings(filename):
    """Restaurant rating lister."""

    restaurant_ratings = {}  # initialize restaurant_ratings dictionary

    with open(filename) as restaurant_file:  # import the file
        for line in restaurant_file:  # for each line:
            line = line.rstrip()  # strip right whitespace
            restaurant, rating = line.split(':')  # split by ':'
            restaurant_ratings[restaurant] = int(rating)  # add list elements to dictionary

    return restaurant_ratings


def print_sorted_ratings(restaurant_ratings):
    # create sorted list of items within restaurant_ratings dictionary
    sorted_ratings = sorted(restaurant_ratings.items())

    print

    # print restaurant and rating statements
    for restaurant, rating in sorted_ratings:
        print "%s is rated at %d." % (restaurant, rating)


def input_restaurant_rating(restaurant_ratings):
    # ask user for new restaurant and rating
    restaurant = raw_input('Enter a restaurant name: ')
    rating = None

    while rating is None or rating < 1 or rating > 5:
        rating = int(raw_input('Rate the restaurant between 1 and 5: '))

    # add new restaurant and rating to restaurant_ratings
    restaurant_ratings[restaurant] = rating
    # print new sorted list of restaurant_ratings
    return restaurant_ratings


def print_restaurant_ratings():
    restaurant_ratings = create_restaurant_ratings()
    restaurant_ratings = input_restaurant_rating(restaurant_ratings)
    print_sorted_ratings(restaurant_ratings)


def update_random_restaurant(restaurant_ratings):
    # random.choice to pick a restaurant
    random_restaurant = random.choice(restaurant_ratings.keys())
    rating = None
    # print choice out to user
    print "Provide an updated rating for {}.".format(random_restaurant)
    # ask user to update rating
    while rating is None or rating < 1 or rating > 5:
        rating = int(raw_input('Rate the restaurant between 1 and 5: '))
    # update rating in dictionary
    restaurant_ratings[random_restaurant] = rating

    return restaurant_ratings


def choose_file():
    print "Welcome to the restaurant rater! What file would you like to open"
    for option, filename in enumerate(os.listdir(".")):
        print option + 1, filename  # print list of files in directory os.listdir("/home/user/src/dicts-restaurant-ratings")
  
    while True:
        file_choice = raw_input('Enter the file name you would like to use: ')  # ask user which file to open

        if os.path.isfile(file_choice):
            return file_choice
        # check if file exits os.path.isfile("/home/user/src/dicts-restaurant-ratings/scores.txt")


restaurant_ratings = create_restaurant_ratings(choose_file())

while True:
    print
    print "\t1. See all the ratings (in alphabetical order)"
    print "\t2. Add/update a restaurant (and rate it)"
    print "\t3. Quit"
    print "\t4. Update the rating for a random restaurant."
    print "\t5. Open a different file."

    user_choice = int(raw_input(">>> "))

    if user_choice == 3:
        break
    if user_choice == 1:
        print_sorted_ratings(restaurant_ratings)
    elif user_choice == 2:
        restaurant_ratings = input_restaurant_rating(restaurant_ratings)
    elif user_choice == 4:
        restaurant_ratings = update_random_restaurant(restaurant_ratings)
    else:
        file_choice = choose_file()
        restaurant_ratings = create_restaurant_ratings(file_choice)

print "Thank you for rating restaurants!"
# sys.exit("Goodbye!")



# give_user_choices()
