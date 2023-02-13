from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Imports for atntications
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))

	# If we have a valid user
	return render(request, "users/user.html")

# User's passwords: pass0000
def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		# Checking the inputed name/pass
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "users/login.html", {
				"message": "Invalid credentials"
			})

	return render(request, "users/login.html")


def logout_view(request):
	logout(request)
	return render(request, "users/login.html", {
		"message": "Logged out"
	})