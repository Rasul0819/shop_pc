from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'shop'
urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.register, name='register'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)