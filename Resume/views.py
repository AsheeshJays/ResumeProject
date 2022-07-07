from django.shortcuts import render, HttpResponseRedirect
from Resume.models import Contact
from django.core.mail import send_mail,send_mass_mail


def Index(request):
    return render(request, 'index.html')



def skill(request):
    context = {'skill':'active'}
    return render(request, 'skill.html',context)

def services(request):
    context = {'services':'active'}
    return render(request, 'services.html',context)

def education(request):
    context = {'education':'active'}
    return render(request, 'education.html',context)

def contact(request):
    if request.method == 'POST':
        c = Contact()
        c.name = request.POST.get('name')
        c.email = request.POST.get('email')
        c.subject = request.POST.get('subject')
        c.message = request.POST.get('message')
        subject = "For Contact"
        body =  """
                    Hello!!!!
                    Thanks For Beleving me .
                    Me & My Team   will conact
                     very Soon 

                    Team:  Asheesh
                """
        send_mail(subject, body,"armannmalik9880@gmail.com",[c.email,], fail_silently=False)
        c.save()
        return HttpResponseRedirect("/")
    context = {'contact':'active'}
    return render(request, 'contact.html',context)
