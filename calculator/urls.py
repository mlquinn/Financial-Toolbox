from django.urls import path
from .views import LoanDashView, LoanDetailView
app_name='calculator'
urlpatterns = [
    path('dash/', LoanDashView.as_view(), name='loan-dash'),
    path('<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
]