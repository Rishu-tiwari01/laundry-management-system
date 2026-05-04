from django.db import models, transaction
from django.db.utils import IntegrityError
from django.core.validators import MinValueValidator, RegexValidator
import uuid


class Order(models.Model):
    STATUS_CHOICES = [
        ('RECEIVED', 'Received'),
        ('PROCESSING', 'Processing'),
        ('READY', 'Ready for Pickup'),
        ('DELIVERED', 'Delivered'),
    ]

    order_id = models.CharField(max_length=12, unique=True, editable=False)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?[0-9]{10,15}$',
                message='Enter a valid phone number (10-15 digits)'
            )
        ]
    )
    garment = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price_per_item = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RECEIVED')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.order_id} - {self.customer_name}"

    def save(self, *args, **kwargs):
        self.total_bill = self.quantity * self.price_per_item
        if self.order_id:
            super().save(*args, **kwargs)
            return
        # 8-hex-char IDs (~4B space) — retry on the rare collision
        for _ in range(5):
            self.order_id = uuid.uuid4().hex[:8].upper()
            try:
                with transaction.atomic():
                    super().save(*args, **kwargs)
                return
            except IntegrityError:
                continue
        raise IntegrityError('Could not generate a unique order_id after 5 attempts')
