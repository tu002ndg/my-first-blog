from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',  'text',)
        labels = {'title':'Заголовок','text':''}
        widgets = {
            'title':forms.TextInput(attrs={'size':50}),
            'text':forms.Textarea(attrs={'cols':80})}