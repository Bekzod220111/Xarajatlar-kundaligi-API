from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.sarf.models import Expense
from api.user.serializers import expense_serializers

class ExpenseListAPIView(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = expense_serializers.ExpenseListSerializer

class ExpenseCreateAPIView(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = expense_serializers.ExpenseListSerializer

class ExpenseUpdateAPIView(UpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = expense_serializers.ExpenseListSerializer

class ExpenseDeleteAPIView(DestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = expense_serializers.ExpenseListSerializer