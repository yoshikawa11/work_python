from django.http import HttpResponse

def helloworldfunction(request):
    returnobject = HttpResponse('hello world')
    return returnobject