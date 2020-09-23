from django.db import models

class Loan(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    principle = models.FloatField()
    current_balance = models.FloatField()
    apr = models.FloatField()
    is_paid = models.BooleanField(default=False)
    start_date = models.DateField()

    def __str__(self):
        return self.title

class Payment(models.Model):
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.DateField()
