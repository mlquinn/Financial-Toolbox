from django.test import TestCase
from django.urls import reverse

from calculator.models import Loan


class CalculatorViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_loans = 2 
        #if changed, update number in test_loandash_shows_all_loans()
        
        for loan_id in range(0, number_of_loans):
            Loan.objects.create(
                title='test loan',
                description='testing the view page',
                principle=1000,
                current_balance=1000,
                apr=10,
            )
    def test_loandash_url_is_at_desired_location(self):
        '''Tests to verify the loan dashboard is at the proper URL.'''
        response = self.client.get('/dash/')
        self.assertEqual(response.status_code, 200)

    def test_loandash_url_is_accessible_by_name(self):
        '''Tests to verify the loan dashboard is accessible by URL name.'''
        response = self.client.get(reverse('calculator:loan-dash'))
        self.assertEqual(response.status_code, 200)

    def test_loandash_shows_all_loans(self):
        '''Tests to verify all loans are displayed on the page.'''
        response = self.client.get(reverse('calculator:loan-dash'))
        self.assertTrue(len(response.context['loans']) == 2)
