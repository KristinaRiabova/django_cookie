from django.http import JsonResponse


def set_cookie(request):
    name = request.GET.get('name')
    value = request.GET.get('value')
    http_only = bool(request.GET.get('httpOnly', False))

    response = JsonResponse({'name': name, 'value': value, 'httpOnly': http_only, 'message': 'Cookie set successfully'})
    response.set_cookie(name, value, httponly=http_only)
    return response


def get_cookie(request, name):
    cookie_value = request.COOKIES.get(name, 'Cookie not found')
    return JsonResponse({'name': name, 'value': cookie_value})


def set_header(request):
    name = request.GET.get('name')
    value = request.GET.get('value')

    response = JsonResponse({'name': name, 'value': value, 'message': 'Header set successfully'})
    response[name] = value
    return response

def get_header(request):
    name = request.GET.get('name')
    header_value = request.headers.get(name, 'Header not found')
    return JsonResponse({name: header_value})

