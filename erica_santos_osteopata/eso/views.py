from django.shortcuts import render, get_object_or_404
from .models import TextPresentation, Opinion, OsteopathyAbout, OsteopathyCase, OsteopathyHistory, AppointmentsDescription
from .backend import insert_calendar_event
import datetime

APPOINTMENT_DURATION_MIN = 60


def home_page(request):
    presentation_text = get_object_or_404(TextPresentation)
    opinions = Opinion.objects.filter(is_valid=True)
    context = {"presentation_text": presentation_text, "opinions": opinions}

    return render(request=request, template_name='eso/index.html', context=context)


def osteopathy_about_page(request):
    osteopathy_about = get_object_or_404(OsteopathyAbout)
    context = {"osteopathy_about": osteopathy_about}

    return render(request=request, template_name='eso/osteopathy_about_page.html', context=context)


def osteopathy_cases_page(request):
    osteopathy_cases = OsteopathyCase.objects.all() #Later change this to filter by valid cases only
    context = {"osteopathy_cases": osteopathy_cases}

    return render(request=request, template_name='eso/osteopathy_cases_page.html', context=context)


def osteopathy_history_page(request):
    osteopathy_history = get_object_or_404(OsteopathyHistory)
    context = {"osteopathy_history": osteopathy_history}

    return render(request=request, template_name='eso/osteopathy_history_page.html', context=context)


def scheduling_page(request):
    appointments_description = get_object_or_404(AppointmentsDescription)
    context = {"appointments_description": appointments_description}

    if request.method == "POST" and request.POST.get("form") == 'appointment':
        summary = "Consulta: " + request.POST.get("name") + " - " + request.POST.get("phone")
        date_requested = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        description = "Nome: " + request.POST.get("name") + "\nTel: " + request.POST.get("phone") + "\nEmail: " + request.POST.get("email") + "\nSubmetido a: " + date_requested + "\nRazão: " + request.POST.get("description")
        start_datetime = datetime.datetime(int(request.POST.get("year")), int(request.POST.get("month")), int(request.POST.get("day")), int(request.POST.get("hour")), int(request.POST.get("minutes")))
        end_datetime = start_datetime + datetime.timedelta(minutes=APPOINTMENT_DURATION_MIN)

        # print(summary)
        # print(description)
        # print(start_datetime)
        # print(request.POST.get("name"))
        # print(request.POST.get("phone"))
        # print(request.POST.get("email"))
        # print(request.POST.get("day"))
        # print(request.POST.get("month"))
        # print(request.POST.get("year"))
        # print(request.POST.get("hour"))
        # print(request.POST.get("minutes"))
        # print(request.POST.get("description"))
        #
        insert_calendar_event(summary, description, start_datetime, end_datetime)

    if request.method == "POST" and request.POST.get("form") == 'opinion':

        print(request.POST.get("name"))
        print(request.POST.get("opinion"))

    return render(request=request, template_name='eso/scheduling_page.html', context=context)
