from django.urls import path
from .views import (
    ProductListView, ProductDetailView, CategoryListView, CategoryDetailView,
    FileListView, FileDetailView
)
#when we want to imort many items in the same line , import like above

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('products/<int:product_id>/files', FileListView.as_view(), name='file-list'),
    path('products/<int:product_id>/files/<int:pk>', FileDetailView.as_view(), name='file-detail')
]


# to add th url that will be used by the client, 1-give name to above urls 2-in serializers instead of ModelSerializer we shoud have HyperlinkedModelSerializer 3- we add url in the fields


