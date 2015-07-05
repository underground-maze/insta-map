from django.http import JsonResponse


def render_to_json(controller):
    """ decorator to return JsonResponse """
    def wrapper(request, *args, **kwargs):
        response, status = controller(request, *args, **kwargs)
        return JsonResponse(response, status=status)
    return wrapper
