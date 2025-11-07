from django.db import models

class Volunteer(models.Model):
    PROGRAMS = [
        ('Education', 'Education'),
        ('Healthcare Outreach', 'Healthcare Outreach'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Environmental Sustainability', 'Environmental Sustainability'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    program = models.CharField(max_length=50, choices=PROGRAMS)
    relevant_experience = models.TextField()
    availability = models.CharField(max_length=100)
    reasons = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Volunteer by ({self.full_name}) on Program ({self.program})'

    class Meta:
        verbose_name = 'Volunteer',
        verbose_name_plural = 'Volunteer'


class Partnerships(models.Model):
    PROGRAMS = [
        ('Education', 'Education'),
        ('Healthcare Outreach', 'Healthcare Outreach'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Environmental Sustainability', 'Environmental Sustainability'),
    ]
    PartnerShip_Type = [
        ('Corporate Partnerships', 'Corporate Partnerships'),
        ('NGO Collaborations', 'NGO Collaborations'),
        ('Government Partnerships', 'Government Partnerships'),
        ('Academic Institutions', 'Academic Institutions'),
    ]
    organization_name = models.CharField(max_length=100)
    contacts_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    partnership_type = models.CharField(max_length=50, choices=PartnerShip_Type)
    program_type = models.CharField(max_length=50, choices=PROGRAMS)
    partnership_goals = models.TextField()
    values = models.TextField()
    preffered_timeline = models.CharField(max_length=50)
    def __str__(self):
        return f'Partnership by {self.organization_name} -- ({self.partnership_type})'
    class Meta:
        verbose_name = 'Partnerships'
        verbose_name_plural = 'Partnerships'

class Donations(models.Model):
    PROGRAMS = [
        ('Education', 'Education'),
        ('Healthcare Outreach', 'Healthcare Outreach'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Environmental Sustainability', 'Environmental Sustainability'),
    ]
    amount = models.IntegerField()
    program = models.CharField(max_length=100, choices=PROGRAMS)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    dedication = models.CharField(max_length=100)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f'Donations by ({self.first_name} {self.last_name}) -- Programs ({self.program})'
    class Meta:
        verbose_name = 'Donations'
        verbose_name_plural = 'Donations'


class Contacts(models.Model):
    Inquiry_Type = [
        ('Education', 'Education'),
        ('Healthcare Outreach', 'Healthcare Outreach'),
        ('Women Empowerment', 'Women Empowerment'),
        ('Environmental Sustainability', 'Environmental Sustainability'),
    ]
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    inquiry_type = models.CharField(max_length=255, choices=Inquiry_Type)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'Message from {self.full_name}'
    
    class Meta:
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'

