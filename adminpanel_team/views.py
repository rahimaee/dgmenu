import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from adminpanel_team.forms import TeamForm
from dgmenu_cafe.models import Cafe
from dgmenu_cafe_team.models import CafeTeam


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cafe_team = CafeTeam.objects.filter(Cafe__Manager_id=user.id, IsActiveAdmin=True).all()
        ctx = {'cafe_team': cafe_team, }
        return render(request, 'adminpanel_team/team_list.html', ctx)


class TeamCreate(LoginRequiredMixin, View):
    template = 'adminpanel_team/team_form.html'
    success_url = reverse_lazy('team:all')

    def get(self, request):
        form = TeamForm(initial={'IsActive':True})
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = TeamForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        user = request.user
        cafe_team = CafeTeam()
        cafe = Cafe.objects.filter(Manager_id=user.id).first()
        cafe_team.IsActiveAdmin = True
        cafe_team.IsActive = form.cleaned_data['IsActive']
        cafe_team.Cafe = cafe
        cafe_team.Name = form.cleaned_data['Name']
        cafe_team.Family = form.cleaned_data['Family']
        cafe_team.Profile = form.cleaned_data['Profile']
        cafe_team.facebook = form.cleaned_data['facebook']
        cafe_team.instagram = form.cleaned_data['instagram']
        cafe_team.linkedin = form.cleaned_data['linkedin']
        cafe_team.JobType = form.cleaned_data['JobType']
        cafe_team.SubmitTime = datetime.datetime.now()

        cafe_team.save()
        return redirect(self.success_url)


class TeamUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('team:all')
    template = 'adminpanel_team/team_form.html'

    def get(self, request, pk):
        cafe_team = CafeTeam.objects.filter(pk=pk, Cafe__Manager_id=request.user.id).first()
        form = TeamForm(initial={'Profile': cafe_team.Profile})
        form.initial["Name"] = cafe_team.Name
        form.initial["Family"] = cafe_team.Family
        form.initial["JobType"] = cafe_team.JobType
        form.initial["facebook"] = cafe_team.facebook
        form.initial["instagram"] = cafe_team.instagram
        form.initial["linkedin"] = cafe_team.linkedin
        form.initial["IsActive"] = cafe_team.IsActive
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        cafe_team = CafeTeam.objects.filter(pk=pk, Cafe__Manager_id=request.user.id).first()
        form = TeamForm(request.POST, request.FILES or None, initial={'Profile':  cafe_team.Profile})
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        cafe_team.Profile = form.cleaned_data['Profile']
        cafe_team.Name = form.cleaned_data['Name']
        cafe_team.Family = form.cleaned_data['Family']
        cafe_team.JobType = form.cleaned_data['JobType']
        cafe_team.linkedin = form.cleaned_data['linkedin']
        cafe_team.instagram = form.cleaned_data['instagram']
        cafe_team.facebook = form.cleaned_data['facebook']
        cafe_team.IsActive = form.cleaned_data['IsActive']
        cafe_team.save()
        return redirect(self.success_url)
