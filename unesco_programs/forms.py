from django import forms
from organizations.models import Organization
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

from .models import UnescoProgram

class UnescoProgramForm(forms.ModelForm):
    organizations = forms.ModelMultipleChoiceField(
        queryset=Organization.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Partners'
    )
    courses = forms.ModelMultipleChoiceField(
        queryset=CourseOverview.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = UnescoProgram
        fields = ['name', 'organizations', 'courses', 'description','website', 'banner_image', 'logo_image']