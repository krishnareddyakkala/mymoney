from django.conf.urls import url
from accounts.views import ExpenseListChart

urlpatterns = [
    url(r'^$', ExpenseListChart.as_view(), name="chart_view"),
]