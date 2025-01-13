from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemViews.as_view(), name='menu'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('restaurant/booking/', include(router.urls)),
    path('message/', views.msg),
     path('api-token-auth/', obtain_auth_token)
]
