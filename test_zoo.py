import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    
    def test_kid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test_kid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_adolescence_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    def test_adolescence2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    def test_adult2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
        
    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)

    def test_old2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)



    def test_err_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-12), "Error")

if __name__ == '__main__':
    unittest.main()