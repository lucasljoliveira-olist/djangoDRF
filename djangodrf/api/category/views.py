from rest_framework import viewsets
from .serializers import CategorySerializer, BannedCategorySerializer
from .models import Category, BannedCategory

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class BannedCategoryViewSet(viewsets.ModelViewSet):
    queryset = BannedCategory.objects.all().order_by('name')
    serializer_class = BannedCategorySerializer
