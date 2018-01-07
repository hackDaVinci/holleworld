from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponse(reversed('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponse(reversed('learning_logs:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)