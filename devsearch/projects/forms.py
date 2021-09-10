from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__' # All the fields of the model
        fields = ['title', 'featured_image','description', 'demo_link', 'source_link', 'tags']