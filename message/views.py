"""
Messaging and Conversation Views
Handles real-time messaging between tenants and property owners.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from appartement.models import Appartement
from .models import Conversation, Message


@login_required
def envoyer_message(request):
    """
    Display messaging interface and handle message posting.
    Lists all active conversations ordered by recent activity.
    """
    conversations = (
        Conversation.objects.filter(Q(locataire=request.user) | Q(proprietaire=request.user))
        .select_related('logement', 'locataire', 'proprietaire')
        .annotate(last_message_date=Max('messages__date_envoi'))
        .order_by('-last_message_date', '-date_creation')
    )

    if request.method == "POST":
        conversation_id = request.POST.get('conversation_id')
        contenu = request.POST.get('contenu', '').strip()
        if conversation_id and contenu:
            conversation = get_object_or_404(Conversation, id=conversation_id)
            Message.objects.create(
                conversation=conversation,
                expediteur=request.user,
                contenu=contenu,
            )
            return redirect('voir_conversation', conversation_id=conversation.id)

    return render(request, "messages.html", {
        'conversations': conversations,
    })


@login_required
def creer_conversation(request, logement_id):
    """
    Create or retrieve existing conversation for an apartment.
    Ensures conversation exists before redirecting to view.
    """
    logement = get_object_or_404(Appartement, id=logement_id)

    conversation, created = Conversation.objects.get_or_create(
        logement=logement,
        locataire=request.user,
        proprietaire=logement.proprietaire
    )

    return redirect('voir_conversation', conversation_id=conversation.id)


@login_required
def voir_conversation(request, conversation_id):
    """
    Display full conversation thread with all messages.
    Handles new message posting for current conversation.
    """
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
def liste_conversations(request):
    """
    Display all conversations for current user.
    Shows both as tenant and property owner.
    """
    conversations = (
        Conversation.objects.filter(Q(locataire=request.user) | Q(proprietaire=request.user))
        .select_related('logement', 'locataire', 'proprietaire')
        .annotate(last_message_date=Max('messages__date_envoi'))
        .order_by('-last_message_date', '-date_creation')
    )

    return render(request, 'liste_conversation.html', {'conversations': conversations})
