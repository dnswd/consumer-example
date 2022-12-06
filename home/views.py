from django.shortcuts import render
from user.models import User
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests as req
@csrf_exempt
def index(request):
    if request.method == "GET":
        return render(request, 'home/index.html')
    elif request.method == "POST":
        data = json.loads(request.body)
        queue = data["queue"]
        consumer = {"consumer":data["consumer"]}
        response = req.post(queue, json=consumer)
        callback = data["consumer"]["url_callback"]
        user, is_create = User.objects.get_or_create(username=callback.split("/")[-1])
        if (is_create):
            user.save()
            print("User created")
        print("Finished")
        return JsonResponse(response.json(), safe=False)
