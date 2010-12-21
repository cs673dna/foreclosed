from selenium import selenium
import unittest, time, re

class hamp_test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://localhost/")
        self.selenium.start()
    
    def test_hamp_test(self):
        sel = self.selenium
        sel.open("/foreclosed/")
        sel.click("link=HAMP Eligibility Test")
        sel.wait_for_page_to_load("30000")
        sel.click("id_firstMortgage")
        sel.click("id_ownerOccupied")
        sel.click("id_current")
        sel.click("id_freddiFannie")
        sel.type("id_monthlyPayment", "1000")
        sel.type("id_amountOwed", "250000")
        sel.type("id_numberOfUnits", "2")
        sel.type("id_monthlyIncome", "60000")
        sel.type("id_streetAddress", "16 Adelaide Street")
        sel.type("id_cityStateZip", "Boston MA, 02130")
        sel.click("//input[@value='Submit']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
