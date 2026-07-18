from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from apps.sarf.models import Category
from api.user.serializers import category_serializers

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = category_serializers.CategoryListSerializer

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = category_serializers.CategoryListSerializer

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = category_serializers.CategoryListSerializer

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = category_serializers.CategoryListSerializer