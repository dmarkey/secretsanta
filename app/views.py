from django.shortcuts import render, get_object_or_404
from models import SecretSantaOrg
from forms import NewSecretSantaForm

# Create your views here.


def launch(request):
    if request.POST:
        form = NewSecretSantaForm(request.POST)
    else:
        form = NewSecretSantaForm()

    return render(request, "launch.html", {"form": form, "layout": "vertical" })

def manage(request, org_id):
    org = get_object_or_404(SecretSantaOrg, key=org_id)

