import unittest

class TestMyStack(unittest.TestCase):
    
    def test_push_and_top(self):
        stack = MyStack()
        stack.push(1)
        self.assertEqual(stack.top(), 1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        stack.push(3)
        self.assertEqual(stack.top(), 3)

    def test_pop(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.empty())

    def test_empty(self):
        stack = MyStack()
        self.assertTrue(stack.empty())
        stack.push(1)
        self.assertFalse(stack.empty())
        stack.pop()
        self.assertTrue(stack.empty())

if __name__ == '__main__':
    unittest.main()
