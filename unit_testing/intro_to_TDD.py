import unittest
# def isEven(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# def reverseList(arr):
#     for i in range(int(len(arr)/2)):
#         arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
#     return arr

# def isPalindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False

import math
def coins(value):
    change = []
    quarters = math.floor(value / 25)
    change.append(quarters)

    value = value - quarters*25
    dimes = math.floor(value / 10)
    change.append(dimes)
    
    value = value - dimes*10
    nickels = math.floor(value / 5)
    change.append(nickels)

    value = value - nickels*5
    pennies = math.floor(value / 1)
    change.append(pennies)

    return change

# initialized by creating a class that inherits from unittest.TestCase
# class IsEvenTests(unittest.TestCase):
#     # each method in this class is a test to be run
#     def testTwo(self):
#         self.assertEqual(isEven(2), True) # another way to write above is: self.assertTrue(isEven(2)
#     def testThree(self):
#         self.assertEqual(isEven(3), False) # another way to write above is: self.assertFalse(isEven(3))
#         # any task you want run before any method above is executed, put them in the setUp method
#     def setUp(self):
#         # add the setUp tasks
#         print("running setUp")
#     # any task you want run after the tests are executed, put them in the tearDown method
#     def tearDown(self):
#         # add the tearDown tasks
#         print("running tearDown tasks")

# class ReverseListTests(unittest.TestCase):
#     # each method in this class is a test to be run
#     def testTwo(self):
#         self.assertEqual(reverseList([1,2,3]), [3,2,1])
#     def testThree(self):
#         self.assertEqual(reverseList([5,1,2,3]), [3,2,1,5])
#         # any task you want run before any method above is executed, put them in the setUp method
#     def setUp(self):
#         # add the setUp tasks
#         print("running setUp")
#     # any task you want run after the tests are executed, put them in the tearDown method
#     def tearDown(self):
#         # add the tearDown tasks
#         print("running tearDown tasks")


# class IsPalindromeTests(unittest.TestCase):
#     # each method in this class is a test to be run
#     def testTwo(self):
#         self.assertEqual(isPalindrome("racecar"), True)
#     def testThree(self):
#         self.assertFalse(isPalindrome("rabcr"), False)
#         # any task you want run before any method above is executed, put them in the setUp method
#     def setUp(self):
#         # add the setUp tasks
#         print("running setUp")
#     # any task you want run after the tests are executed, put them in the tearDown method
#     def tearDown(self):
#         # add the tearDown tasks
#         print("running tearDown tasks")


class CoinsTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(coins(87), [3,1,0,2])
    def testThree(self):
        self.assertFalse(coins(50), [3,1,0,2])
        # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # this runs our tests