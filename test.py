import unittest   #import the unittest framework
from  Salary import Employee   # import the class Salary to be tested 
from Salary import Manager 
from Salary import TeamLader

#Create a test class called TestSalary 
class  TestSalary(unittest.TestCase): 


    def setUp(self):

        self.employ = Employee("Jun", "AB")
        self.manager = Manager("Mang", "CD")
        self.teamleader = TeamLader("TeamLead", "EF")


        pass

        #self.test_salary = Salary
    
    def test_name(self):

        self.assertEqual("Jun", self.employ.firstname)
        self.assertEqual("AB", self.employ.lastname)

        #self.assertIsInstance(self.employ.printname(), str) #the print name doesn't return value. What do you want test here?
        
    def test_monthlysalary(self):

        self.assertAlmostEqual(20*8*30, self.manager.monthlysalary())

        self.assertEqual(12*8*30, self.employ.monthlysalary())

    def test_title(self):

        self.assertTrue("Manager", self.manager.title())

        self.assertTrue("Junior", self.employ.title())
        self.assertTrue("Team Leader", self.teamleader.title())


if __name__=="__main__":
    unittest.main()
 
