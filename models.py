from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='destinations/', null=True, blank=True)

    def __str__(self):
        return self.name


DESTINATION_CHOICES = [
    ('Goa', 'Goa'),
    ('Ooty', 'Ooty'),
    ('Munnar', 'Munnar'),
    ('Kodaikanal', 'Kodaikanal'),
    ('Kerala','Kerala'),
    ('Delhi','Delhi'),
    ('Bengalore','Bengalore'),
    ('Kolkata','Kolkata'),
]

BUS_TYPES = [
    ('AC Sleeper', 'AC Sleeper'),
    ('AC Seater', 'AC Seater'),
    ('Non AC Sleeper', 'Non AC Sleeper'),
    ('Non AC Seater', 'Non AC Seater'),
]

FOOD_TYPES = [
    ('Veg', 'Veg'),
    ('Non-Veg', 'Non-Veg'),
    ('Both', 'Both'),
]

BUDGET_CHOICES = [
    ('<10000', 'Below ₹10,000'),
    ('10000-20000', '₹10,000 - ₹20,000'),
    ('20000-30000', '₹20,000 - ₹30,000'),
    ('>30000', 'Above ₹30,000'),
]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=50, choices=DESTINATION_CHOICES)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()
    bus_type = models.CharField(max_length=50, choices=BUS_TYPES)
    food_type = models.CharField(max_length=50, choices=FOOD_TYPES)
    budget = models.CharField(
    max_length=50,
    choices=BUDGET_CHOICES,
    blank=True,
    null=True
)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination} ({self.guests} guests)"

# ============================
# CONTACT MODEL
# ============================
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"

class Package(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)  # e.g., "3 Days / 2 Nights"
    image = models.ImageField(upload_to='packages/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, blank=True)  # Bootstrap Icon name
    description = models.TextField()

    def __str__(self):
        return self.title  

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"  