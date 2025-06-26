from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View 
from .forms import ReviewForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import FormView ,CreateView
from .models import Review
# Create your views here.



class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

class ReviewFormView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    


class ReviewsList2View(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review
    context_object_name = "reviews"

class SingleDetailReiewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request,"reviews/review.html",{
            "form":form
        })
    
    def post(self ,request):
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        
        return render(request,"reviews/review.html",{
            "form":form
        })

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"
    
class ReviewsListView(TemplateView):
    template_name = "reviews/reviews_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews 
        return context
    
class SingleReiewView(TemplateView):
    template_name = "reviews/single_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_review = Review.objects.get(pk = review_id)
        context["review"] = selected_review
        return context
    
def review(request):

    if request.method =="POST":
        # enterd_name = request.POST["username"]
        form=ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            # review_from_request = Review(
            #     user_name =form.cleaned_data["user_name"],
            #     review_area = form.cleaned_data["review_text"],
            #     rating = form.cleaned_data["rating"])
            form.save()
            return HttpResponseRedirect("/thank-you")
        
    else:
        form = ReviewForm()
    return render(request,"reviews/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request , "reviews/thank_you.html")