from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from adminpanel_about.forms import AboutForm
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_about.models import CafeAbout
from dgmenu_account_role.models import Role


def about(request, *args, **kwargs):
    ctx = {}
    if not request.user.is_authenticated:
        raise Http404()

    role = Role.objects.filter(User_id=request.user.id, Cafe_About_edit=True).first()
    if role is None:
        return HttpResponse("عدم دسترسیس")
    cafe = Cafe.objects.filter(id=role.Cafe.id, Admin_Is_Active=True).first()
    if cafe is None:
        raise Http404()
    About = CafeAbout.objects.filter(id=cafe.id).first()
    if request.method == "GET":
        form = AboutForm()
        if About is None:
            ctx = {'form': form}
        else:
            form.fields['Image'].initial = About.Image
            form.fields['Title'].initial = About.Title
            form.fields['Description'].initial = About.Description
            ctx = {'form': form}
    if request.method == "POST":
        if About is None:
            form = AboutForm(request.POST, request.FILES or None, )
        else:
            form = AboutForm(request.POST, request.FILES or None, initial={"Image": About.Image})
        if not form.is_valid():
            if About is None:
                ctx = {'form': form}
            else:
                form.fields['Image'].initial = About.Image
                form.fields['Title'].initial = About.Title
                form.fields['Description'].initial = About.Description
                ctx = {'form': form}
            return render(request, 'adminpanel_about/about_form_list.html', ctx)
        else:
            if About is None:
                a = CafeAbout()
                a.Title = form.cleaned_data['Title']
                a.Description = form.cleaned_data['Description']
                a.Image = form.cleaned_data['Image']
                a.Cafe = cafe
                a.save()
                return redirect('adminpanel:starting_page')
            else:
                About.Image = form.cleaned_data['Image']
                About.Title = form.cleaned_data['Title']
                About.Description = form.cleaned_data['Description']
                About.save()
                return redirect('adminpanel:starting_page')
    return render(request, 'adminpanel_about/about_form_list.html', ctx)
