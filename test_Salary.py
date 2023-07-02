import unittest   #import the unittest framework
from  Salary import Employee   # import the class Salary to be tested 
from Salary import Manager 
from Salary import TeamLader

#Create a test class called TestSalary 
class  TestSalary(unittest.TestCase): 


    def setUp(self):

        self.employ = Employee
        self.manager = Manager
        self.teamleader = TeamLader


        pass

        #self.test_salary = Salary
    
    def test_name(self):

        self.assertEqual("Jun AB", self.employ.printname())

        self.assertIsInstance(self.employ.printname(), str)

        self.a("Teklehaimanot Aman", self.test_salary.printname("Teklehaimanot"))


    def test_monthlysalary(self):

        self.assertAlmostEqual(20*8*30, self.manager.Monthlysalary())

        self.assertEqual(12*8*30, self.employ.Monthlysalary())

    def test_title(self):

        self.assertTrue("Manager", self.manager.title())

        self.assertTrue("Junior", self.employ.title())
        self.assertTrue("Team Leader", self.teamleader.title())


if __name__=="__main__":

    a = TestSalary()

    print(a.test_title())
 
