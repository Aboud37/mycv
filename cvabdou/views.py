from django.core.mail import send_mail
from django.shortcuts import render
from .models import *


def index(request):
    abouts = About.objects.all
    pros = ProfessionalSkills.objects.all
    works = WorkExperience.objects.all
    educations = Education.objects.all
    certifications = Certification.objects.all

    if request.method == 'POST':
        name = request.POST['name']
        replyto = request.POST['replyto']
        message = request.POST['message']

        send_mail(
            name,
            replyto,
            message,
            ['abdou371992@gmail.com'],

        )

    context = {'abouts':abouts, 'pros': pros, 'works':works, 'educations':educations, 'certifications':certifications }
    return render(request, 'cv/index.html',context)
