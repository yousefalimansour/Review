from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name:",max_length=100,error_messages={
#         "required":"Name is requied!",
#         "max_length": "len must not be less than 100!"
#     })
#     review_text = forms.CharField(label="Your feedback:", widget=forms.Textarea)
#     rating = forms.IntegerField( label= "Rateing:" ,min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = "__all__"

        labels = {
            "user_name" : "Yor Name",
            "review_area":"Your feedback:",
            "rating":"Your Rating"
        }

        error_messages = {
            "user_name":{
                "required":"Name is requied!",
                "max_length": "len must not be less than 100!"
            }
        }
        