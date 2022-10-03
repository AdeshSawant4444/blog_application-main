from django import forms
from .models import Profile, BlogPost

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'bio','phone_no', 'facebook', 'instagram', 'linkedin',  )
        widgets = {
                'bio': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the Bio'}),
                    'phone_no': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the phone number'}),
                'facebook': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facebook'}),
            'linkedin': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Linkedin'}),
            'instagram': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Instagram'}),
        }
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', )
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
    }   