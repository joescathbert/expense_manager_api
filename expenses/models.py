from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from bankaccounts.models import BankAccount, PaymentMedium

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    TRANSACTION_TYPES = [
        ("DEBIT", "Debit"),
        ("CREDIT", "Credit"),
    ]

    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    payment_medium = models.ForeignKey(PaymentMedium, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)
    reference_id = models.CharField(max_length=50, blank=True, null=True)
    transaction_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-transaction_date"]

    def __str__(self):
        return f"{self.transaction_type} {self.amount} ({self.bank_account})"

    def clean(self):
        # Ensure payment_medium belongs to the same bank_account
        if not self.bank_account.paymentmedium_set.filter(id=self.payment_medium.id).exists():
            raise ValidationError("Invalid payment medium for this bank account.")
