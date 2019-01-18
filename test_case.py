import unittest
a = 1
b = 2



class Test_first_test(unittest.TestCase):

    def test_add(self):
        c = a + b
        print(c)
        self.assertEqual(c, 3)



    def test_subtract(self):
        d = a - b

        print(d)
        self.assertEqual( d, -1)
if __name__ == '__main__':
    unittest.main()


