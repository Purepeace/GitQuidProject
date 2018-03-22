from django import forms
from django.contrib.auth.models import User
from GitQuid.models import UserProfile, Category

class CategoryForm(forms.ModelForm):
    name= forms.CharField(max_length=128,
                          help_text="Please enter the category name." )
    views =forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes =forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields =('name',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None,
        }

    # Checks if confirm password field matches
    # Sauce: https://stackoverflow.com/questions/34609830/django-modelform-how-to-add-a-confirm-password-field
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'description')
