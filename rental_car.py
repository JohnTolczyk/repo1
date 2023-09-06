cars = {
    'chevy' : ['camaro','corvette'],
    'ford' : ['mustang','galaxy'],
    'mopar' : ['barracuda','charger'],
}
rental_car = input("what kinda rental car are you looking for?: ")
print(f"let me see if i can find you a {rental_car}.")

if rental_car in cars:
    print(f"\nWe will set you up with your {rental_car} right away!")
else:
    print(f"\nI'm sorry but we do not have a {rental_car} at the moment.")
    
