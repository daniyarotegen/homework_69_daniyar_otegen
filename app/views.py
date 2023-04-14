from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def validate_input(data):
    if "A" not in data or "B" not in data:
        return False, "Both 'A' and 'B' must be provided."
    if not isinstance(data["A"], (int, float)) or not isinstance(data["B"], (int, float)):
        return False, "Both 'A' and 'B' must be numbers."
    return True, ""


@csrf_exempt
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_valid, message = validate_input(data)
        if not is_valid:
            return JsonResponse({"error": message}, status=400)
        result = data["A"] + data["B"]
        return JsonResponse({"answer": result})
    return JsonResponse({"error": "Only POST method is allowed."}, status=400)


@csrf_exempt
def subtract(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_valid, message = validate_input(data)
        if not is_valid:
            return JsonResponse({"error": message}, status=400)
        result = data["A"] - data["B"]
        return JsonResponse({"answer": result})
    return JsonResponse({"error": "Only POST method is allowed."}, status=400)


@csrf_exempt
def multiply(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_valid, message = validate_input(data)
        if not is_valid:
            return JsonResponse({"error": message}, status=400)
        result = data["A"] * data["B"]
        return JsonResponse({"answer": result})
    return JsonResponse({"error": "Only POST method is allowed."}, status=400)


@csrf_exempt
def divide(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_valid, message = validate_input(data)
        if not is_valid:
            return JsonResponse({"error": message}, status=400)
        if data["B"] == 0:
            return JsonResponse({"error": "Division by zero!"}, status=400)
        result = data["A"] / data["B"]
        return JsonResponse({"answer": result})
    return JsonResponse({"error": "Only POST method is allowed."}, status=400)
