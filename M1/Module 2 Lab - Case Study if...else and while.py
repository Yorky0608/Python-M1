class GPA:
    pass
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
    
    def check_honors(self):
        if self.gpa >= 3.25:
            return True
    
    def check_deans_list(self):
        if self.gpa >= 3.5:
            return True
            
    def deans_list_or_honors(self):
        if self.check_deans_list():
            return f"{self.first_name} {self.last_name} is on the Dean's List."
        elif self.check_honors():
            return f"{self.first_name} {self.last_name} has honors."
        else:
            return f"{self.first_name} {self.last_name} does not have honors."
        
# Example usage:
student1 = GPA("Alice", "Smith", 3.6)
print(student1.deans_list_or_honors())

student2 = GPA("Bob", "Johnson", 3.2)
print(student2.deans_list_or_honors())

student3 = GPA("Charlie", "Brown", 3.8)
print(student3.deans_list_or_honors())

student4 = GPA("Mike", "Davis", 2.8)
print(student4.deans_list_or_honors())

student5 = GPA("Anne", "Wilson", 3.1)
print(student5.deans_list_or_honors())