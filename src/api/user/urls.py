from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views.category_views import CategoryListAPIView, CategoryCreateAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView
from api.user.views.expense_views import ExpenseListAPIView, ExpenseCreateAPIView, ExpenseUpdateAPIView, ExpenseDeleteAPIView
router = DefaultRouter()
router.include_root_view = False

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/delete/<int:pk>/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    path('expense/', ExpenseListAPIView.as_view(), name='expense-list'),
    path('expense/create/', ExpenseCreateAPIView.as_view(), name='expense-create'),
    path('expense/update/<int:pk>/', ExpenseUpdateAPIView.as_view(), name='expense-update'),
    path('expense/delete/<int:pk>/', ExpenseDeleteAPIView.as_view(), name='expense-delete'),

    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),
]
