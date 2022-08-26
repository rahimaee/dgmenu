from django.shortcuts import render


# Create your views here.

def cafe_team(request, *args, **kwargs):
    cx = {
        'CafeUserId': 12
    }
    return render(request, 'dgmenu_cafe_team/cafe_team_page.html', cx)
