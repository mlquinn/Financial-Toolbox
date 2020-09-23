from django.shortcuts import render
from django.views.generic import TemplateView

class LoanCaclulatorView(TemplateView):
    template_name = "calculator/loanview.html"
