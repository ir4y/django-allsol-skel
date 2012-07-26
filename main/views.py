# Create your views here.
from django.views.generic.simple import direct_to_template

def main_view(request):
    return direct_to_template(request,"base.html")