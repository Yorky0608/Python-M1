class GPA:
    pass
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def check_honors(self):
        if self.gpa >= 3.25:
            return True
    
    def check_deans_list(self):
        if self.gpa >= 3.5:
            return True
            
    def deans_list_or_honors(self):
        if self.check_deans_list():
            return f"{self.name} is on the Dean's List."
        elif self.check_honors():
            return f"{self.name} has honors."
        else:
            return f"{self.name} does not have honors."

# Example usage:
student1 = GPA("Alice", 3.6)
print(student1.deans_list_or_honors())

student2 = GPA("Bob", 3.2)
print(student2.deans_list_or_honors())

student3 = GPA("Charlie", 3.8)
print(student3.deans_list_or_honors())

student4 = GPA("Mike", 2.8)
print(student4.deans_list_or_honors())

student5 = GPA("Anne", 3.1)
print(student5.deans_list_or_honors())