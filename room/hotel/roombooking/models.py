from django.db import models

# Create your models here.


# STATUS = [
#     ("Pending","Pending"),
#     ("Approved","Approved"),
#     ("Rejected","Rejected")
# ]

# GENDER = [
#     ('Male','Male'),
#     ('Female','Female'),
#     ('other','other')
# ]

# CITY = [
#     ('Ahmedabad','Ahmedabad'),
#     ('Surat','Surat'),
#     ('Vadodara','Vadodara'),
#     ('Rajkot','Rajkot')
# ]

# ID_PROOF = [
#     ('Aadhar','Aadhar'),
#     ('Pan card','Pan card')
# ]


# class guest_detail(models.Model):

#     name = models.CharField(max_length=20)
#     gender = models.CharField(max_length=15,choices=GENDER)
#     age = models.IntegerField(max_length=2)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=10)
#     city = models.CharField(max_length=30,choices=CITY)
#     state = models.CharField(max_length=30,default='Gujarat')
#     address = models.CharField(max_length=200)
#     pincode = models.IntegerField(max_length=6)
#     id_proof = models.FileField(upload_to ='uploads/',choices=ID_PROOF)


# HOTELS = [
#     ('Radhe krishn Hotel','Radhe krishn Hotel'),
#     ('Vaijanti Hotel','Vaijanti Hotel'),
#     ('Sadabahar Hotel','Sadabhar Hotel')
# ]

# ROOM_TYPE = [
#     ('Single BedRoom','Single BedrRoom'),
#     ('Double BedRoom','Double Bedroom')
# ]

# class Hotelt(models.Model):

#     choose_Hotel = models.CharField(max_length=50,choices=HOTELS)
#     room_type = models.CharField(max_length=50, choices= ROOM_TYPE)
#     price_for_single_bedroom = models.IntegerField(max_length=5,default=2000)
#     price_for_double_bedroom = models.IntegerField(max_length=5,default=2000)

# class Radhe_hotel(models.Model):




class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

ROOM_TYPE = [
    ('Single BedRoom','Single BedRoom'),
    ('Double BedRoom','Double Bedroom')
]

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50,choices=ROOM_TYPE)  # e.g., Single, Double, Suite
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.room_number} - {self.hotel.name}"

GENDER = [
    ('Male','Male'),
    ('Female','Female'),
    ('other','other')

]

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=15,choices=GENDER,default='Male')
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('in-progress', 'in-progress')
        # Add other statuses if needed
    ]

class Booking(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Confirmed')

    def __str__(self):
        return f"Booking {self.id} by {self.customer}"


PAYMENT_METHOD_CHOICES = [
    ('Credit Card', 'Credit Card'),
    ('Cash', 'Cash'),
    ('Online', 'Online'),
    # Add other payment methods if needed
]

PAYMENT_STATUS = [
    ('Done','Done'),
    ('Progress','Progress')
]

class Payment(models.Model):

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment {self.id} for Booking {self.booking.id}"