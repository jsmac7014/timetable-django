
from django.forms import ModelForm, forms, TextInput, TimeInput,CharField,IntegerField
from .models import Activity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['content', 'day', 'fromTime','toTime']
        widgets={
            "fromTime":TimeInput(attrs={'type':'time','class':'time'}),
            "toTime":TimeInput(attrs={'type':'time', 'class':'time'}),
        }
            

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = '이름'
        self.fields['last_name'].widget.attrs['placeholder'] = '성'
        self.fields['username'].widget.attrs['placeholder'] = '아이디'
        self.fields['password1'].widget.attrs['placeholder'] = '비밀번호'
        self.fields['password2'].widget.attrs['placeholder'] = '비밀번호 확인'

        for fieldname in ['first_name','last_name','username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs['class'] = 'tb-input'
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''


    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
