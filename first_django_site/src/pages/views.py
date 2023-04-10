from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is some text about us",
        "my_number": 123,
        "boolean": True,
        "my_list": [13,34,631,6424]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    # return render(request, "social.html", {})
    return HttpResponse("<h1>Social Page</h1>")