from django import forms
from posts.models import Comment,Post
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('message','username')
        ordering = ['-created_at']
        widgets = {'message':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
                'username':forms.TextInput(attrs={'class':'form-control'})
                }
