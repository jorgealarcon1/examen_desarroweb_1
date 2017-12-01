from django import forms

from .models import Car

class CarModelForm(forms.ModelForm):
    """docstring for ."""
    content = forms.CharField(label='',
                                widget=forms.Textarea(
                                        attrs={'placeholder':"Car",
                                                'class': "textarea"}
                                ))
#        super(, self).__init__()
#        self.arg = arg

    class Meta:
        model = Car
        fields = "__all__"
