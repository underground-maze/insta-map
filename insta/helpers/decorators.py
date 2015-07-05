from django.http import JsonResponse


def render_to_json(controller):
    """ decorator to return JsonResponse """
    def wrapper(request, *args, **kwargs):
        response, status = controller(request, *args, **kwargs)
        return JsonResponse(response, status=status)
    return wrapper


def ajax(controller):
    """ decorator to disallow not ajax request """
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return dict(result='errors'), 400
        return controller(request, *args, **kwargs)
    return wrapper
