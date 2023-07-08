# Base class for all employees. This class doesn't inherit anything from other classes
class Employee:
    # constructor (initializer) for new object of type "Employee"
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.fullname = self.firstname+" "+ self.lastname
    
    # A method used to print the names and full name of each employee
    def printname(self):

        return self.firstname+ " "+ self.lastname
        print('Full Name: ', self.firstname, self.lastname)
    
    def printfullname(self):

        return self.fullname

        #print("FUll Name :", self.fullname)
        
    def monthlysalary(self): # 
        # Instead writing manually, we can create attribute for the price 

        return 12*8*30

    def title(self):
        return "Junior"
    
    # This can also integrated in the attribute as a position 
    # ( self.title = position kind of )
        
    def printtitle(self):
        print("Title = ", self.title())   
        
    def printsalary(self):
        print("Gross monthly salary = ", self.monthlysalary())
        
 # A manager class inheriting from the Employee class and modifying how its salary is calculated (polymorphism)       
class Manager(Employee):
    def monthlysalary(self):
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
        empX.printname()
        empX.printtitle()
        empX.printsalary()
        print('----------------------------\n')
        
#Entry point to execute the main method
if __name__ == "__main__":
    main()
            