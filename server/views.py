from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

def run(request):
    if request.method== "POST":
        json_data = json.loads(request.body.decode())
        try:
            course= json_data['course']
            teamcode= json_data['teamcode']
            host= json_data['host']
            return JsonResponse({'success':1})
        except KeyError:
            return JsonResponse({'success':0})
