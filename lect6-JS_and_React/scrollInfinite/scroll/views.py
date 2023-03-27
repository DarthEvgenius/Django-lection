from django.shortcuts import render
import time
from django.http import JsonResponse

# Create your views here.
def index(request):
	return render(request, 'scroll/index.html')


def posts(request):
	""" Generates posts and return them in JSON """

	# Get start/end indexes of posts (or create them)
	# Convert them to int
	start = int(request.GET.get("start") or 0)
	end = int(request.GET.get("end") or start + 9)

	# Create and populate a list of posts
	data = []
	# Take 'end+1' as 'range' doesn't include finish index
	for i in range(start, end + 1):
		data.append(f"Post {i}")

	# Delay speed of response to fell the loading of new posts
	time.sleep(1)

	# Return list of posts as JSON
	# Import JsonResponse
	return JsonResponse({
		"posts": data
	})