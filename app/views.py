from django.shortcuts import render, get_object_or_404, redirect
from models import SecretSantaOrg
from forms import NewSecretSantaForm, RegisterForm
from django.core.urlresolvers import reverse

# Create your views here.


def manageorg(request, unique_id):
    org= get_object_or_404(SecretSantaOrg, unique_id=unique_id)
    pass

def manageuser(request, unique_id):
    org= get_object_or_404(SecretSantaOrg, unique_id=unique_id)
    pass


def launch(request):
    if request.POST:
        form = NewSecretSantaForm(request.POST)
        if form.is_valid():
            org = form.save()
            return redirect("register", unique_id=org.unique_id);
    else:
        form = NewSecretSantaForm()

    return render(request, "launch.html", {"form": form, "layout": "vertical" })

def register(request, unique_id):
    org= get_object_or_404(SecretSantaOrg, unique_id=unique_id)
    if request.POST:
        form = RegisterForm(request.POST)
        form.set_org(org)
        if form.is_valid():
            org.add_participant(form.cleaned_data['your_email'])

    else:
        form = RegisterForm()
    return render(request, "list.html", {"form": form, "layout": "vertical", "org" : org })




