from django import forms
from .models import *

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.role = 'user'
        if commit:
            user.save()
        return user
    
class PoliceRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    police_profile_fields = ['station_name','police_station_location','helpline_number']  # Add fields from PoliceProfile model here

    for field in police_profile_fields:
        locals()[field] = forms.CharField()  # Create a form field for each PoliceProfile field

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.role = 'police'
        if commit:
            user.save()

            police_profile = PoliceProfile(user=user)
            for field in self.police_profile_fields:
                setattr(police_profile, field, self.cleaned_data.get(field))
            police_profile.save()

        return user

class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.role = 'admin'
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['address', 'phone', 'dob', 'location',  'profile_image', 'guardian_name', 'guardian_phone','guardian_email',]
        

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


# class PoliceProfileForm(forms.ModelForm):
#     class Meta:
#         model = PoliceProfile
#         fields = ['station_name','police_station_location','helpline_number']    


class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=['description']





class SaftytipsForm(forms.ModelForm):
    class Meta:
        model=Saftytips
        fields=['description'] 


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields=['message']            


class PoliceProfileForm(forms.ModelForm):
    class Meta:
        model = PoliceProfile
        fields = ['station_name','police_station_location','helpline_number']       

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')            
