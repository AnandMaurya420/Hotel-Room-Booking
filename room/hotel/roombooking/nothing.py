# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Hotel, Booking
# from .forms import BookingForm

# def hotel_list(request):
#     hotels = Hotel.objects.all()
#     return render(request, 'hotel_list.html', {'hotels': hotels})

# def hotel_detail(request, hotel_id):
#     hotel = get_object_or_404(Hotel, id=hotel_id)
#     return render(request, 'hotel_detail.html', {'hotel': hotel})

# def booking_list(request):
#     bookings = Booking.objects.all()
#     return render(request, 'booking_list.html', {'bookings': bookings})

# def book_room(request, room_id):
#     room = get_object_or_404(Room, id=room_id)
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.room = room
#             booking.save()
#             return redirect('booking_list')
#     else:
#         form = BookingForm()
#     return render(request, 'book_room.html', {'form': form, 'room': room})


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.hotel_list, name='hotel_list'),
#     path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
#     path('book/<int:room_id>/', views.book_room, name='book_room'),
#     path('bookings/', views.booking_list, name='booking_list'),
# ]