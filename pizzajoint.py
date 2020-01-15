'''
Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

Add a method for interacting with a pizza's toppings, called add_topping.

Add a method for outputting a description of the pizza (sample output below).

Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()
You should produce output in the terminal similiar to the following string.

"I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."
'''

class Pizza: 
  def __init__(self, size, crust):
    self.size = size
    self.crust = crust
    self.topping = ""

  # def add_topping (self, topping):
  #   self.topping = topping
  #   self.toppingsList.append(self.topping)

  def add_topping (self, topping):
    self.topping += topping

  # def print_pizza (self):
  #   print(f'I would like a {self.size}-inch, {self.crust}-crust pizza with {self.toppingsList}')
    
  def print_pizza (self):
    print(f'I would like a {self.size}-inch, {self.crust}-crust pizza with {self.topping}')

papa_special = Pizza("16", "thin")
papa_special.add_topping("shrooms")
papa_special.add_topping(" extra cheese")

papa_special.print_pizza()
