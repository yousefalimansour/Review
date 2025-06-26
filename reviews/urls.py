from django.urls import path
from . import views
urlpatterns = [
    path("",views.ReviewCreateView.as_view()),
    path("thank-you",views.ThankyouView.as_view()),
    path("reviews",views.ReviewsList2View.as_view()),
    path("review/<int:pk>",views.SingleDetailReiewView.as_view())
]
