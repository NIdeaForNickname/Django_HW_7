from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import EventForm, ParticipantForm

c_id = 0
events = {}

def create_event(request):
    global c_id, events
    form_count = int(request.GET.get("forms", 1))

    ParticipantFormSet = formset_factory(ParticipantForm, extra=form_count)

    if request.method == "POST":
        event_form = EventForm(request.POST)
        participant_formset = ParticipantFormSet(request.POST)

        if event_form.is_valid() and participant_formset.is_valid():
            event = {"name": event_form.cleaned_data["name"], "date": event_form.cleaned_data["date"], "participants": participant_formset.cleaned_data}
            c_id = c_id+1
            events[c_id] = event
            return HttpResponseRedirect(f"/event?id={c_id}")

    else:
        event_form = EventForm()
        participant_formset = ParticipantFormSet()

    print("returning...")
    return render(request, "create_event.html", {
        "event_form": event_form,
        "participant_formset": participant_formset,
        "form_count": form_count,
        "next_count": form_count + 1,
    })

def view_event(request):
    global events
    q = int(request.GET.get("id", None))
    if q:
        return render(request, "event.html", {"event": events[q]})
    return HttpResponseRedirect(f"/add_event?forms=1")