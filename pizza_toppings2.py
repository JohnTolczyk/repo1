available_toppings = ['sausage','green pepper','onion','pepperoni','black olive','mushroom',]


prompt = "\nWhat Toppings would you like to add to you Pizza?: "
prompt += "\n(Enter 'done' when you are finished choosing your toppings.)"
prompt += "\n(Enter 'quit' to exit the program.)"

requested_toppings = []

active = True

while active:
    topping = input(prompt)
    
    if topping == 'done':
        print("Making your pizza with the following toppings: ")
        for topping in requested_toppings:
            print(topping)
        
    elif topping == 'quit':
        break
    elif topping == 'pineapple':
        print("Go Fuck yourself!")
        break
    else:
        print(f"adding {topping} to your pizza.")
        if topping not in available_toppings:
            print(f"I'm sorry we dont have {topping}.")
        else:
           requested_toppings.append(topping)



        

    