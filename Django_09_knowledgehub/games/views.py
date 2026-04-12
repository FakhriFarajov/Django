from django.shortcuts import render


def home(request):
	return render(request, "games/home.html")


def football(request):
	return render(request, "games/football.html")


def hockey(request):
	return render(request, "games/hockey.html")


def basketball(request):
	return render(request, "games/basketball.html")
