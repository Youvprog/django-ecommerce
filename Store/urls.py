from django.urls import path
from . import views

urlpatterns = [
   path('products', views.products_list, name="products-list"),
   path('products/<str:slug>/add-to-cart', views.add_to_cart, name="add-to-cart"),
   path('products/<str:slug>', views.product_detail, name="product-detail"),
   path('cart', views.view_cart, name="cart"),
   path('cart/<str:slug>/update-quantity',views.update_product_quantity, name="update-product-quantity"),
   path('cart/<str:slug>/remove-quantity', views.remove_product_quantity, name="remove-product-quantity"),
   path('cart/<str:slug>/remove-orderitem',views.remove_orderitem, name="remove-orderitem"),
   path('cart/checkout', views.checkout, name="checkout"),
   path('products/category/<int:pk>', views.categorize_product, name="arranged"),
   path('products/sorted-by/<str:slug>', views.sort_prod, name="sorted"),
   path('products/color/<int:pk>', views.sort_with_colors, name="sorted-with-colors"),
   path('products/filter/bysearch', views.product_filter_by_search, name="by-search"),
]
