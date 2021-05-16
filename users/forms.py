from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        # fields we want to be available for form to add new user
        # password and confirm password are not neede add explicitly
        fields = ('username', 'email', 'age')
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        # Here we will add all the default fields
        # Here, age field will be available to editing by default
        fields = UserChangeForm.Meta.fields
        model = CustomUser
