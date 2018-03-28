from django import forms
from django.contrib.auth.models import *
from GitQuid.models import *
from markdownx.fields import MarkdownxFormField
from django.contrib.auth.forms import UserChangeForm


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


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


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User

        fields = (
            'email',

        )


class EditRestForm(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = (

            'picture',
            'description',
        )


class AddProjectForm(forms.ModelForm):
    name = forms.CharField(label="Title of the project:", max_length=Project.maxLen)

    class Meta:
        model = Project
        fields = ('name', 'category')

    def clean(self):
        cleaned_data = super(AddProjectForm, self).clean()
        # Validates if category actually exists. Needed cuz post could be tampered with.
        cat = cleaned_data.get('category')
        if not Category.objects.filter(name=cat):
            raise forms.ValidationError(
                "No such category exists, you cheeky hacker"
            )


class ProjectForm(forms.ModelForm):
    name = forms.CharField(label="Title of the project:", max_length=Project.maxLen,
                           widget=forms.TextInput(attrs={'placeholder': "(it will be displayed on search page, duh)"}))
    description = forms.CharField(label="", max_length=Project.maxLen, required=False,
                                  widget=forms.Textarea(attrs={
                                      'placeholder': "Short description: This will be displayed on browsing page. Think how you would attract potential donations"}))
    title_image = forms.ImageField(label="Title image:", required=False)
    # category = forms.CheckboxSelectMultiple(label="Category*:")

    body = MarkdownxFormField(label="Long description:", required=False,
                              widget=forms.TextInput(attrs={
                                  'placeholder': "Supports markdown! Also it autosaves! (if us lazy cunts will implement ajax lol)(also, succ a ducc, kickstarter)"}))
    goal = forms.FloatField(label="How much Quid do you wanna Git?")


    class Meta:
        # Provide an association between the ModelForm and a model
        model = Project
        fields = ('name', 'description', 'title_image', 'body', 'goal', 'published')
        widgets = {

            'title_image': forms.FileInput(attrs={'class': 'custom-file', 'id': "custom-file"}),

        }


class DonationForm(forms.ModelForm):
    amount = forms.FloatField(label="Amount")
    comment = forms.CharField(label="", max_length=Donation.comMaxLen, required=False,
                              widget=forms.Textarea(attrs={'placeholder':'Leave a comment if you wish!'}))
    class Meta:
        model = Donation
        fields = ('amount', 'comment')
