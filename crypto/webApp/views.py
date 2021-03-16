from django.shortcuts import render

# Homepage
def home(request):
    return render(request, 'webApp/index.html')
