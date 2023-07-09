import unittest   #import the unittest framework
from  Salary import Employee   # import the class Salary to be tested 
from Salary import Manager     # import the class Manager to be tested 
from Salary import TeamLeader    # import the class TeamLeader 

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
        
    def test_monthlysalary(self):

        self.assertAlmostEqual(20*8*30, self.manager.Monthlysalary())

        self.assertEqual(12*8*30, self.employ.Monthlysalary())

    def test_title(self):

    with self.subTest("Tests title"):
        self.assertTrue("Manager", self.manager.title(), "This is expected to be correct ")

    with self.subTest("Test the employ's Title "):
        self.assertTrue("Junior", self.employ.title(), "This is expected to be correct")

    with self.subTest("Test the team leader's Title "):
        self.assertTrue("Team Leader", self.teamleader.title(), "This will expected to be correct")

    with self.subTest("Test the team leader's Title "):
        self.assertNotEqual("Team Lader", self.teamleader.title(), "This is wrong, expected to fail")

if __name__=="__main__":

    a = TestSalary()

    print(a.test_title())
 
