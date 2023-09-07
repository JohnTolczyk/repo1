# movie tickets

prompt = "\nWelcome!! Our featured film today is Saw! Please tell us your age: "
prompt +="\nLimit 4 tickets per party.(Enter'quit to exit.): "

guests = []

while True:
    age = input(prompt)
    if age == 'quit':
       break
    age = int(age)
    if age < 4:
           price = 0    
    elif age < 18:
           price = 5
    elif age < 65:
             price = 15
    elif age >= 65:
             price = 7
    
    print(f"Your admission cost is ${price}.")
    guests.append(price)
    if len(guests) >= 4:
       print("You have reached your limit on tickets.")
       print(f"Your total is ${sum(guests)}.")
       break
       




    

