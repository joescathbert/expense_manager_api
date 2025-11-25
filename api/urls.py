from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from bankaccounts.views import BankAccountViewSet, PaymentMediumViewSet, BankAccountPaymentMediumViewSet
from expenses.views import ExpenseViewSet, ExpenseCategoryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bank-accounts', BankAccountViewSet)
router.register(r'payment-mediums', PaymentMediumViewSet)
router.register(r'account-payment-mediums', BankAccountPaymentMediumViewSet)
router.register(r"expenses", ExpenseViewSet)
router.register(r"expense-categories", ExpenseCategoryViewSet)

urlpatterns = router.urls
