from rest_framework.serializers import ModelSerializer
from apps.sarf.models import Expense

class ExpenseListSerializer(ModelSerializer):

    class Meta:
        model = Expense
        fields = '__all__'

    def validate_summa(self, value):
            if value <= 0:
                raise serializers.ValidationError('Xarajatingiz 0 som dan katta bolishi kerak')
            return value


    def validate_spent_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError('Xarajat sansi kelajakda bolishi mumkin emas')
        return value