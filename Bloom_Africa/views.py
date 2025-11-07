from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import VolunteerSerializers, PartnershipSerializers, DonationSerializers, ContactsSerializers
from .models import Volunteer, Partnerships, Donations, Contacts

@api_view(['POST'])
def volunteerView(request):
    serializers = VolunteerSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message' : 'Data Submitted Successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def volunteerList(request):
    volunteer = Volunteer.objects.all().order_by('-created_at')
    serializers = VolunteerSerializers(volunteer, many=True, context={'request' : request})
    return Response(serializers.data)


@api_view(['POST'])
def partnershipView(request):
    serializers = PartnershipSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message' : 'Partnership data submitted Successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializers.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def partnerships_list(request):
    partnerships = Partnerships.objects.all()
    serializers = PartnershipSerializers(partnerships, many=True, context={'request' : request})
    return Response(serializers.data)

@api_view(['POST'])
def donationViews(request):
    serializers = DonationSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message' : 'Donations data submitted successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def donationList(request):
    donations = Donations.objects.all().order_by('-created_at')
    serializers = DonationSerializers(donations, many=True, context={'request' : request})
    return Response(serializers.data)

@api_view(['POST'])
def contacts(request):
    serializers = ContactsSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message' : 'Message sent successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def contacts_list(request):
    contact = Contacts.objects.all()
    serializer = ContactsSerializers(contact, many=True, context={'request' : request})
    return Response(serializer.data)

