from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Loan, Payment

class LoanDashView(ListView):
    template_name='calculator/loandashview.html'
    model = Loan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loans'] = Loan.objects.all()
        return context


class LoanCaclulatorView(TemplateView):
    template_name = "calculator/loanview.html"
