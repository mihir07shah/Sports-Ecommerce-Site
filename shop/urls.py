from django.contrib import admin
from django.urls import path
from . import views


# ... your normal urlpatterns here



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="shop-index"),
    path('about/',views.about, name="shop-about"),
    path('contact/',views.contact, name="shop-contact"),
    path('tracker/',views.tracker, name="shop-tracker"),
    path('search/',views.search, name="shop-search"),
    path("products/<int:myid>/", views.productView, name="shop-products"),
    path('checkout/',views.checkout, name="shop-checkout"),

]

