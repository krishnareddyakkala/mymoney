from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible  # only if you need to support Python 2
class MainCategory(models.Model):
    category_name = models.CharField("Category Name", max_length=120, unique=True)

    def __str__(self):
        return self.category_name


@python_2_unicode_compatible  # only if you need to support Python 2
class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    category_name = models.CharField("Category Name", max_length=120, unique=True)

    class Meta:
        ordering = ['main_category__category_name']

    def __str__(self):
        return self.category_name

# test commit
class DebitCategory(models.Model):
    category_name = models.CharField("Category Name", max_length=120, unique=True)

    def __str__(self):
        return self.category_name


class Expenses(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    debit_category = models.ForeignKey(DebitCategory, on_delete=models.CASCADE)
    description = models.TextField()
    spent_date = models.DateField("Spent on Date")
    amount = models.FloatField("Amount Spent")
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}".format(self.description)


class UploadData(models.Model):
    data = models.FileField()
    upload_time = models.DateTimeField(auto_now_add=True)
    debit_category = models.ForeignKey(DebitCategory, on_delete=models.CASCADE)


