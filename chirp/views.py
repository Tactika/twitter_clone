from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponseRedirect

# Importing Chirp Model Class
from .models import Chirp

# Import Create Chirp Form Class
from .forms import NewChirp

# Decorators
from django.contrib.auth.decorators import login_required

# Create your views here.

# Index View
def index(request,*args, **kwargs): 
    chirps = Chirp.objects.all()

    context = {
        'chirps': chirps,
    }
    return render(request, 'index.html', context)

# Display All Chirps
def all_chirps(request,*args, **kwargs):
    chirps = Chirp.objects.order_by('-user')
    context = {
        'chirps': chirps,
    }
    return render(request, 'index.html', context)

# Display All Chirps
def user_chirp(request, *args, **kwargs):
    current_user = request.get_current_user
    chirps = Chirp.objects.filter_by('-id')
    context = {
        'chirps': chirps,
        'current_user': current_user,
    }
    return render(request, 'feed.html', context)

# Create New Chirp
@login_required
def new_chirp(request, *args, **kwargs):
    chirp = NewChirp(request.POST or None)

    if chirp.is_valid():
        chirp.save()

    return HttpResponseRedirect(reverse('chirp:new_chirp'))

def like(request, pk, **kwargs):
    chirp = get_object_or_404(Chirp, id=request.POST.get('like'))
    chirp.likes.add(request.user)
    chirp.save()
    return HttpResponseRedirect(reverse('chirp:index'))
