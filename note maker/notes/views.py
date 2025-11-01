from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

# Hardcoded credentials
USERNAME = "anshu"
PASSWORD = "12345"


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == USERNAME and password == PASSWORD:
            request.session["logged_in"] = True
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")


def home(request):
    if not request.session.get("logged_in"):
        return redirect("login")

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Note.objects.create(content=content)
            return redirect("home")

    notes = Note.objects.all().order_by("-created_at")
    return render(request, "home.html", {"notes": notes})


def delete_note(request, note_id):
    if not request.session.get("logged_in"):
        return redirect("login")

    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect("home")


def edit_note(request, note_id):
    if not request.session.get("logged_in"):
        return redirect("login")

    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        new_content = request.POST.get("content")
        if new_content:
            note.content = new_content
            note.save()
            return redirect("home")
    return render(request, "edit_note.html", {"note": note})
