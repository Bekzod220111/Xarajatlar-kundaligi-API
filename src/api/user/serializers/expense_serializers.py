from rest_framework.serializers import ModelSerializer
from apps.sarf.models import Expense
from django.utils import timezone
from rest_framework.validators import ValidationError

class ExpenseListSerializer(ModelSerializer):

    class Meta:
        model = Expense
        fields = '__all__'

    def validate_xarajat_sanasi(self, xarajat_sanasi):
       now = timezone.now()
       if xarajat_sanasi > now:
          raise ValidationError("Xarajat kelajakda bolmaydi")
       return xarajat_sanasi