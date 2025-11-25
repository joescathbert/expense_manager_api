from rest_framework import serializers
from .models import Expense, ExpenseCategory

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ["id", "name", "description"]


class ExpenseSerializer(serializers.ModelSerializer):
    category = ExpenseCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ExpenseCategory.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Expense
        fields = [
            "id",
            "bank_account",
            "category",
            "category_id",
            "transaction_type",
            "payment_medium",
            "amount",
            "notes",
            "reference_id",
            "transaction_date",
            "created_at",
            "updated_at",
        ]
