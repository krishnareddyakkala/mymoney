from django.contrib import admin
from django.contrib import auth
import csv
import os
from django.conf import settings
from django.contrib.admin import DateFieldListFilter

# username: admin
# password: admin123

from accounts.models import MainCategory, SubCategory, DebitCategory, Expenses, UploadData
from utils import process_hdfc_account_data



class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    list_display = [f.name for f in SubCategory._meta.fields]
    list_filter = ('main_category__category_name',)


class ExpensesAdmin(admin.ModelAdmin):
    model = Expenses
    search_fields = ['description', '^main_category__category_name']
    list_filter = (
        ('spent_date', DateFieldListFilter),
    )
    list_display = [f.name for f in Expenses._meta.fields]

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "main_category":
    #         kwargs["queryset"] = Expenses.objects.filter(main_category__category_name=db_field.value)
    #     return super(ExpensesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class DebitCategoryAdmin(admin.ModelAdmin):
    model = DebitCategory
    list_display = [f.name for f in DebitCategory._meta.fields]


class UploadDataAdmin(admin.ModelAdmin):
    model = UploadData
    list_display = [f.name for f in UploadData._meta.fields]

    def save_model(self, request, obj, form, change):
        super(UploadDataAdmin, self).save_model(request, obj, form, change)
        file_url = os.path.join(settings.MEDIA_ROOT, obj.data.url)
        with open(file_url) as csvfile:
            reader = csv.DictReader(csvfile)
            print(obj.debit_category, ' debit category')
            if obj.debit_category.category_name == "HDFC Bank": # HDFC Bank
                process_hdfc_account_data(reader, obj.debit_category)


admin.site.register(MainCategory)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(DebitCategory, DebitCategoryAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(UploadData, UploadDataAdmin)
