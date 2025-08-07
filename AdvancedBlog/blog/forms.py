from django import forms
from .models import Post, Attachment, Comment
from ckeditor.widgets import CKEditorWidget
from taggit.forms import TagWidget
from captcha.fields import CaptchaField

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    tags = forms.CharField(widget=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'cover_image', 'tags']

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']

AttachmentFormSet = forms.inlineformset_factory(Post, Attachment, form=AttachmentForm, extra=2)

class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['name', 'message']
