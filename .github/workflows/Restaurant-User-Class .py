# In this program, I've learned and created the process of declaring and creating user classes with restaurant's of different varieties. Below I shall explain some of the processes of how things work and what their function is.

# First, we should declare some variables, such as the flavors of ice cream these restaurants should have.
default_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]
default_privileges = ["can add post", "can delete post", "can ban user"]

#From there, we will now create our first class, the restaurant class, which is basically putting a name on it for Python to know what its referring to. 
class Restaurant:
    def __init__(self, restaurant_name="Default Restaurant", cuisine_type="Unknown Cuisine"):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

  restaurant = Restaurant()


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


#Here, I've listed the specified variety of restaurants that will be redaily availble.
restaurant1 = Restaurant("Red Lobster", "Seafood")
restaurant2 = Restaurant("Olive Garden", "Italian")
restaurant3 = Restaurant("Taco Bell", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
  
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

# The same process goes into naming our Ice Cream stand
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name="Default Ice Cream Stand", cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = default_flavors

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

#For our restaurant, we'll more than likely need to set up a user and an admin class so that our restaurant can be maneged. Below I've left it blank so the user can set it up as needed. 
#I've also added the necessary security measures, making sure our dear User doesn't end up trying to bruteforce their way in. 
class User:
    def __init__(self, first_name="John", last_name="Doe", age=None, location=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile:\nName: {self.first_name} {self.last_name}")
        if self.age:
            print(f"Age: {self.age}")
        if self.location:
            print(f"Location: {self.location}")
        if self.email:
            print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

#For our user, I've equally made some specific privilege's, since there will be an administrator available
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = default_privileges
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

#Below is the administrator class being setup, with similar setups made like the User, but, now with the privilege class being setup alongside with it. 
class Admin(User):
    def __init__(self, first_name="Admin", last_name="User", age=None, location=None, email=None):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()
