from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Contact, PhoneNumber
from django.views.decorators.csrf import csrf_exempt


def calc_view(request):
    if request.POST:
        words = request.POST.get("input", "")
        w1, w2 = words.split(' ', 2)
        w1, w2 = set(w1), set(w2)
        result = w1.intersection(w2)
        result = sorted(result)
        result = ', '.join(result)
    else:
        result = None

    context = {"result": result}
    return render(request, "calc.html", context)





def get_all_contacts_view(request):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}
    return render(request, "contacts.html", context)


def get_contact_view(request, id):
    phone_numbers = PhoneNumber.objects.filter(contact=id)
    context = {"phone_numbers": phone_numbers}
    return render(request, "phone_numbers.html", context)







def edit_contact_view(request, id):
    context = {"id": id}
    return render(request, "edit.html", context)


def delete_contact_view(request, id):
    context = {"id": id}
    return render(request, "delete.html", context)


def create_contact_view(request):
    context = {}
    return render(request, "create.html", context)


def create_contact_post(request):
    name = request.POST.get("name", None)
    surname = request.POST.get("surname", None)
    Contact.objects.create(name=name, surname=surname)
    return HttpResponseRedirect('/Home/')


def edit_contact_post(request, id):
    name = request.POST.get("name", None)
    surname = request.POST.get("surname", None)
    contact = Contact.objects.filter(id=id)
    contact.update(name=name, surname=surname)
    return HttpResponseRedirect('/Home/')


def delete_contact_post(request, id):
    Contact.objects.filter(id=id).delete()
    return HttpResponseRedirect('/Home/')


def WApi_GetAll_view(request):
    all_contacts = Contact.objects.all()
    return JsonResponse(list(all_contacts.values()), safe=False, json_dumps_params={'ensure_ascii': False})


def WApi_Get_view(request, id):
    contact = Contact.objects.filter(id=id)
    return JsonResponse(list(contact.values()), safe=False, json_dumps_params={'ensure_ascii': False})


def WApi_Create_view(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    contact = Contact.objects.create(id=id, name=name, surname=surname)
    contact.save()
    contact = Contact.objects.filter(id=id)
    return JsonResponse(list(contact.values()), safe=False, json_dumps_params={'ensure_ascii': False})


def WApi_Update_view(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    surname = request.POST.get("surname")

    contact = Contact.objects.filter(id=id)
    contact.update(name=name, surname=surname)
    return JsonResponse(list(contact.values()), safe=False, json_dumps_params={'ensure_ascii': False})


def WApi_Delete_view(request):
    id = request.POST.get("id")
    contact = Contact.objects.filter(id=id)
    response = JsonResponse(list(contact.values()), safe=False, json_dumps_params={'ensure_ascii': False})
    contact.delete()
    return response


def index_view(request):
    return render(request, "index.html")
