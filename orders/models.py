from django.db import models
import uuid

class Order(models.Model):
    STATUS_CHOICES = [
        ('RECEIVED','RECEIVED'),('PROCESSING','PROCESSING'),('READY','READY'),('DELIVERED','DELIVERED')
    ]
    order_id = models.CharField(max_length=12, unique=True, editable=False)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    garment = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RECEIVED')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4()).split('-')[0].upper()
        self.total_bill = self.quantity * self.price_per_item
        super().save(*args, **kwargs)