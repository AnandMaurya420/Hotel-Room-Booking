from rest_framework import serializers
from .models import Hotel,Room,Customer,Booking,Payment
from rest_framework.validators import UniqueValidator



class hotel_serializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = '__all__'
        
class customer_serializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class room_serializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'

        # extra_kwargs = {
        #         'room_number':{
        #             'validators':[
        #                 UniqueValidator(
        #                     queryset = Room.objects.all(),
        #                     message = ('Room number already exist')
        #                 )
        #             ]
        #         }
        #     }

class booking_serializer(serializers.ModelSerializer):

    room = room_serializer()
    customer = customer_serializer()

    class Meta:
        model = Booking
        fields = '__all__'

class payment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'