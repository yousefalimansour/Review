from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
from django.views.generic import ListView , CreateView
# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg","wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(CreateView):
    model = UserProfile
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
    fields = "__all__"

class CreateProfileListView(ListView):
    model = UserProfile
    template_name = "profiles/create_listprofile.html"
    context_object_name = "profiles"




# class CreateProfileView(View):
#     def get(self, request):
    #     form = ProfileForm()
    #     return render(request, "profiles/create_profile.html",{
    #         "form":form
    #     })

    # def post(self, request):
    #     # store_file(request.FILES["image"])
    #     submitted_form = ProfileForm(request.POST,request.FILES)
    #     if submitted_form.is_valid():
    #         profile = UserProfile(image = request.FILES["user_image"])
    #         profile.save()
    #         return HttpResponseRedirect("/profiles")
