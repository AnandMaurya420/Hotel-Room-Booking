from django.shortcuts import render
from .models import Hotel,Room,Customer,Booking,Payment
from .serializers import hotel_serializer,customer_serializer,room_serializer,booking_serializer,payment_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.renderers import JSONRenderer



# Create your views here.   

@api_view(['POST'])
def hotel_register(request):
    if request.method == 'POST':

        serializer = hotel_serializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status':200, 'error':serializer.errors})
        serializer.save()
        return Response({'data':serializer.data, 'status':status.HTTP_201_CREATED})

    # return render (request, 'roombooking/hotel_register.html')

@api_view(['PUT'])
def hotel_update(request,id):

    # if request.method == 'POST':
        if id is not None:
            try:
                model_hotel = Hotel.objects.get(pk=id)
                serializer = hotel_serializer(model_hotel,data = request.data,partial = True)

                if not serializer.is_valid():
                    # return Response({'error':serializer.errors})
                    return Response({'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
                serializer.save()
            except Hotel.DoesNotExist:
                return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def hotel_delete(request,id):

    try:
        model_hotel = Hotel.objects.get(pk=id)
        model_hotel.delete()
        # return Response({'delete':'hotel delete sucessfully'})
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Hotel.DoesNotExist:
        return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def show_hotels(request,id=None):

    # if request.method == 'GET':
        if id is not None : 
            try:
                model_hotel = Hotel.objects.get(pk=id)
                serializers = hotel_serializer(model_hotel)  
                return Response({'status': 'success', "hotel":serializers.data}, status=200)
                # return render neede 
            except Hotel.DoesNotExist:
                return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            model_hotel = Hotel.objects.all()
            serializers = hotel_serializer(model_hotel,many = True)
            return Response({'data':serializers.data})
            # return render need

# ------------------- customer detail -----------------------------------

@api_view(['POST'])
def customer_register(request):

    serializer = customer_serializer(data = request.data)
    if not serializer.is_valid():
        return Response({'status':200, 'error':serializer.errors})
    serializer.save()
    return Response({'data':serializer.data, 'status':status.HTTP_201_CREATED})

@api_view(['PUT'])
def customer_update(request,id):

    if id is not None:
        try:
            model_hotel = Customer.objects.get(pk=id)
            serializer = customer_serializer(model_hotel,data = request.data,partial = True)

            if not serializer.is_valid():
                # return Response({'error':serializer.errors})
                return Response({'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
            serializer.save()
            return Response({'data':serializer.data})
        except Customer.DoesNotExist:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def customer_delete(request,id):

    try:
        model_hotel = Customer.objects.get(pk=id)
        model_hotel.delete()
        # return Response({'delete':'hotel delete sucessfully'})
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Hotel.DoesNotExist:
        return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def customer_get(request,id):

    if id is not None : 
        try:
            model_hotel = Customer.objects.get(pk=id)
            serializers = customer_serializer(model_hotel)  
            return Response({'status': 'success', "customer":serializers.data}, status=200)
            # return render neede 
        except Customer.DoesNotExist:
            return Response({'error': 'Hotel not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        model_hotel = Customer.objects.all()
        serializers = customer_serializer(model_hotel,many = True)
        return Response({'data':serializers.data})
            # return render need

# ----------------- room --------------------------

@api_view(['POST'])
def room_details(request):
    
    obj = request.data
    mydata = Room.objects.filter(room_number= obj['room_number'], hotel=obj['hotel']).exists()
    if mydata:
        return Response({'error': 'Room already exists'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = room_serializer(data = request.data)
    if not serializer.is_valid():
        return Response({'error':serializer.errors})
    serializer.save()
    return Response({'status': 'room Created'}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def room_update(request,id=None):

    if id is not None:
        try:
            model_room = Room.objects.get(pk=id)
            serializer = room_serializer(model_room,request.data,partial =True)
            if not serializer.is_valid():
                return Response({'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
            serializer.save()
            return Response({'data':serializer.data})
        except Room.DoesNotExist:
            return Response({'error': 'room not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'ID is required for update'}, status=status.HTTP_400_BAD_REQUEST)

def room_get(request,id=None):
        
        if id is not None:

            try:
                model_room = Room.objects.get(pk=id)
                serializer = room_serializer(model_room,many=True)
                return Response({'status': 'success', "customer":serializer.data}, status=200)
            except Room.DoesNotExist:
                return Response({'error':serializer.errors,'status':status.HTTP_404_NOT_FOUND})
        else:
            model_room = Room.objects.all()
            serializers = room_serializer(model_room,many = True)
            return Response({'data':serializers.data})

# ----------------------- booking ------------------

@api_view(['POST'])
def booking(request):

    sw = request.data

    # when you have foregien key where you want to save your data,then you have to be create instance
    customer_instance = Customer.objects.get(id=sw['customer'])
    print('-----booking_instance-------',customer_instance)

    customer = request.POST.get('customer')
    print('=======customer-----',customer)

    check_in_date = sw['check_in_date']
    check_out_date = sw['check_out_date']

    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(check_in_date, date_format)
    end_date = datetime.strptime(check_out_date, date_format)
    difference = end_date - start_date
    duration = difference.days
   
    price_for_room = Room.objects.get(id = sw['room']).price
    total_price = duration*price_for_room

    book = Booking.objects.filter(customer=sw['customer'],room = sw['room']).exists()
    if book:
        return Response({'data':'data already exist'})
   
    booking_data = Booking(customer = Customer.objects.get(id=sw['customer']),room = Room.objects.get(id=sw['room']),check_in_date = sw['check_in_date'],check_out_date = sw['check_out_date'],
                    total_price = total_price, status = sw['status'] )
    booking_data.save()
    return Response({'status':'booked','data':booking_data.data}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def payment(request):

    data = request.data
    booking_model = Booking.objects.get(id=data['booking'])
    print('amount---------',booking_model)

    payment = Payment.objects.get(booking = data['booking'])

    if payment.payment_status == True:
        print('payment-------------',payment.payment_status)
        return Response({'payment':' payment done '})
        

    else:
        payment_model = Payment(
        booking = Booking.objects.get(id=data['booking']), amount = booking_model.total_price, payment_date = booking_model.booking_date, 
        payment_method = data['payment_method'], transaction_id = data['transaction_id'],payment_status = data['payment_status']
        )
        print('=======>',payment_model.booking)

        payment_model.save()

        payment_data = Payment.objects.get(booking = data['booking'])
        print('===========',payment_data.payment_status)
        ('====paymentdata=====',payment_data)

        if payment_data.payment_status == True:
            booking = Booking.objects.get(id = data['booking'])
            booking.status = 'Confirmed'
            booking.save()
            # because of forregin key
            room = booking.room
            print('-------->',room.hotel)
            hotell = Hotel.objects.get(name = room.hotel)
            print(hotell.id)

            # room_update = Room.objects.filter(room_number = room.room_number, hotel = hotel.id)
            room_update = Room.objects.get(room_number = room.room_number, hotel = hotell.id)
            print('-----------roomupdate---------------',room_update)
            print('-------------->>>>>>>>>>',room_update.is_available)
            room_update.is_available = False
            room_update.save()
            return Response({'status':'booking status update'})
        else:
            return Response({'errors':'payment in progress'})