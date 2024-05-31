from django.forms import ModelForm
from .models import News, Comments
from django import forms

class NewsModelForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(NewsModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = ""
        self.fields['title'].label = ""
        self.fields['title'].widget = forms.Textarea(
            attrs={'placeholder': 'Название новости', "rows": 1, "class": "form-control",}
        )
        self.fields['content'].help_text = ""
        self.fields['content'].label = ""
        self.fields['content'].widget = forms.Textarea(
            attrs={'placeholder': 'Содержание новости', "rows": 13, "class": "form-control", }
        )

class CommentModelForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]
    def __init__(self, *args, **kwargs):
        super(CommentModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].help_text = ""
        self.fields['text'].label = ""
        self.fields['text'].widget = forms.Textarea(
            attrs={'placeholder': 'Текст комментария', "rows": 1, "class": "form-control",}
        )
