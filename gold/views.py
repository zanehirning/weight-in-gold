from django.shortcuts import render


def index(request):
    template_name = "gold/index.html"
    return render(request, template_name)

def plan(request):
    template_name = "gold/plan.html"
    return render(request, template_name)
# Create your views here.
