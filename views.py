from django.shortcuts import render, redirect
from .models import Destination, Booking
from .forms import BookingForm, ContactForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404

def home(request):
    destinations = Destination.objects.all()  # Show destinations to all users
    return render(request, 'agency/home.html', {'destinations': destinations})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'agency/login.html', {'form': form})

@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Redirect to success page
            return redirect('booking_success')
    else:
        form = BookingForm()

    user_bookings = Booking.objects.filter(user=request.user).order_by('-id')

    return render(request, 'agency/booking.html', {
        'form': form,
        'user_bookings': user_bookings
    })
@login_required
def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Your booking was successful!")  # success message
            return redirect('booking')  # reload page to show message
    else:
        form = BookingForm()

    # Get only bookings of the logged-in user
    user_bookings = Booking.objects.filter(user=request.user).order_by('-id')

    context = {
        'form': form,
        'user_bookings': user_bookings
    }
    return render(request, 'agency/booking.html', context)

def booking_success(request):
    return render(request, 'agency/booking_success.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'agency/contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'agency/register.html', {'form': form})

def packages(request):
    return render(request, 'agency/packages.html')

def services(request):
    return render(request, 'agency/services.html')

def tariff(request):
    return render(request, 'agency/tariff.html')

def reviews(request):
    all_reviews = Review.objects.order_by('-created_at')

    # Count rating stats
    rating_stats = {
        5: Review.objects.filter(rating=5).count(),
        4: Review.objects.filter(rating=4).count(),
        3: Review.objects.filter(rating=3).count(),
        2: Review.objects.filter(rating=2).count(),
        1: Review.objects.filter(rating=1).count(),
    }

    # Form handling
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    return render(request, 'agency/reviews.html', {
        'form': form,
        'reviews': all_reviews,
        'rating_stats': rating_stats,
    })

def reviews(request):
    if request.method == "POST":
        Review.objects.create(
            name=request.POST['name'],
            rating=request.POST['rating'],
            message=request.POST['message']
        )
        return redirect('reviews')

    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'agency/reviews.html', {'reviews': reviews})
# Admin-only delete review
@user_passes_test(lambda u: u.is_superuser)
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('reviews')


@user_passes_test(lambda u: u.is_superuser)
def delete_review(request, id):
    Review.objects.get(id=id).delete()
    return redirect('reviews')

def destinations(request):
    all_destinations = Destination.objects.all()
    return render(request, 'agency/destinations.html', {'destinations': all_destinations})