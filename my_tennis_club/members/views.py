from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')

    records_andres = Member.objects.filter(firstname__startswith='i').values()
    records_paula = Member.objects.filter(firstname__icontains='mar').values()
    records_carlos = Member.objects.filter(firstname__endswith='os').values()
    records_Valentina = Member.objects.filter(firstname__in=['valentina', 'valery', 'valeria']).values()
    records_Juan = Member.objects.filter(firstname__iexact='juan').values()
    records_Camila = Member.objects.filter(firstname__contains='mil').values()
    recods_Felipe = Member.objects.exclude(firstname__startswith='f').values()
    records_Sofia = Member.objects.filter(firstname__regex=r'^[s].*[a]$').values()
    records_Enrique = Member.objects.filter(Q(firstname__icontains='en') | Q(lastname__icontains='que')).values()
    records_Daniel = Member.objects.filter(id__range=(1, 5)).values()

    miembros = Member.objects.all().values()

    context = {
        'miembros': miembros,
        'records_andres': records_andres,
        'records_paula': records_paula,
        'records_carlos': records_carlos,
        'records_Valentina': records_Valentina,
        'records_Juan': records_Juan,
        'records_Camila': records_Camila,
        'recods_Felipe': recods_Felipe,
        'records_Sofia': records_Sofia,
        'records_Enrique': records_Enrique,
        'records_Daniel': records_Daniel,
    }

    return HttpResponse(template.render(context, request))
    