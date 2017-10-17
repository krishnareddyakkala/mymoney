from django.shortcuts import render
from django.views.generic import ListView
from .models import Expenses
from django.db.models import F, FloatField, Sum
from .forms import  DateRangeForm


class ExpenseListChart(ListView):
    template_name = "expenses.html"
    context_object_name = 'expense_main_category'
    form = DateRangeForm

    def get_context_data(self, **kwargs):
        context = super(ExpenseListChart, self).get_context_data(**kwargs)
        context['expense_main_sub_category'] = Expenses.objects.values('main_category__category_name', 'sub_category__category_name').annotate(
            check_sum=Sum(F('amount'), output_field=FloatField()))
        context['total_amount'] = Expenses.objects.aggregate(Sum(F('amount'), output_field=FloatField()))

        if 'date_range_form' not in context:
            context['date_range_form'] = DateRangeForm(self.request.GET)

        return context

    def get_queryset(self):
        form = DateRangeForm(self.request.GET)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            expenses = Expenses.objects.filter(spent_date__range=(start_date, end_date))
        else:
            expenses = Expenses.objects
        return expenses.values('main_category__category_name').annotate(
            check_sum=Sum(F('amount'), output_field=FloatField()))
