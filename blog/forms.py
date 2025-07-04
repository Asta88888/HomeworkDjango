from django.forms import ModelForm
from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ("number_of_views",)







