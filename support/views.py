from django.shortcuts import render


def faq_view(request):
    return render(request, 'support/faq.html')


def contact_view(request):
    return render(request, 'support/contact.html')


def about_view(request):
    return render(request, 'support/about.html')


def team_view(request):
    return render(request, 'support/team.html')


def privacy_policy_view(request):
    return render(request, 'support/privacy_policy.html')
