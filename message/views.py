from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from appartement.models import Appartement
from .models import Conversation, Message




def envoyer_message(request):
    
    conversation = Conversation.objects.first()

    if request.method == "POST":
        contenu = request.POST.get("contenu")

        Message.objects.create(
            conversation=conversation,
            expediteur=request.user,
            contenu=contenu
        )

    return render( request, "messages.html")


@login_required
def creer_conversation(request, logement_id):

    logement = get_object_or_404(Appartement, id=logement_id)

    # vérifier si conversation existe déjà
    conversation, created = Conversation.objects.get_or_create(
        logement=logement,
        locataire=request.user,
        proprietaire=logement.proprietaire
    )

    return redirect('voir_conversation', conversation_id=conversation.id)


@login_required
def voir_conversation(request, conversation_id):

    conversation = get_object_or_404(Conversation, id=conversation_id)

    messages = conversation.messages.all().order_by('date_envoi')

    if request.method == 'POST':
        contenu = request.POST.get('contenu')

        Message.objects.create(
            conversation=conversation,
            expediteur=request.user,
            contenu=contenu
        )

        return redirect('voir_conversation', conversation_id=conversation.id)

    return render(request, 'conversation.html', {
        'conversation': conversation,
        'messages': messages
    })


@login_required
# message/views.py

def liste_conversations(request):
    # On récupère les conversations où l'utilisateur est soit le locataire, soit le proprio
    # Ajuste 'locataire' et 'proprietaire' selon tes noms de champs dans ton modèle Conversation
    conversations = Conversation.objects.filter(
        Q(locataire=request.user) | Q(proprietaire=request.user)
    ).order_by('-last_message_date') 
    
    return render(request, 'liste_conversation.html', {'conversations': conversations})
# Create your views here.
