from django.shortcuts import render
from django.http import HttpResponse
from user.models import User, Message
from asgiref.sync import sync_to_async, async_to_sync
import asyncio
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request, name):
    if (request.method == "GET"):
        user = User.objects.get(username=name)
        messages = Message.objects.filter(user=user)
        return render(request, 'user/index.html', {"user": user, "msg": messages})
    elif (request.method == "POST"):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        async_result = loop.run_until_complete(createMessage(request=request, name=name))
        loop.close()
        return HttpResponse("User created")

async def createMessage(request, name):
    data = json.loads(request.body)
    user = await sync_to_async(User.objects.get)(username=name)
    topic = data["topic"]
    message = data["message"]
    message = await sync_to_async(Message.objects.create)(user=user, topic=topic, message=message)
    await sync_to_async(message.save)()
    return HttpResponse("Message created")