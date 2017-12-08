from django import forms

from .models import Car

class CarModelForm(forms.ModelForm):
#    make = forms.CharField(label='', widget=forms.TextInput(attrs = {'placeholder':"Make",'class': "textarea"}))
#    Type = forms.CharField(label='', widget=forms.TextInput(attrs = {'placeholder':"Type",'class': "textarea"}))
#    year = forms.CharField(label='', widget=forms.TextInput(attrs = {'placeholder':"year",'class': "textarea"}))
#    colour = forms.CharField(label='', widget=forms.TextInput(attrs = {'placeholder':"colour",'class': "textarea"}))
#    price = forms.CharField(label='', widget=forms.TextInput(attrs = {'placeholder':"price",'class': "textarea"}))
    content = forms.CharField(label='',
                                widget=forms.Textarea(
                                        attrs={'placeholder':"Car",
                                                'class': "textarea"}
                                ))
    class Meta:
        model = Car
#        fields= ["make","Type","year","colour","price",]
        fields = "__all__"
#        fields = [
#            "make",
#            "Type",
#            "year",
#            "colour",
#            "price"
#         ]
