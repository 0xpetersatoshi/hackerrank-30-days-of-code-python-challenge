# Parent class
class Person:
	def __init__(self, first_name, last_name, id_number):
		self.first_name = first_name
		self.last_name = last_name
		self.id_number = id_number
	def printPerson(self):
		print("Name:", self.last_name + ",", self.first_name)
		print("ID:", self.id_number)

# Student class inherits Person class
class Student(Person):

    def __init__(self, first_name, last_name, id_number, scores):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.scores = scores

    def calculate(self):
        # Returns the students grade based on average of scores        
        avg = sum(self.scores) / len(self.scores)
        if 90 <= avg <= 100:
            return 'O'
        elif avg >= 80:
            return 'E'
        elif avg >= 70:
            return 'A'
        elif avg >= 55:
            return 'P'
        elif avg >= 40:
            return 'D'
        else:
            return 'T' 


line = input().split()
first_name = line[0]
last_name = line[1]
idNum = line[2]
_ = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(first_name, last_name, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())