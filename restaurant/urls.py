from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, LoginTokenView, LogoutTokenView, MenuItemViewSet, RegistrationView
router=DefaultRouter(); router.register("menu",MenuItemViewSet,basename="menu"); router.register("bookings",BookingViewSet,basename="booking")
urlpatterns=[path("",include(router.urls)),path("registration/",RegistrationView.as_view(),name="registration"),path("token/login/",LoginTokenView.as_view(),name="token_login"),path("token/logout/",LogoutTokenView.as_view(),name="token_logout")]
