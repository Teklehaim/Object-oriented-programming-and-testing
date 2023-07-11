import unittest   #import the unittest framework
from  Salary import Employee   # import the class Salary to be tested 
from Salary import Manager     # import the class Manager to be tested 
from Salary import TeamLeader    # import the class TeamLeader 

#Create a test class called TestSalary 
class  TestSalary(unittest.TestCase): 

    def setUp(self):

        self.employ = Employee("Teklehaimanot", "Aman")
        self.manager = Manager("Tewelde", "Beraki")
        self.teamleader = TeamLeader("Getnet", "Ayele")
    
    def test_name(self):

        self.assertEqual("Teklehaimanot"+" "+"Aman", self.employ.firstname+" "+self.employ.lastname)
        self.assertEqual("Getnet"+" "+"Ayele", self.teamleader.firstname+" "+self.teamleader.lastname)
        self.assertIsInstance(self.employ.firstname, str)
        self.assertIsInstance(self.employ.lastname, str)


    def test_monthlysalary(self):
        self.assertEqual(12*8*30, self.employ.monthlysalary())
        self.assertAlmostEqual(20*8*30, self.manager.monthlysalary())
        self.assertAlmostEqual(20*8*30, self.teamleader.monthlysalary())


    def test_title(self):

        with self.subTest("Tests title"):

            self.assertTrue("Manager"==self.manager.title(), "This is expected to be correct ")

        with self.subTest("Test the employ's Title "):
            self.assertTrue("Junior"==self.employ.title(), "This is expected to be correct")

        with self.subTest("Test the team leader's Title "):
            self.assertTrue("Team Leader"==self.teamleader.title(), "This will expected to be correct")

        with self.subTest("Test the team leader's Title "):
            self.assertNotEqual("Team Lader"==self.teamleader.title(), "This is wrong, expected to fail")

if __name__=="__main__":

    unittest.main()

