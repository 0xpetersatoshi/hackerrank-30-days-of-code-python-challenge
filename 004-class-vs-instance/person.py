class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            self.initialAge = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.initialAge = initialAge

    def am_i_old(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge < 13:
            print("You are young.")
        elif self.initialAge < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def year_passes(self):
        # Increment the age of the person in here
        self.initialAge += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.am_i_old()
    for j in range(0, 3):
        p.year_passes()       
    p.am_i_old()
    print("")