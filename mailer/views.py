import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            subject = f"Portfolio - wiadomość od: {data.get('name')}"
            message = f"Nadawca: {data.get('name')} ({data.get('email')})\n\n{data.get('message')}"

            send_mail(
                subject,
                message,
                'kulak.jan0@gmail.com',
                ['kulak.jan0@gmail.com'],
                fail_silently=False,
            )

            send_mail(
                "Potwierdzenie kontaktu",
                "Dziękuję za kontakt, wiadomość została odebrana i odpowiem na nią jak najszybciej.\nZ poważaniem\nJan Kulak",
                "kulak.jan0@gmail.com",
                [data.get('email')],
                fail_silently=False,
            )

            return JsonResponse({'status': 'success'})
        except Exception as e:
            # w przypadku błędu wypisz go
            print(e)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error'}, status=405)