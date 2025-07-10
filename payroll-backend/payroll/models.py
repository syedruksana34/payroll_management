from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    basic_salary = models.IntegerField()
    allowance = models.IntegerField()
    deductions = models.IntegerField()
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def _str_(self):
        return self.name

