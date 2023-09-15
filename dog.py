class Dog:
    """a simple attempt to model a dog"""

    def __init__(self,name,age):
        """initialize age and attributes"""
        self.name = name
        self.age = age

    def sit(self):
        '''simulate the dog sitting in response to a command'''
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        '''simulate the dog rolling over in response to a command.'''
        print(f"{self.name} has now rolled over.") 

    def give_paw(self):
        '''simulate the dog shaking your hand with his right paw in response to a command.'''
        print(f"{self.name} has given you his paw.")

    def other_paw(self):
        '''simulate the dog giving you his left paw in response to a command.'''
        print(f"{self.name} has given you his other paw.")

    def speak(self):
        '''simulate the dog barking in response to a command.'''
        print(f"{self.name} is barking.")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
my_dog.give_paw()
my_dog.other_paw()

annas_dog = Dog('pop pop', 1)

print (f"Anna's dog is named {annas_dog.name}")
print(f"{annas_dog.name} is {annas_dog.age} years old.")
annas_dog.speak()
annas_dog.roll_over()

print(type(annas_dog))