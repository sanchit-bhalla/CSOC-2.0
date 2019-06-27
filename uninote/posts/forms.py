from django import forms
from posts.models import Comment,Post


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','message')

        widgets = {'message':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
                    'author':forms.TextInput(attrs={'class':'textinputclass'})
                    }
