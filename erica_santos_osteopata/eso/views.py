from django.shortcuts import render, get_object_or_404
from.models import TextPresentation, Opinion, OsteopathyAbout, OsteopathyCase, OsteopathyHistory, AppointmentsDescription


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

    return render(request=request, template_name='eso/scheduling_page.html', context=context)