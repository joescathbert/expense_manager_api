from django.db import models
from users.models import User

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bank_accounts")
    account_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30, blank=True, null=True)
    ifsc_code = models.CharField(max_length=15, blank=True, null=True)
    salary_account = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_name} ({self.bank_name})"


class PaymentMedium(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BankAccountPaymentMedium(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="payment_medium_links")
    payment_medium = models.ForeignKey(PaymentMedium, on_delete=models.CASCADE, related_name="bank_account_links")
    details = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("bank_account", "payment_medium")

    def __str__(self):
        return f"{self.bank_account} - {self.payment_medium}"
