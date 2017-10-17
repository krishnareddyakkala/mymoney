from accounts.models import Expenses, MainCategory, SubCategory
import datetime


def str_to_date(date_str):
    date, month, year = date_str.split('/')
    return datetime.date(int(year), int(month), int(date))


def process_hdfc_account_data(data, debit_category):
    for row in data:
        if not row['Withdrawal Amt.']:
            continue
        e = Expenses()
        e.amount = row['Withdrawal Amt.']
        e.description = "{0} {1}".format(row['Narration'], row['Chq./Ref.No.'])

        e.spent_date = str_to_date(row['Value Dt'])
        e.main_category = MainCategory.objects.get(id=1)
        e.sub_category = SubCategory.objects.get(id=1)
        e.debit_category = debit_category
        e.save()

