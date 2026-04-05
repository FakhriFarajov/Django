import random
from django.http import HttpResponse

def quotes(request):
    lst = ["quote1", "quote2", "quote3", "quote4"]
    return HttpResponse(lst[random.randint(0, len(lst)-1)])