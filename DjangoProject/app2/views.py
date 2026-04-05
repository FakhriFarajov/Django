from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def week_day(request):
    day = datetime.now().strftime("%A")
    return HttpResponse(f"Today is: {day}")
