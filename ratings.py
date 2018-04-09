import sys


def create_restaurant_ratings(filename=sys.argv[1]):
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


def input_new_restaurant_rating(restaurant_ratings):
    # ask user for new restaurant and rating
    restaurant = raw_input('Enter a new restaurant name: ')
    rating = None

    while rating is None or rating < 1 or rating > 5:
        rating = int(raw_input('Rate the resturant between 1 and 5: '))

    # add new restaurant and rating to restaurant_ratings
    restaurant_ratings[restaurant] = rating
    # print new sorted list of restaurant_ratings
    return restaurant_ratings


def print_restaurant_ratings():
    restaurant_ratings = create_restaurant_ratings()
    restaurant_ratings = input_new_restaurant_rating(restaurant_ratings)
    print_sorted_ratings(restaurant_ratings)


print_restaurant_ratings()
