from django.test import TestCase
from calculator.models import Loan,Payment
from django.utils.timezone import now

class CalculatorViewTests(TestCase):

    def test_loanpageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print("Loanview status code is 200.")

class LoanModelTests(TestCase):

    def setUp(self):
        Loan.objects.create(
            title="test title",
            description='test desc',
            principle=1000,
            current_balance=900,
            apr=10,
            is_paid=False,
            start_date=now(),
        )

    def test_loancreation(self):
        '''Tests if the loan is create successfully.'''
        loan = Loan.objects.first()
        self.assertIsNotNone(loan)
        print("Loan created.")

class PaymentModelTests(TestCase):

    def setUp(self):
        Loan.objects.create(
            title="test title",
            description='test desc',
            principle=1000,
            current_balance=1000,
            apr=10,
            is_paid=False,
            start_date=now(),
        )
        Payment.objects.create(
            loan_id=Loan.objects.first(),
            payment_amount=100,
            payment_date=now(),
        )

    def test_paymentcreation(self):
        '''Tests if the payment creates successfully.'''
        payment=Payment.objects.first()
        self.assertIsNotNone(payment)
        print("Payment created.")
    
    def test_paymentlowerscurrentbalance(self):
        '''Tests if a new payment lowers the current balance of loan.'''
        loan = Loan.objects.first()
        start_bal = loan.principle
        payment = Payment.objects.first().payment_amount
        bal2 = start_bal - payment
        current = Loan.objects.first().current_balance
        self.assertEqual(bal2, current)
        print("Loan start is : {} Loan balance is: {}.".format(start_bal,current))