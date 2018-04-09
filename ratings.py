import sys


def print_sorted_ratings(filename=sys.argv[1]):
    """Restaurant rating lister."""

    restaurant_ratings = {}  # initialize restaurant_ratings dictionary

    with open(filename) as restaurant_file: # import the file
        for line in restaurant_file: # for each line:
            line = line.rstrip()  # strip right whitespace
            restaurant, rating = line.split(':')  # split by ':'
            restaurant_ratings[restaurant] = rating  # add list elements to dictionary

    # create sorted list of items within restaurant_ratings dictionary
    sorted_ratings = sorted(restaurant_ratings.items())
    # print restaurant and rating statements
    for record in sorted_ratings:
        restaurant, rating = record
        print "%s is rated at %d." % (restaurant, int(rating))


print_sorted_ratings()
