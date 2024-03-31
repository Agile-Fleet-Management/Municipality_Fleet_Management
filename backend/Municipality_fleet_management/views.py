from django.http import HttpResponse

def home(request):
    return HttpResponse('App is deployed for the demo')
