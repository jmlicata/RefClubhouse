from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField




class Member(AbstractUser):
    
    class MemberLevels(models.TextChoices):
        NON_OFFICIAL = 'NON-OFFICIAL', 'Non-Official'
        CANDIDATE = 'CANDIDATE', 'Candidate'
        JUNIOR = 'JUNIOR', 'Junior'
        MIDDLE_SCHOOL = 'MIDDLE_SCHOOL', 'Middle School'
        JV = 'JUNIOR_VARSITY', 'Junior Varsity'
        VARSITY = 'VARSITY', 'Varsity'

    class MemberStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        INACTIVE = 'INACTIVE', 'Inactive'
        RETIRED = 'RETIRED', 'Retired'
        EMERITUS = 'EMERITUS' 'Emeritus'
    
    level = models.CharField(max_length = 20, choices = MemberLevels.choices, default = MemberLevels.CANDIDATE)
    status = models.CharField(max_length = 20, choices = MemberStatus.choices, default = MemberStatus.ACTIVE)
    
    def __str__(self):
        return self.get_full_name()
    

class Address(models.Model):

    class AddressTypes(models.TextChoices):
        HOME_ADDRESS = 'HOME', 'Home'
        WORK_ADDRESS = 'WORK', 'Work'
        ALT_ADDRESS = 'ALT', 'Alternate'

    default = models.BooleanField(default = False)
    type = models.CharField(max_length = 4, choices = AddressTypes.choices, default = AddressTypes.HOME_ADDRESS)
    street = models.CharField(max_length = 25)
    city = models.CharField(max_length = 25)
    state = models.CharField(max_length = 2)
    zip = models.CharField(max_length = 10)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)

    def __str__(self):
        return self.get_type_display()

class Phone(models.Model):

    class PhoneTypes(models.TextChoices):
        MOBILE_PHONE = 'MOBILE', 'Mobile'
        HOME_PHONE = 'HOME', 'Home'
        WORK_PHONE = 'WORK', 'Work'
        OTHER_PHONE = 'OTHER', 'Other'

    default = models.BooleanField(default = False)
    type = models.CharField(max_length = 10, choices = PhoneTypes.choices, default = PhoneTypes.MOBILE_PHONE )
    number = PhoneNumberField(blank=False)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)

    
    def __str__(self):
        return self.get_type_display()


class Season(models.Model):

    name = models.CharField(blank = False, max_length = 25)
    start_date = models.DateField(blank = True)
    end_date = models.DateField(blank = True)

    def __str__(self) -> str:
        return self.name

class Payment(models.Model):

    class PaymentTypes(models.TextChoices):

        CHECK = 'CHECK', 'Check'
        CASH = 'CASH', 'Cash'
        EFT = 'EFT', 'Electronic Funds Transfer'

    class PaymentReason(models.TextChoices):

        DUES = 'DUES', 'Dues'
        FINE = 'FINE', 'Fines'
        GIFT = 'GIFT', 'Gift'
        OTHER = 'OTHER', 'Other'     

    reason = models.CharField(max_length = 5, choices = PaymentReason.choices, default = PaymentReason.DUES)
    type = models.CharField(max_length = 5, choices = PaymentTypes.choices, default = PaymentTypes.CHECK)
    payment_date = models.DateField(blank = False)
    amount = models.DecimalField(blank = False, max_digits=8, decimal_places=2)
    notes = models.CharField(max_length = 255)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    season = models.ForeignKey(Season, on_delete = models.SET_NULL, blank = True, null = True)

    def __str__(self) -> str:
        return f'{self.member.get_full_name} - {self.get_reason_display} - {self.amount}'

class Documentation(models.Model):

    class DocumentationType(models.TextChoices):

        EXAM = 'EXAM', 'Examination Results'
        CREDENTIALS = 'CRED', 'Credentials' 
        OTHER = 'OTHER', 'Other'

    type = models.CharField(max_length = 5,  choices = DocumentationType.choices, default = DocumentationType.OTHER)
    date = models.DateField()
    notes = models.CharField(max_length = 255)
    approved = models.BooleanField(blank = False, default = False)
    member = models.ForeignKey(Member, on_delete = models.CASCADE)
    season = models.ForeignKey(Season, on_delete = models.SET_NULL, blank = True, null = True)


