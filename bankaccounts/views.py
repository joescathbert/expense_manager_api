from rest_framework import viewsets, permissions
from .models import BankAccount, PaymentMedium, BankAccountPaymentMedium
from .serializers import (
    BankAccountSerializer,
    PaymentMediumSerializer,
    BankAccountPaymentMediumSerializer,
)

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentMediumViewSet(viewsets.ModelViewSet):
    queryset = PaymentMedium.objects.all()
    serializer_class = PaymentMediumSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankAccountPaymentMediumViewSet(viewsets.ModelViewSet):
    queryset = BankAccountPaymentMedium.objects.all()
    serializer_class = BankAccountPaymentMediumSerializer
    permission_classes = [permissions.IsAuthenticated]
