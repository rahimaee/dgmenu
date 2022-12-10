from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from adminpanel_cafe_settings.forms import SettingsForm
from dgmenu_cafe.models import Cafe
from dgmenu_account_role.models import Role


class SettingsUpdate(LoginRequiredMixin, View):
    success_url = reverse_lazy('food:all')
    template = 'adminpanel_cafe_settings/cafe_settings_form.html'

    def get(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_settings_edit=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe = Cafe.objects.filter(id=role.Cafe.id).first()
        if cafe is None:
            raise Http404()
        form = SettingsForm()
        if cafe.Cafe_Header_Logo is not None:
            form.fields['Cafe_Header_Logo'].initial = cafe.Cafe_Header_Logo
        if cafe.Cafe_favicon is not None:
            form.fields['Cafe_favicon'].initial = cafe.Cafe_favicon
        if cafe.Cafe_Apple_Touch_Icon57 is not None:
            form.fields['Cafe_Apple_Touch_Icon57'].initial = cafe.Cafe_Apple_Touch_Icon57
        if cafe.Cafe_Apple_Touch_Icon60 is not None:
            form.fields['Cafe_Apple_Touch_Icon60'].initial = cafe.Cafe_Apple_Touch_Icon60
        if cafe.Cafe_Apple_Touch_Icon72 is not None:
            form.fields['Cafe_Apple_Touch_Icon72'].initial = cafe.Cafe_Apple_Touch_Icon72

        if cafe.Cafe_Apple_Touch_Icon76 is not None:
            form.fields['Cafe_Apple_Touch_Icon76'].initial = cafe.Cafe_Apple_Touch_Icon76

        if cafe.Cafe_Apple_Touch_Icon114 is not None:
            form.fields['Cafe_Apple_Touch_Icon114'].initial = cafe.Cafe_Apple_Touch_Icon114
        if cafe.Cafe_Apple_Touch_Icon120 is not None:
            form.fields['Cafe_Apple_Touch_Icon120'].initial = cafe.Cafe_Apple_Touch_Icon120
        if cafe.Cafe_Apple_Touch_Icon144 is not None:
            form.fields['Cafe_Apple_Touch_Icon144'].initial = cafe.Cafe_Apple_Touch_Icon144
        if cafe.Cafe_Apple_Touch_Icon152 is not None:
            form.fields['Cafe_Apple_Touch_Icon152'].initial = cafe.Cafe_Apple_Touch_Icon152
        if cafe.Cafe_Apple_Touch_Icon180 is not None:
            form.fields['Cafe_Apple_Touch_Icon180'].initial = cafe.Cafe_Apple_Touch_Icon180
        if cafe.Cafe_Apple_Touch_Icon192 is not None:
            form.fields['Cafe_Apple_Touch_Icon192'].initial = cafe.Cafe_Apple_Touch_Icon192
        if cafe.Cafe_Apple_Touch_Icon32 is not None:
            form.fields['Cafe_Apple_Touch_Icon32'].initial = cafe.Cafe_Apple_Touch_Icon32
        if cafe.Cafe_Apple_Touch_Icon196 is not None:
            form.fields['Cafe_Apple_Touch_Icon196'].initial = cafe.Cafe_Apple_Touch_Icon196
        if cafe.Cafe_Apple_Touch_Icon16 is not None:
            form.fields['Cafe_Apple_Touch_Icon16'].initial = cafe.Cafe_Apple_Touch_Icon16

        if cafe.Cafe_Msapplication is not None:
            form.fields['Cafe_Msapplication'].initial = cafe.Cafe_Msapplication

        if cafe.Cafe_Header_Home_Background is not None:
            form.fields['Cafe_Header_Home_Background'].initial = cafe.Cafe_Header_Home_Background

        if cafe.Cafe_Header_Detail_Background is not None:
            form.fields['Cafe_Header_Detail_Background'].initial = cafe.Cafe_Header_Detail_Background

        if cafe.Cafe_Header_About_Background is not None:
            form.fields['Cafe_Header_About_Background'].initial = cafe.Cafe_Header_About_Background

        if cafe.Cafe_Header_Team_Background is not None:
            form.fields['Cafe_Header_Team_Background'].initial = cafe.Cafe_Header_Team_Background

        if cafe.Cafe_Banner_Home is not None:
            form.fields['Cafe_Banner_Home'].initial = cafe.Cafe_Banner_Home

        form.initial['Cafe_Name'] = cafe.Cafe_Name
        form.initial['Cafe_Description'] = cafe.Cafe_Description
        form.initial['Cafe_keywords'] = cafe.Cafe_keywords
        form.initial['Cafe_Address'] = cafe.Cafe_Address
        form.initial['Cafe_Tel1'] = cafe.Cafe_Tel1
        form.initial['Cafe_Tel2'] = cafe.Cafe_Tel2
        form.initial['Cafe_Tel3'] = cafe.Cafe_Tel3
        form.initial['Cafe_Email'] = cafe.Cafe_Email
        form.initial['Cafe_Instagram'] = cafe.Cafe_Instagram
        form.initial['Cafe_Facebook'] = cafe.Cafe_Facebook
        form.initial['Cafe_YouTube'] = cafe.Cafe_YouTube
        form.initial['Cafe_Twitter'] = cafe.Cafe_Twitter
        form.initial['Cafe_Opening_Hours'] = cafe.Cafe_Opening_Hours

        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        role = Role.objects.filter(User_id=request.user.id, Cafe_settings_edit=True).first()
        if role is None:
            return HttpResponse("عدم دسترسیس")
        cafe = Cafe.objects.filter(id=role.Cafe.id).first()
        if cafe is None:
            raise Http404()

        form = SettingsForm(request.POST, request.FILES or None)

        if cafe.Cafe_Header_Logo is not None:
            form.fields['Cafe_Header_Logo'].initial = cafe.Cafe_Header_Logo

        if cafe.Cafe_favicon is not None:
            form.fields['Cafe_favicon'].initial = cafe.Cafe_favicon
        if cafe.Cafe_Apple_Touch_Icon57 is not None:
            form.fields['Cafe_Apple_Touch_Icon57'].initial = cafe.Cafe_Apple_Touch_Icon57
        if cafe.Cafe_Apple_Touch_Icon60 is not None:
            form.fields['Cafe_Apple_Touch_Icon60'].initial = cafe.Cafe_Apple_Touch_Icon60
        if cafe.Cafe_Apple_Touch_Icon72 is not None:
            form.fields['Cafe_Apple_Touch_Icon72'].initial = cafe.Cafe_Apple_Touch_Icon72
        if cafe.Cafe_Apple_Touch_Icon76 is not None:
            form.fields['Cafe_Apple_Touch_Icon76'].initial = cafe.Cafe_Apple_Touch_Icon76
        if cafe.Cafe_Apple_Touch_Icon114 is not None:
            form.fields['Cafe_Apple_Touch_Icon114'].initial = cafe.Cafe_Apple_Touch_Icon114
        if cafe.Cafe_Apple_Touch_Icon120 is not None:
            form.fields['Cafe_Apple_Touch_Icon120'].initial = cafe.Cafe_Apple_Touch_Icon120
        if cafe.Cafe_Apple_Touch_Icon144 is not None:
            form.fields['Cafe_Apple_Touch_Icon144'].initial = cafe.Cafe_Apple_Touch_Icon144
        if cafe.Cafe_Apple_Touch_Icon152 is not None:
            form.fields['Cafe_Apple_Touch_Icon152'].initial = cafe.Cafe_Apple_Touch_Icon152
        if cafe.Cafe_Apple_Touch_Icon180 is not None:
            form.fields['Cafe_Apple_Touch_Icon180'].initial = cafe.Cafe_Apple_Touch_Icon180
        if cafe.Cafe_Apple_Touch_Icon192 is not None:
            form.fields['Cafe_Apple_Touch_Icon192'].initial = cafe.Cafe_Apple_Touch_Icon192
        if cafe.Cafe_Apple_Touch_Icon32 is not None:
            form.fields['Cafe_Apple_Touch_Icon32'].initial = cafe.Cafe_Apple_Touch_Icon32
        if cafe.Cafe_Apple_Touch_Icon196 is not None:
            form.fields['Cafe_Apple_Touch_Icon196'].initial = cafe.Cafe_Apple_Touch_Icon196
        if cafe.Cafe_Apple_Touch_Icon16 is not None:
            form.fields['Cafe_Apple_Touch_Icon16'].initial = cafe.Cafe_Apple_Touch_Icon16

        if cafe.Cafe_Header_Home_Background is not None:
            form.fields['Cafe_Header_Home_Background'].initial = cafe.Cafe_Header_Home_Background

        if cafe.Cafe_Header_Detail_Background is not None:
            form.fields['Cafe_Header_Detail_Background'].initial = cafe.Cafe_Header_Detail_Background

        if cafe.Cafe_Header_About_Background is not None:
            form.fields['Cafe_Header_About_Background'].initial = cafe.Cafe_Header_About_Background

        if cafe.Cafe_Header_Team_Background is not None:
            form.fields['Cafe_Header_Team_Background'].initial = cafe.Cafe_Header_Team_Background

        if cafe.Cafe_Msapplication is not None:
            form.fields['Cafe_Msapplication'].initial = cafe.Cafe_Msapplication

        if cafe.Cafe_Banner_Home is not None:
            form.fields['Cafe_Banner_Home'].initial = cafe.Cafe_Banner_Home

        form.initial['Cafe_Name'] = cafe.Cafe_Name
        form.initial['Cafe_Description'] = cafe.Cafe_Description
        form.initial['Cafe_keywords'] = cafe.Cafe_keywords
        form.initial['Cafe_Address'] = cafe.Cafe_Address
        form.initial['Cafe_Tel1'] = cafe.Cafe_Tel1
        form.initial['Cafe_Tel2'] = cafe.Cafe_Tel2
        form.initial['Cafe_Tel3'] = cafe.Cafe_Tel3
        form.initial['Cafe_Email'] = cafe.Cafe_Email
        form.initial['Cafe_Instagram'] = cafe.Cafe_Instagram
        form.initial['Cafe_Facebook'] = cafe.Cafe_Facebook
        form.initial['Cafe_YouTube'] = cafe.Cafe_YouTube
        form.initial['Cafe_Twitter'] = cafe.Cafe_Twitter
        form.initial['Cafe_Opening_Hours'] = cafe.Cafe_Opening_Hours
        if not form.is_valid():
            if cafe.Cafe_Header_Logo is not None:
                form.fields['Cafe_Header_Logo'].initial = cafe.Cafe_Header_Logo

            if cafe.Cafe_favicon is not None:
                form.fields['Cafe_favicon'].initial = cafe.Cafe_favicon
            if cafe.Cafe_Apple_Touch_Icon57 is not None:
                form.fields['Cafe_Apple_Touch_Icon57'].initial = cafe.Cafe_Apple_Touch_Icon57
            if cafe.Cafe_Apple_Touch_Icon60 is not None:
                form.fields['Cafe_Apple_Touch_Icon60'].initial = cafe.Cafe_Apple_Touch_Icon60
            if cafe.Cafe_Apple_Touch_Icon72 is not None:
                form.fields['Cafe_Apple_Touch_Icon72'].initial = cafe.Cafe_Apple_Touch_Icon72
            if cafe.Cafe_Apple_Touch_Icon76 is not None:
                form.fields['Cafe_Apple_Touch_Icon76'].initial = cafe.Cafe_Apple_Touch_Icon76
            if cafe.Cafe_Apple_Touch_Icon114 is not None:
                form.fields['Cafe_Apple_Touch_Icon114'].initial = cafe.Cafe_Apple_Touch_Icon114
            if cafe.Cafe_Apple_Touch_Icon120 is not None:
                form.fields['Cafe_Apple_Touch_Icon120'].initial = cafe.Cafe_Apple_Touch_Icon120
            if cafe.Cafe_Apple_Touch_Icon144 is not None:
                form.fields['Cafe_Apple_Touch_Icon144'].initial = cafe.Cafe_Apple_Touch_Icon144
            if cafe.Cafe_Apple_Touch_Icon152 is not None:
                form.fields['Cafe_Apple_Touch_Icon152'].initial = cafe.Cafe_Apple_Touch_Icon152
            if cafe.Cafe_Apple_Touch_Icon180 is not None:
                form.fields['Cafe_Apple_Touch_Icon180'].initial = cafe.Cafe_Apple_Touch_Icon180
            if cafe.Cafe_Apple_Touch_Icon192 is not None:
                form.fields['Cafe_Apple_Touch_Icon192'].initial = cafe.Cafe_Apple_Touch_Icon192
            if cafe.Cafe_Apple_Touch_Icon32 is not None:
                form.fields['Cafe_Apple_Touch_Icon32'].initial = cafe.Cafe_Apple_Touch_Icon32
            if cafe.Cafe_Apple_Touch_Icon196 is not None:
                form.fields['Cafe_Apple_Touch_Icon196'].initial = cafe.Cafe_Apple_Touch_Icon196
            if cafe.Cafe_Apple_Touch_Icon16 is not None:
                form.fields['Cafe_Apple_Touch_Icon16'].initial = cafe.Cafe_Apple_Touch_Icon16

            if cafe.Cafe_Msapplication is not None:
                form.fields['Cafe_Msapplication'].initial = cafe.Cafe_Msapplication

            if cafe.Cafe_Header_Home_Background is not None:
                form.fields['Cafe_Header_Home_Background'].initial = cafe.Cafe_Header_Home_Background

            if cafe.Cafe_Header_Detail_Background is not None:
                form.fields['Cafe_Header_Detail_Background'].initial = cafe.Cafe_Header_Detail_Background

            if cafe.Cafe_Header_About_Background is not None:
                form.fields['Cafe_Header_About_Background'].initial = cafe.Cafe_Header_About_Background

            if cafe.Cafe_Header_Team_Background is not None:
                form.fields['Cafe_Header_Team_Background'].initial = cafe.Cafe_Header_Team_Background

            if cafe.Cafe_Banner_Home is not None:
                form.fields['Cafe_Banner_Home'].initial = cafe.Cafe_Banner_Home

            form.initial['Cafe_Name'] = cafe.Cafe_Name
            form.initial['Cafe_Description'] = cafe.Cafe_Description
            form.initial['Cafe_keywords'] = cafe.Cafe_keywords
            form.initial['Cafe_Address'] = cafe.Cafe_Address
            form.initial['Cafe_Tel1'] = cafe.Cafe_Tel1
            form.initial['Cafe_Tel2'] = cafe.Cafe_Tel2
            form.initial['Cafe_Tel3'] = cafe.Cafe_Tel3
            form.initial['Cafe_Email'] = cafe.Cafe_Email
            form.initial['Cafe_Instagram'] = cafe.Cafe_Instagram
            form.initial['Cafe_Facebook'] = cafe.Cafe_Facebook
            form.initial['Cafe_YouTube'] = cafe.Cafe_YouTube
            form.initial['Cafe_Twitter'] = cafe.Cafe_Twitter
            form.initial['Cafe_Opening_Hours'] = cafe.Cafe_Opening_Hours
            ctx = {'form': form, }
            return render(request, self.template, ctx)

        cafe.Cafe_Name = form.cleaned_data['Cafe_Name']
        cafe.Cafe_Description = form.cleaned_data['Cafe_Description']
        cafe.Cafe_keywords = form.cleaned_data['Cafe_keywords']
        cafe.Cafe_Address = form.cleaned_data['Cafe_Address']
        cafe.Cafe_Tel1 = form.cleaned_data['Cafe_Tel1']
        cafe.Cafe_Tel2 = form.cleaned_data['Cafe_Tel2']
        cafe.Cafe_Tel3 = form.cleaned_data['Cafe_Tel3']
        cafe.Cafe_Email = form.cleaned_data['Cafe_Email']
        cafe.Cafe_Instagram = form.cleaned_data['Cafe_Instagram']
        cafe.Cafe_Facebook = form.cleaned_data['Cafe_Facebook']
        cafe.Cafe_YouTube = form.cleaned_data['Cafe_YouTube']
        cafe.Cafe_Twitter = form.cleaned_data['Cafe_Twitter']
        cafe.Cafe_Opening_Hours = form.cleaned_data['Cafe_Opening_Hours']

        if not form.cleaned_data['Cafe_Header_Logo']:
            cafe.Cafe_Header_Logo.delete()
        else:
            cafe.Cafe_Header_Logo = form.cleaned_data['Cafe_Header_Logo']

        if not form.cleaned_data['Cafe_favicon']:
            cafe.Cafe_favicon.delete()
        else:
            cafe.Cafe_favicon = form.cleaned_data['Cafe_favicon']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon57']:
            cafe.Cafe_Apple_Touch_Icon57.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon57 = form.cleaned_data['Cafe_Apple_Touch_Icon57']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon60']:
            cafe.Cafe_Apple_Touch_Icon60.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon60 = form.cleaned_data['Cafe_Apple_Touch_Icon60']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon72']:
            cafe.Cafe_Apple_Touch_Icon72.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon72 = form.cleaned_data['Cafe_Apple_Touch_Icon72']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon76']:
            cafe.Cafe_Apple_Touch_Icon76.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon76 = form.cleaned_data['Cafe_Apple_Touch_Icon76']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon114']:
            cafe.Cafe_Apple_Touch_Icon114.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon114 = form.cleaned_data['Cafe_Apple_Touch_Icon114']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon120']:
            cafe.Cafe_Apple_Touch_Icon120.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon120 = form.cleaned_data['Cafe_Apple_Touch_Icon120']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon144']:
            cafe.Cafe_Apple_Touch_Icon144.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon144 = form.cleaned_data['Cafe_Apple_Touch_Icon144']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon152']:
            cafe.Cafe_Apple_Touch_Icon152.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon152 = form.cleaned_data['Cafe_Apple_Touch_Icon152']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon180']:
            cafe.Cafe_Apple_Touch_Icon180.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon180 = form.cleaned_data['Cafe_Apple_Touch_Icon180']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon192']:
            cafe.Cafe_Apple_Touch_Icon192.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon192 = form.cleaned_data['Cafe_Apple_Touch_Icon192']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon32']:
            cafe.Cafe_Apple_Touch_Icon32.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon32 = form.cleaned_data['Cafe_Apple_Touch_Icon32']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon196']:
            cafe.Cafe_Apple_Touch_Icon196.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon196 = form.cleaned_data['Cafe_Apple_Touch_Icon196']

        if not form.cleaned_data['Cafe_Apple_Touch_Icon16']:
            cafe.Cafe_Apple_Touch_Icon16.delete()
        else:
            cafe.Cafe_Apple_Touch_Icon16 = form.cleaned_data['Cafe_Apple_Touch_Icon16']

        if not form.cleaned_data['Cafe_Msapplication']:
            cafe.Cafe_Msapplication.delete()
        else:
            cafe.Cafe_Msapplication = form.cleaned_data['Cafe_Msapplication']

        if not form.cleaned_data['Cafe_Header_Home_Background']:
            cafe.Cafe_Header_Home_Background.delete()
        else:
            cafe.Cafe_Header_Home_Background = form.cleaned_data['Cafe_Header_Home_Background']

        if not form.cleaned_data['Cafe_Header_Detail_Background']:
            cafe.Cafe_Header_Detail_Background.delete()
        else:
            cafe.Cafe_Header_Detail_Background = form.cleaned_data['Cafe_Header_Detail_Background']

        if not form.cleaned_data['Cafe_Header_About_Background']:
            cafe.Cafe_Header_About_Background.delete()
        else:
            cafe.Cafe_Header_About_Background = form.cleaned_data['Cafe_Header_About_Background']

        if not form.cleaned_data['Cafe_Header_Team_Background']:
            cafe.Cafe_Header_Team_Background.delete()
        else:
            cafe.Cafe_Header_Team_Background = form.cleaned_data['Cafe_Header_Team_Background']

        if not form.cleaned_data['Cafe_Banner_Home']:
            cafe.Cafe_Banner_Home.delete()
        else:
            cafe.Cafe_Banner_Home = form.cleaned_data['Cafe_Banner_Home']
        cafe.save()
        return redirect(self.success_url)
