from django.contrib import admin
from django.urls import path
from book import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TopView.as_view(), name="top"),
    path('book/',views.ProductListView.as_view(),name="list"),
]