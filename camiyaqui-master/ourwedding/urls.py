from django.urls import path
from django.views.generic import TemplateView

from ourwedding.views import index_forbidden, Index, GuestLogin, \
    GuestProfile, GuestAdd, CreateMessage, ViewMessages, \
    Contact, Register, UpdateGuestAjax, \
    EventView, SaveTheDateView, HelpView, GroupView, \
    AccommodationView, TangoView, BuenosAiresView, GuestList, WeddingView, PreWeddingView

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('login', GuestLogin.as_view(), name='guest-login'),
    path('register', Register.as_view(), name='guest-register'),
    path('me', GuestProfile.as_view(), name='guest-profile'),

    path('save-the-date', SaveTheDateView.as_view(), name='save-the-date'),

    path('code-sent', TemplateView.as_view(template_name='ourwedding/code-sent.html'), name='code-sent'),

    path('forbidden', index_forbidden, name='home-forbidden'),

    path('guest-list', GuestList.as_view(), name='guest-list'),

    path('rsvp', GroupView.as_view(), name='RSVP'),
    path('rsvp/add', GuestAdd.as_view(), name='guest-add'),

    path('messages', ViewMessages.as_view(), name='list-messages'),
    path('messages/new', CreateMessage.as_view(), name='create-message'),
    path('contact', Contact.as_view(), name='contact'),

    path('update-guest-ajax', UpdateGuestAjax.as_view(), name='update-guest-ajax'),
    path('event', EventView.as_view(), name='event'),
    path('event/wedding', WeddingView.as_view(), name='event-wedding'),
    path('event/pre-wedding', PreWeddingView.as_view(), name='event-pre-wedding'),
    path('buenosaires', BuenosAiresView.as_view(), name='buenosaires'),
    path('tango', TangoView.as_view(), name='tango'),
    path('accommodation', AccommodationView.as_view(), name='accommodation'),
    path('help', HelpView.as_view(), name='help'),
]
