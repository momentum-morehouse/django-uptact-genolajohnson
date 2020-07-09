from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Note
from .forms import ContactForm, NoteForm


# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})

def list_notes(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    notes = Notes.objects.filter(contact=contact)


def contact_detail(request,pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request,"contacts/contact_view.html", {"contact": contact})

# def add_NoteForm (request,pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'GET':
#         form = NoteForm()

#     else:
#         form = NoteForm
#         (data=request.POST)

#     if form.is_valid():

#         form.save()
#         return redirect
#         (to='contat_detail')

#     return render(request,"contacts/vint.:pk>/notes/",{'form': form})

def add_note(request):
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})

# def contact_detail(request):
#     if request.method =='GET':
#         form = 