# movie tickets

prompt = "\nWelcome!! Our featured film today is Saw! Please tell us your age: "
prompt +="\n(Enter'quit to exit.): "

active = True

while active:
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

    

