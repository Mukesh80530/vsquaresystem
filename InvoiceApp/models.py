from django.db import models

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()

class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    units = models.IntegerField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)