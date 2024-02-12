from django import forms
from rango.models import Page, Category
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
from rango.models import UserProfile
>>>>>>> 3aad359ab85a6c495c7cda84e8e25252d0da2bbd

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
        help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

<<<<<<< HEAD
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Category with this Name already exists.")
        return name

=======
>>>>>>> 3aad359ab85a6c495c7cda84e8e25252d0da2bbd
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
        help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
        help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

<<<<<<< HEAD
=======
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data

>>>>>>> 3aad359ab85a6c495c7cda84e8e25252d0da2bbd
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values; we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include (don't include the category field).
        #fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

<<<<<<< HEAD
=======
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


>>>>>>> 3aad359ab85a6c495c7cda84e8e25252d0da2bbd
