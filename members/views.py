from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Member 
from .forms import MemberForm


# Create your views here.
def index(request):

    member_list = Member.objects.all()

    Member.

    return render(request, 'index.html', {'member_list' : member_list})

    
def member_edit(request):

    if request.method == 'POST':
        form = MemberForm(request.POST)
        return HttpResponseRedirect('/')
    else:
        form = MemberForm()

    return render(request, 'member.html', {'form' : form})    