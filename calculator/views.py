from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Loan, Payment

class LoanDashView(ListView):
    template_name='calculator/loandashview.html'
    model = Loan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loans'] = Loan.objects.all()
        return context


class LoanDetailView(DetailView):
    model = Loan
    template_name='calculator/loanview.html'

class NewLoanView(CreateView):
    model = Loan
    template_name='calculator/newloan_form.html'
    fields = '__all__'
    

    def get_success_url(self):
        return reverse('calculator:loan-detail', kwargs={'pk':self.object.pk})