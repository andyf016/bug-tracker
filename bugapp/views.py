from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from bugapp.models import Ticket
from myuser.models import CustomUser
from bugapp.forms import TicketForm, LoginForm

@login_required
def index(request):
    new_tickets = Ticket.objects.filter(status="N")
    progress_tickets = Ticket.objects.filter(status="IP")
    finished_tickets = Ticket.objects.filter(status='D')
    invalid_tickets = Ticket.objects.filter(status="IN")
    return render(request, 'index.html', {'new_tickets': new_tickets, 'progress_tickets': progress_tickets, 'finished_tickets': finished_tickets, 'invalid_tickets': invalid_tickets})

@login_required
def ticket_detail_view(request, ticket_id):
    my_ticket = Ticket.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail.html', {'ticket': my_ticket})

@login_required
def ticket_form_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                author=request.user
            )
            return HttpResponseRedirect(reverse('home'))
    form = TicketForm()
    return render(request, "generic_form.html", {'form': form})

@login_required
def ticket_edit_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    data = {
        "title": ticket.title,
        "description": ticket.description
    }
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("details", args=[ticket.id]))
    form = TicketForm(initial=data)
    return render(request, "generic_form.html", {"form": form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home")))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def assign_view(request, ticket_id):
    current_ticket = Ticket.objects.get(id=ticket_id)
    current_ticket.assigned = request.user
    current_ticket.status = 'In Progress'
    current_ticket.finishing = None
    current_ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def done_view(request, ticket_id):
    current_ticket = Ticket.objects.get(id=ticket_id)
    current_ticket.status = 'Done'
    current_ticket.finishing = current_ticket.assigned
    current_ticket.assigned = None
    current_ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def invalid_view(request, ticket_id):
    current_ticket = Ticket.objects.get(id=ticket_id)
    current_ticket.status = 'Invalid'
    current_ticket.finishing = None
    current_ticket.assigned = None
    current_ticket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))



