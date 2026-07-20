from django.db import models

# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summa = models.PositiveIntegerField()
    izoh = models.TextField(blank=True, null=True)
    xarajat_sanasi = models.DateTimeField()

    def __str__(self):
        return self.summa
        