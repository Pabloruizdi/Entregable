from django.db import models

class Payment(models.Model):
    choices = models.CharField(max_length=20)
    
    class Meta():
        db_table = "Payment_method"
        verbose_name = 'Payment'
        verbose_name_plural = 'Paymet'

    def __str__(self):
        return self.choices

class Ordenes(models.Model):
    CHOISES = (
        ("Cash", "Cash"),
        ("Card", "Card"),
    )

    cliente = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=CHOISES, max_length=4)



