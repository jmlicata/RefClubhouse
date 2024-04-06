from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from  .models import Member, Address, Phone, Season

class MemberAddressAdminInline(admin.StackedInline):
    model =Address
    extra = 0
    verbose_name = 'Address'
    verbose_name_plural = 'Addresses'

class MemberPhoneAdminInline(admin.StackedInline):
    model = Phone
    extra = 0
    verbose_name = 'Phone Number'
    verbose_name_plural = 'Phone Numbers'

class MemberAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'last_name', 'first_name', 'email', 'status')
    
    fieldsets = UserAdmin.fieldsets + (
    ('Member Details', {'fields': ('level','status')}),)

    inlines = (MemberAddressAdminInline, MemberPhoneAdminInline)

admin.site.register(Member, MemberAdmin)

class SeasonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Season, SeasonAdmin)


