import unittest   #import the unittest framework
from  Salary import Employee   # import the class Salary to be tested 
from Salary import Manager     # import the class Manager to be tested 
from Salary import TeamLeader    # import the class TeamLeader 

#Create a test class called TestSalary 
class  TestSalary(unittest.TestCase): 

    def setUp(self):

        self.employ = Employee("Teklehaimanot","Aman")
        self.manager = Manager("Teklehaimanot","Aman")
        self.teamleader = TeamLeader("Teklehaimanot","Aman")
   
    def test_name(self):

        with self.subTest("Test first name"):
            self.assertEqual("Teklehaimanot Aman", self.employ.fullname(), "Full name correct, expected returns True ")

        with self.subTest("Test name is not equal"):
            self.assertNotEqual("Teklemariam Berhe", self.employ.fullname(),"Full name is not correct,expected returns True")

        with self.subTest("Test first name"):
            self.assertEqual("Teklehaimanot", self.employ.firstname, "Test first name, expected returns True")

        with self.subTest("Test last name "):
            self.assertEqual("Aman", self.employ.lastname, "Last name, expected returns True ")

        with self.subTest("Test last name "):
            self.assertFalse("Aman", self.employ.lastname, "Test last name, expected return False")

        with self.subTest("Test first name is false"):
            self.assertFalse("Getnet", self.employ.firstname, "Test first name, expected error/return False")

        #self.assertIsInstance(self.employ.printname(), str)

    def test_monthlysalary(self):

        with self.subTest("Test equality of the salary of manager"):
            self.assertEqual(20*8*30,self.manager.monthlysalary(), "The Manager monthly salary is equal")

        with self.subTest("Test junior salary"):
            self.assertEqual(12*30*8,self.employ.monthlysalary(),"The Junior salary is equal")

        with self.subTest("Test junior salary"):
            self.assertEqual(12*30*6,self.employ.monthlysalary(),"The Junior salary is wrong")

        with self.subTest("Test the class of the monthly salary"):
            self.assertIsInstance(self.employ.monthlysalary(),(int,float), "The salary should be either float or integer.")

        with self.subTest("Test monthly salary data class"):
            self.assertNotIsInstance(self.employ.monthlysalary(),str, "Will give true, the salary is always numerical")

        with self.subTest("Test monthly salary data class"):
            self.assertNotIsInstance(self.employ.monthlysalary(),(int, float), "Will give error because the salary is either float or integer")
        
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

    unittest.main()

