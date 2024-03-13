from django.http import HttpResponse
from django.http import JsonResponse
from .models import Game
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST":
        received_data = json.loads(request.body).get("data")
        data = Game.dataFormat(received_data)
        if data['status'] == 'error':
            return JsonResponse(data)

        response = Game.queensAttack(
            data['n'], data['k'], data['rq'], data['cq'], data['obstacles'])
        return HttpResponse(json.dumps(response))
    else:
        return JsonResponse({"error": "Only POST requests are allowed"})
