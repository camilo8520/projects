
from calendar import c


def coffee_bot():
  print('Welcome to the cafe!')

def get_size():
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>")
    if res == "a":
        return "small"
    elif res == "b":
        return "medium"
    elif res == "c":
        return "large"
    else:
        print_message()
    return get_size()

def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
    res = input("""
What type of drink would you like?
[a] Brewed Coffee
[b] Mocha
[c] Latte
    """)
    if res == "a":
        return "brewed coffee"
    elif res == "b":
        return "mocha"
    elif res == "c":
        return order_latte()
    else:
        print_message()
    return get_drink_type()

def order_latte():
    res = input("""
    And what kind of milk for your latte?
[a] 2% milk
[b] Non-fat milk
[c] Soy milk
    """)
    if res == "a":
        return "latte" 
    elif res == "b":
        return "non-fat latte"
    elif res == "c":
        return "soy latte"
    else:
        print_message()
    return order_latte()

coffee_bot()
size = get_size()
#print(size)
drink_type = get_drink_type()
#print(drink_type)

print("Alright, that's a {} {}!".format(size, drink_type))

name = input("Can I get your name please?\n>")

print("Thanks, {} Your drink will be ready shortly.".format(name))


  