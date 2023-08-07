from django.http import JsonResponse


def contact_form(request):
    context = {'success': True,
               'message': 'Contact form sen successfully.'}
    return JsonResponse(context)
# Create your views here.
