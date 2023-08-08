from django.http import JsonResponse


def contact_form(request):
    context = {
        'success': False,
        'message': 'Contact form sent successfully.'
    }
    return JsonResponse(context)
# Create your views here.
