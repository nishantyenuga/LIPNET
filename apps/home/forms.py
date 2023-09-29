from django import forms 
from .models import uploadedVid,forum

class vidForm(forms.ModelForm):
    class Meta:
        model=uploadedVid
        fields = [
            'video_name',
            'video',
    
        ]
        widgets = {
            'video_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;height: 50px;',
                'placeholder': 'Video Name'
                }),
                # 'uploadfile' : forms.ClearableFileInput(attrs={
            #     'class': "form-control",
            #     'style': 'max-width: 300px;height: 50px;',
            #     'placeholder': 'File'
            #     })


        }

class forumForm(forms.ModelForm):
    class Meta:
        model=forum
        fields=[
            'user_name',
            'answer',
        ]
