from django.shortcuts import render
from django.contrib import messages
from .models import ContactMessage
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

def my_view(request):
    # Exemple de logique de vue :
    context = {
        'message': 'Bienvenue sur Versatile Design!',
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sender_email = request.POST.get('email')

        # Envoi d'un e-mail (exigera une configuration SMTP dans les paramètres Django)
        # Commentez cette partie pour le moment
        # send_mail(
        #     subject,
        #     message,
        #     sender_email,
        #     ['votre_email@example.com'],  # Remplacez par votre adresse e-mail
        #     fail_silently=False,
        # )

        # Créez une nouvelle instance du modèle ContactMessage et enregistrez-la dans la base de données
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_message = ContactMessage(nom=nom, email=email, message=message)
        contact_message.save()

        # Enregistrez un message flash
        messages.success(request, 'Demande bien envoyée.')

        # Redirigez l'utilisateur vers la page contact.html
        # return JsonResponse({'success': True})

    return render(request, 'contact.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signup')  # Rediriger vers la page de connexion après l'inscription
