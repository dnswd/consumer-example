from django.shortcuts import render
from user.models import User


@csrf_exempt
def index(request):
    if request.method == "GET":
        return render(request, 'home/index.html')
    elif request.method == "POST":
        data = request.POST
        queue = data.get("queue")
        callback = data.get("callback")
        user = User.objects.create(username=callback.split("/")[-1])
        user.save()
        return render(request, 'home/index.html', {"queue": queue, "callback": callback})
