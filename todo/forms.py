from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

from todo.models import Item

'''
class TodoForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    description = forms.CharField(max_length=1024, required=False)
    date_due = forms.DateField(widget = SelectDateWidget, required=Falsei)
'''

class TodoForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('done', 'hidden')
        
    def clean(self):
        self.instance.datetime_due=self.cleaned_data.get('datetime_due')
        return self.cleaned_data
