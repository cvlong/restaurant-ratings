def find_restaurant_ratings(file_name):
    """Prints restaurant name and rating"""


    with open(file_name) as text:
        
        restaurant_ratings = {}

        for line in text:
            line = line.rstrip()
            line = line.split(":")
            
            restaurant_ratings[line[0]] = line[1]


        for restaurant, rating in restaurant_ratings.items():
            print "{} is rated at {}.".format(restaurant,
                                              rating,
                                              )

find_restaurant_ratings("scores.txt")