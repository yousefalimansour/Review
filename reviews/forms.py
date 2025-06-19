from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(label="Your Name:",max_length=100,error_messages={
        "required":"Name is requied!",
        "max_length": "len must not be less than 100!"
    })