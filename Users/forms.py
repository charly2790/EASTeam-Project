from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class user_register_form(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k: '' for k in fields}
        