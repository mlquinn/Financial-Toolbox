from django.urls import path
from .views import LoanDashView, LoanDetailView, NewLoanView
app_name='calculator'
urlpatterns = [
    path('dash/', LoanDashView.as_view(), name='loan-dash'),
    path('new/', NewLoanView.as_view(), name='loan-new'),
    path('<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
]