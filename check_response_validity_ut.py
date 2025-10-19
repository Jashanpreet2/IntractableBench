import unittest
from simulator import check_response_validity

class CheckResponseValidityTest(unittest.TestCase):
    def tests(self):
        self.assertEqual(check_response_validity(""), False)
        self.assertEqual(check_response_validity("And then they talked about the experiment"), False)
        self.assertEqual(check_response_validity("Dr. Patel: Yes, that would be good"), False)
        self.assertEqual(check_response_validity("Dr. Patel: Yes, that would be good."), True)
        self.assertEqual(check_response_validity("Dr. Patel: Is that okay?"), True)
        self.assertEqual(check_response_validity("Dr. Patel: That's great!"), True)
        self.assertEqual(check_response_validity("""Dr. Patel: Yes, that would be great!
                                                 
                                                 Jason: Alright then, I will get started."""), True)
        self.assertEqual(check_response_validity("""Dr. Patel: Yes, that would be great!
                                                 Jason: Alright then, I will get started."""), False)

if __name__ == "__main__":
    unittest.main()