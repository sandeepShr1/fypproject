from django import forms
from House.models import Post

#Creating a form
class PostForm(forms.ModelForm):
    #create meta class
    class Meta:
        #specify model to be used
        model = Post

        #specify fields to be used
        fields = [
            "title",
            "description",
            "area",
            "location",
            "price",
            "image"

        ]

 