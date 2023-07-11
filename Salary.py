# Base class for all employees. This class doesn't inherit anything from other classes
class Employee:
    # constructor (initializer) for new object of type "Employee"
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.fullname = self.firstname+" "+ self.lastname
    
    # A method used to print the names and full name of each employee
    def printname(self):
        print('Full Name: ', self.firstname, self.lastname)
        
    def monthlysalary(self):
        return 12*8*30

    def title(self):
        return "Junior"
        
    def printtitle(self):
        print("Title = ", self.title())   
        
    def printSalary(self):
        print("Gross monthly salary = ", self.monthlySalary())
        
 # A manager class inheriting from the Employee class and modifying how its salary is calculated (polymorphism)       
class Manager(Employee):
    def monthlySalary(self):
        return 20*8*30
    def title(self):
        return "Manager"

# A TeamLeader class inheriting from the Manager class with modification on the title (polymorphism)       
class TeamLeader(Manager):
    def title(self):
        return "Team Leader"  
        
def main():
    #Creating a list of employees using the Employee class type as an umbrella
    AllEmployees = []
    
    # instantiating an object of type Employee class and adding it to the list    
    JunAB = Employee("Jun", "AB") 
    AllEmployees.append(JunAB)
    
    # instantiating an object of type Manager class and adding it to the list    
    MangCD = Manager("Mang", "CD") 
    AllEmployees.append(MangCD)    

    # instantiating an object of type TeamLeader class and adding it to the list    
    TeamLeadCD = TeamLeader("TeamLead", "EF") 
    AllEmployees.append(TeamLeadCD)

   
    
    # Printing all the the employees names, titles and salaries
    print('\n----------------------------')
    for empX in AllEmployees:
        empX.printName()
        empX.printTitle()
        empX.printSalary()
        print('----------------------------\n')
        
#Entry point to execute the main method
if __name__ == "__main__":
    main()
            