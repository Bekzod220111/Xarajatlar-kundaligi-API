from django.db import models

# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summa = models.DecimalField(max_digits=10, decimal_places=2)
    izoh = models.TextField(blank=True, null=True)
    xarajat_sanasi = models.DateField(auto_now=True)

    def __str__(self):
        return self.summa
        