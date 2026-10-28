from datetime import timedelta
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Booking, MenuItem
User=get_user_model()
class MenuItemAPITests(APITestCase):
 def setUp(self): self.item=MenuItem.objects.create(title="Greek Salad",price=Decimal("12.50"),inventory=20)
 def test_list_menu_items(self):
  r=self.client.get("/api/menu/"); self.assertEqual(r.status_code,status.HTTP_200_OK); self.assertEqual(r.data[0]["title"],"Greek Salad")
 def test_create_menu_requires_authentication(self):
  r=self.client.post("/api/menu/",{"title":"Lemon Cake","price":"5.00","inventory":8},format="json"); self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)
 def test_authenticated_user_can_create_menu_item(self):
  u=User.objects.create_user(username="chef",password="SafePassword123"); self.client.force_authenticate(user=u)
  r=self.client.post("/api/menu/",{"title":"Lemon Cake","price":"5.00","inventory":8},format="json"); self.assertEqual(r.status_code,status.HTTP_201_CREATED)
class BookingAPITests(APITestCase):
 def setUp(self): self.user=User.objects.create_user(username="guest",password="SafePassword123"); self.client.force_authenticate(user=self.user)
 def test_authenticated_user_can_create_booking(self):
  r=self.client.post("/api/bookings/",{"name":"Alex","no_of_guests":2,"booking_date":(timezone.now()+timedelta(days=1)).isoformat()},format="json")
  self.assertEqual(r.status_code,status.HTTP_201_CREATED); self.assertEqual(Booking.objects.count(),1); self.assertEqual(Booking.objects.first().user,self.user)
 def test_booking_list_requires_authentication(self):
  self.client.force_authenticate(user=None); r=self.client.get("/api/bookings/"); self.assertEqual(r.status_code,status.HTTP_401_UNAUTHORIZED)
class RegistrationTests(APITestCase):
 def test_registration_creates_user(self):
  r=self.client.post("/api/registration/",{"username":"newuser","password":"StrongPass123","email":"new@example.com"},format="json")
  self.assertEqual(r.status_code,status.HTTP_201_CREATED); self.assertTrue(User.objects.filter(username="newuser").exists())
