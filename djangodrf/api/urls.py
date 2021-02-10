from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .category.views import CategoryViewSet, BannedCategoryViewSet


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'bannedcategory', BannedCategoryViewSet, basename='bannedcategory')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
