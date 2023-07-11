import unittest
from Salary import Employee, Manager, TeamLeader

class TestEmployeeClass(unittest.TestCase):        
    
    def test_EmployeeFirstName(self):
        #Arrange and setup
        Obj01 = Employee('AA', 'BB')        
        #Assert
        self.assertEqual(Obj01.firstname,'AA',"Junior First name failed")
        
    def test_EmployeeLastName(self):
        #Arrange and setup
        Obj01 = Employee('AA', 'BB')  
        #Assert    
        self.assertEqual(Obj01.lastname,'BB',"Junior Last name failed")
        
    def test_EmployeeTitle(self):
        #Arrange and setup
        Obj01 = Employee('AA', 'BB')  
        #Assert 
        self.assertEqual(Obj01.title(),'Junior',"Junior Title failed")
        
    def test_EmployeeSalary(self):
        #Arrange and setup
        Obj01 = Employee('AA', 'BB')  
        #Assert 
        self.assertEqual(Obj01.monthlySalary(),2880,"Junior Monthly salary calculation failed")

class TestManagerClass(unittest.TestCase):
    def test_ManagerFirstName(self):
        #Arrange and setup
        Obj01 = Manager('CC', 'DD')        
        #Assert
        self.assertEqual(Obj01.firstname,'CC',"Manager First name failed")
        
    def test_ManagerLastName(self):
        #Arrange and setup
        Obj01 = Manager('CC', 'DD')  
        #Assert    
        self.assertEqual(Obj01.lastname,'DD',"Manager Last name failed")
        
    def test_ManagerTitle(self):
        #Arrange and setup
        Obj01 = Manager('CC', 'DD')  
        #Assert 
        self.assertEqual(Obj01.title(),'Manager',"Manager Title failed")
        
    def test_ManagerSalary(self):
        #Arrange and setup
        Obj01 = Manager('CC', 'DD')  
        #Assert 
        self.assertEqual(Obj01.monthlySalary(),4800,"Manager Monthly salary calculation failed")
        
class TestTeamLeaderClass(unittest.TestCase):
    def test_TeamLeaderFirstName(self):
        #Arrange and setup
        Obj01 = TeamLeader('EE', 'FF')        
        #Assert
        self.assertEqual(Obj01.firstname,'EE',"Team Leader First name failed")
        
    def test_TeamLeaderLastName(self):
        #Arrange and setup
        Obj01 = TeamLeader('EE', 'FF')  
        #Assert    
        self.assertEqual(Obj01.lastname,'FF',"Team Leader Last name failed")
        
    def test_TeamLeaderTitle(self):
        #Arrange and setup
        Obj01 = TeamLeader('EE', 'FF')  
        #Assert 
        self.assertEqual(Obj01.title(),'Team Leader',"Team Leader Title failed")
        
    def test_TeamLeaderSalary(self):
        #Arrange and setup
        Obj01 = TeamLeader('EE', 'FF')  
        #Assert 
        self.assertEqual(Obj01.monthlySalary(),4800,"Team Leader Monthly salary calculation failed")
  

if __name__ == '__main__':
    unittest.main()