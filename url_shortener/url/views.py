from django.shortcuts import render, redirect
from url.forms import URL_Form
from url.models import URL

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        form = URL_Form(request.POST)
        if form.is_valid():
            new_url = form.save()
            request.session['new_object_id'] = new_url.id
            return redirect('index')
    if 'new_object_id' in request.session:
        session_object = URL.objects.get(pk=request.session['new_object_id'])
        context.update({'session_object': session_object})
    form = URL_Form
    context.update({'form': form})
    return render(request, 'url/index.html', context)

def page_redirect(request, number):
    redirect_url = URL.objects.get(pk=number).user_url
    return redirect(redirect_url)