from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Billet

def post_list(request):
    billets = Billet.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'billets': billets })
# Create your views here.
def post_detail(request, pk):
    billet = get_object_or_404(Billet, pk=pk)
    return render(request, 'blog/post_detail.html', {'billet': billet})

