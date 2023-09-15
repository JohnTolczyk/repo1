class Restaurant:

    def __init__(self,name,cuisine):
        '''initialize a name, cuisine and attributes.'''
        self.name = name
        self.cuisine = cuisine
        self.guests_served = 0

    def describe_restaurant(self):
        '''Describes the restaurant. '''
        print(f"{self.name} is a restaurant that serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        '''simulates opening the restaurant.'''
        print(f"{self.name} is now open for business.")

    def close_restaurant(self):
        '''simulates closing the restaurant.'''
        print(f"{self.name} is now closed.")

    def set_number_served(self):
        ''' Show the number of guests served'''
        print(f"{self.guests_served} people have been served.")

    def increment_number_served(self,guest):
        '''update the number of guests served'''
        self.guests_served += guest
    


my_restaurant = Restaurant("Gougertini's", "Italian" )

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.close_restaurant()

joes_place = Restaurant("Joe's Place" , "Greasy Spoon")

joes_place.describe_restaurant()

todds = Restaurant("Todd's", "American pub")

todds.describe_restaurant()

restaurant = Restaurant('schmucks', 'american')
restaurant.increment_number_served(22)
restaurant.describe_restaurant()
restaurant.set_number_served()
