from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, RegistrationSerializer
User=get_user_model()
class MenuItemViewSet(viewsets.ModelViewSet):
 queryset=MenuItem.objects.all().order_by("id")
 serializer_class=MenuItemSerializer
 permission_classes=[permissions.IsAuthenticatedOrReadOnly]
class BookingViewSet(viewsets.ModelViewSet):
 queryset=Booking.objects.select_related("user").all()
 serializer_class=BookingSerializer
 permission_classes=[permissions.IsAuthenticated]
 def perform_create(self,serializer): serializer.save(user=self.request.user)
class RegistrationView(generics.CreateAPIView):
 queryset=User.objects.all(); serializer_class=RegistrationSerializer; permission_classes=[permissions.AllowAny]
class LoginTokenView(ObtainAuthToken):
 permission_classes=[permissions.AllowAny]
 def post(self,request,*args,**kwargs):
  response=super().post(request,*args,**kwargs); token=Token.objects.get(key=response.data["token"])
  return Response({"token":token.key,"user_id":token.user_id,"username":token.user.username})
class LogoutTokenView(APIView):
 permission_classes=[permissions.IsAuthenticated]
 def post(self,request):
  request.user.auth_token.delete(); return Response({"detail":"Successfully logged out."})
