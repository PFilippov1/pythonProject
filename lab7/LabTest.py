import unittest
import Lab7


class LabTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set Up Class Method!"""
        print("Setting up class for tests!")
        print("==========================")

    @classmethod
    def tearDownClass(cls):
        """Tear Down Class Method!"""
        print("==========================")
        print("Cleaning mess after testing!")

    def setUp(self):
        """Set Up Method!"""
        print("Setting up for a test")
        print("==========================")

    def tearDown(self):
        """Tear Down Method!"""
        print("==========================")
        print("Cleaning mess after a test")

    def test_normal_evaluation(self):
        """Normal CAR evaluation test"""

    print("test id: " + self.id())
    self.assertEqual(Car.print_list_brand(brand(toyota, toyota)),
                     "Normal (toyota)")

    def test_lifetime_calc(self):
        """Lifetime_calc method test"""
        self.assertEqual("mazda", Lab7.car1.lifetime_calc(22000))

    def test_car_discount(self):
        """Get_apartment_number method test"""
        self.assertGreater(Lab7.customer_discount(car2.price), Lab7.customer_discount(car1.price))


if __name__ == '__main__':
    unittest.main()
