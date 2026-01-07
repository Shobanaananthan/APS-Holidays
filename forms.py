from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from agency.models import Destination  
from django.db import models
from .models import Booking, DESTINATION_CHOICES, BUS_TYPES, FOOD_TYPES, BUDGET_CHOICES
from .models import Review

DESTINATIONS = [
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

class BookingForm(forms.ModelForm):
    destination = forms.ChoiceField(choices=DESTINATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    bus_type = forms.ChoiceField(choices=BUS_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))
    food_type = forms.ChoiceField(choices=FOOD_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))
    budget = forms.ChoiceField(choices=BUDGET_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    checkin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    guests = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Booking
        fields = ['destination', 'checkin', 'checkout', 'guests', 'bus_type', 'food_type', 'budget']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # hash password
        if commit:
            user.save()
        return user


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, "★☆☆☆☆"),
        (2, "★★☆☆☆"),
        (3, "★★★☆☆"),
        (4, "★★★★☆"),
        (5, "★★★★★")
    ]

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = ['name', 'rating', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }            