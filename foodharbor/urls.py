from django.urls import path
from foodharbor.views.StoreView import StoreListView, StoreView
from foodharbor.views.StoreCategoryView import StoreCategoryListView, StoreCategoryView

urlpatterns = [
    path('store/', StoreView.as_view(), name='store'),
    path('store/list/', StoreListView.as_view(), name='store_list_all'),
    path('store/category/', StoreCategoryView.as_view(), name='store_category'),
    path('store/category/list', StoreCategoryListView.as_view(), name='store_category_list'),
]