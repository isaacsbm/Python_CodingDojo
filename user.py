"""
Attributes:
    Instant of User Arguments:
        first_name , last_name , email , age
    Instant of Default Attributes:
        is_rewards_member - default value of False
        gold_case_points = 0
Methods:
    display_info(self) - print all users' detials on seperate lines
    enroll(self) - change user's member status to True and set gold card points to 200
        BONUS: add "User already a member" and check if they are a member
    spend_points(self, amount) - have this method descreased user's points by amount specified
        BONUS: check to see if they have enough points to spend that amount
"""
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member= False
        self.gold_case_points = 0
    def enroll(self):
        if self.is_rewards_member:
            print((f"{self.first_name} is already a member"))
        else:
            self.is_rewards_member = True
            self.gold_case_points = 200
            print((f"{self.first_name} has been enrolled as a member"))
        return self
    def spend_points(self, amount):
        if self.gold_case_points < amount:
            print((f"Your balance of {self.gold_case_points} is too low for this purchase"))
        else:
            self.gold_case_points = self.gold_case_points - amount
            print ((f"{self.gold_case_points} is left in your balance"))
        return self


    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

luna_lovegood = User("Luna", "Lovegood", "lunalovegood@gmail.com", 16)
luna_lovegood.display_info().enroll().spend_points(50).display_info()