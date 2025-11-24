from rest_framework import serializers
from .models import BankAccount, PaymentMedium, BankAccountPaymentMedium

class PaymentMediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMedium
        fields = "__all__"


class BankAccountSerializer(serializers.ModelSerializer):
    payment_mediums = serializers.SerializerMethodField()

    class Meta:
        model = BankAccount
        fields = ["id", "user", "account_name", "bank_name", "account_number",
                  "ifsc_code", "salary_account", "created_at", "payment_mediums"]

    def get_payment_mediums(self, obj):
        return [link.payment_medium.name for link in obj.payment_medium_links.all()]


class BankAccountPaymentMediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountPaymentMedium
        fields = "__all__"
