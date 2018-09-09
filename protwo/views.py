from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from protwo.models import User
from .forms import UserForm






# Create your views here.

def index(request):
    now = timezone.now()
    my_dict = {
        'now': now
    }
    return render(request, 'protwo/index.html', context=my_dict)


def users(request):
    all_users = User.objects.all()
    return render(request, 'protwo/users.html', {'all_users': all_users})


def user_new(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            return redirect('user_detail', pk=user.pk)
        else:
            print('ERROR Form Invalid')
    else:
        form = UserForm()
    return render(request, 'protwo/user_new.html', {'form': form})


'''



def user_new(request):
    form = UserForm()
    return render(request, 'protwo/user_edit.html', {'form': form})
    
    
'''




def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'protwo/user_detail.html', {'user': user})


def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            user = form.save(commit=False)
            user.date_modify = timezone.now()
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'protwo/user_edit.html', {'form': form})



