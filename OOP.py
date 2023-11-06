"""Object Oriented Programming"""

class Podracer:

  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"


class AnakinsPod(Podracer):

  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def boost(self):
    self.max_speed *= 2


class SebulbasPod(Podracer):

  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self, other):
    other.condition = "thrashed"


"""
1. The previous OOP function displays encapsulation (took the information of podracers and put into a class), inheritance and polymorphism by reusing code and same interface in different classes. 

2. This style works with this function because the data is mutable when certain methods are applied. 

3. OOP helped because the same code was used in different classes and the data changes once it is ran through the classes and methods. 
"""

"""
Reflection 

1. Depending on what you're trying to achieve, a certain paradigm might better to apply, but one isnt better than the other. 

2. If I had choice, OOP would be my preference. It is easier for me to understand since it broken down to class and methods. 

3. Functional progamming would come in handy if the program plans on performing the same task with similar outcome, like rearranging data. OOP is functional when creating a program that changes status, data or instances of a class. 

4. I definitely need to familiarize myself with Functional Programming. Its just a matter or practicing. 
"""