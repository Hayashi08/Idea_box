from django import forms

from .models import Idea,Conclusion

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Idea
        fields = ('idea','description', 'image',)

class ConclusionForm(forms.ModelForm):

    class Meta:
        model = Conclusion
        fields = ('conclusion', 'description', 'image',)