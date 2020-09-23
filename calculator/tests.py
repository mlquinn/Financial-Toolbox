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
        loan = Loan.objects.first()
        self.assertIsNotNone(loan)
        print("Loan created.")

class PaymentModelTests(TestCase):

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
        Payment.objects.create(
            loan_id=Loan.objects.first(),
            payment_amount=100,
            payment_date=now(),
        )

    def test_paymentcreation(self):
        payment=Payment.objects.first()
        self.assertIsNotNone(payment)
        print("Payment created.")