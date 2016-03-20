from django.shortcuts import render
from django.core.mail import send_mail
from .forms import contactForm
from django.conf import settings

# Create your views here.
def about(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        print request.POST
        print form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        subject = 'Message from LeThaiCuisine.com'
        message = '{} {}'.format(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER, form.cleaned_data['email']]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks"
        confirm_message = "Thanks for the message"
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = "contact.html"
    return render(request, template, context)