from django.contrib.auth.forms import UserCreationForms
from django.contrib.auth.models import User
from django import Forms

class RegisterUserForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ('username', 'password1', 'password2')    
  
  def __init__(self, *args, **kwargs):
    super(RegisterUserForm, self).__init__(*args, **kwargs)
    
    self.fields['username'].widget.attrs['class'] = 'name'
    self.fields['password1'].widget.attrs['class'] = 'name'
    self.fields['password2'].widget.attrs['class'] = 'name'
    
