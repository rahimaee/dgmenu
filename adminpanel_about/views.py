from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from adminpanel_about.forms import AboutForm
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_about.models import CafeAbout


def about(request, *args, **kwargs):
    ctx = {}
    if not request.user.is_authenticated:
        raise Http404()
    cafe = Cafe.objects.filter(Manager_id=request.user.id, Admin_Is_Active=True).first()
    if cafe is None:
        raise Http404()

    About = CafeAbout.objects.filter(Cafe__Manager_id=request.user.id).first()
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
        form = AboutForm(request.POST, request.FILES or None, )
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
