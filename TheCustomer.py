import random
class Customer:

    def __init__(self,firstName,lastName,id,userName,password):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.userName = userName
        self.password = password
        self.balance = 1500
        self.creditCardNum = self.firstName[0]+self.lastName[0]+str(random.randint(1,10000000))