class User:
    def __init__(self,id,username): # initialize variables
      self.id = id 
      self.username = username
      self.followers = 0
      self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1
      
user_1 = User("20", "Angela Yu")
user_2 = User("21", "Angela Mi")
print(user_1.followers)
 
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)
