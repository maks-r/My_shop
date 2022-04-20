import orderapp.views as orderapp
from django.urls import path

app_name="orderapp"

urlpatterns = [
path('', orderapp.OrderList.as_view(), name='orders_list'),
path('forming/complete/<int:pk>/', orderapp.order_forming_complete, name='order_forming_complete'),
path('create/', orderapp.OrderCreate.as_view(), name='order_create'),
path('read/<int:pk>/', orderapp.OrderDetail.as_view(), name='order_read'),
path('update/<int:pk>/', orderapp.OrderUpdate.as_view(), name='order_update'),
path('delete/<int:pk>/', orderapp.OrderDelete.as_view(), name='order_delete'),
path('product/<int:pk>/price/', orderapp.product_price, name='product_price')
]