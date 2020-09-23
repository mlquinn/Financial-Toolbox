from django.test import TestCase

class CalculatorTests(TestCase):

    def test_loanpageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print("Loanview status code is 200.")