from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect("contacts:contact_success")
    else:
        form = ContactForm()
    return render(request, "contacts/contact.html", {"form": form})

def contact_success_view(request):
    return render(request, "contacts/contact_success.html")
