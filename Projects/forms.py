from django import forms
from .models import ProjectBlog

class ProjectBlogForm(forms.ModelForm):
    class Meta:
        model = ProjectBlog
        fields = ['blogTitle', 'projectTitleImage', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blogTitle'].widget.attrs.update({'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        self.fields['projectTitleImage'].widget.attrs.update({'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})