from rest_framework import serializers
from .models import *

class VolunteerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"

class PartnershipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partnerships
        fields = "__all__"

class DonationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = "__all__"

class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"