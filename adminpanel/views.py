from django.shortcuts import render
from dgmenu_account.models import CustomUser as User


# Create your views here.

def index(request, *args, **kwargs):
    cx = {}
    return render(request, 'adminpanel/adminpanel_home_page.html', cx)


def header_references_partial_view(request, *args, **kwargs):
    cx = {}
    return render(request, 'shared/panel/_HeaderReferences.html', cx)


def header_panel_partial_view(request, *args, **kwargs):
    cx = {}
    return render(request, 'shared/panel/_Header.html', cx)


def quick_bar_panel_partial_view(request, *args, **kwargs):
    cx = {}
    return render(request, 'shared/panel/_QuickBar.html', cx)


def navbar_panel_partial_view(request, *args, **kwargs):
    userid = request.user
    user = User.objects.filter(id=userid.id).first()

    cx = {'user': user}
    return render(request, 'shared/panel/_Navbar.html', cx)
