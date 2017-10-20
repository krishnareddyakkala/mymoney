from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormMixin
from .models import Expenses
from django.db.models import F, FloatField, Sum
from .forms import  DateRangeForm


class ExpenseListChart(View):
    http_method_names = ['get', 'post']
    template_name = "expenses.html"
    context_object_name = 'expense_main_category'
    form = DateRangeForm

    def get(self, request, *args, **kwargs):
        print("####################")
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

    def get_context_data(self, request):

        context = {}
        context['expense_main_sub_category'] = Expenses.objects.values('main_category__category_name',
                                                                       'sub_category__category_name') \
            .annotate(check_sum=Sum(F('amount'), output_field=FloatField()))
        context['total_amount'] = Expenses.objects.aggregate(Sum(F('amount'), output_field=FloatField()))

        context['date_range_form'] = DateRangeForm(request.GET)
        context['expense_main_category'] = self.get_queryset(request)

        return context

    def get_queryset(self, request):
        print("in query set")
        form = DateRangeForm(request.POST)
        print (request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            print (start_date,   end_date)
            expenses = Expenses.objects.filter(spent_date__range=(start_date, end_date))
        else:
            expenses = Expenses.objects
        print (expenses)
        return expenses.values('main_category__category_name').annotate(
            check_sum=Sum(F('amount'), output_field=FloatField()))

    def post(self, request, *args, **kwargs):
        print(" ********************************** ")
        context = self.get_context_data(request)

        return render(request, self.template_name, context)
