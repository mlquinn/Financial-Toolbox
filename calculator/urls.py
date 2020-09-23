from django.urls import path
from .views import LoanCaclulatorView
app_name='calculator'
urlpatterns = [
    path('', LoanCaclulatorView.as_view(), name='loan-view'),
]