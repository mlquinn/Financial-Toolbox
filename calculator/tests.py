from django.test import TestCase
from django.urls import reverse

from calculator.models import Loan,Payment

class CalculatorViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_loans = 2
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


    # def test_loanpageview(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    #     print("Loanview status code is 200.")

class LoanModelTests(TestCase):

    def setUp(self):
        Loan.objects.create(
            title="test title",
            description='test desc',
            principle=1000,
            current_balance=900,
            apr=10,
            is_paid=False,
        )

    def test_loancreation(self):
        '''Tests if the loan is created successfully.'''
        loan = Loan.objects.first()
        self.assertIsNotNone(loan)

class PaymentModelTests(TestCase):

    def setUp(self):
        Loan.objects.create(
            title="test title",
            description='test desc',
            principle=1000,
            current_balance=1000,
            apr=10,
            is_paid=False,
        )
        Payment.objects.create(
            loan_id=Loan.objects.first(),
            payment_amount=100,
        )

    def test_paymentcreation(self):
        '''Tests if the payment creates successfully.'''
        payment=Payment.objects.first()
        self.assertIsNotNone(payment)
    
    def test_paymentlowerscurrentbalance(self):
        '''Tests if a new payment lowers the current balance of loan.'''
        loan = Loan.objects.first()
        start_bal = loan.principle
        payment = Payment.objects.first().payment_amount
        bal2 = start_bal - payment
        current = Loan.objects.first().current_balance
        self.assertEqual(bal2, current)