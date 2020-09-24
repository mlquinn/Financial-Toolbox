from django.urls import path
from .views import LoanDashView, LoanCaclulatorView
app_name='calculator'
urlpatterns = [
    path('dash/', LoanDashView.as_view(), name='loan-dash'),
]