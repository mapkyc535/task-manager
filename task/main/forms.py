from django import forms
from .models import Tasks


class ViewTaskForm(forms.Form):
    number = forms.IntegerField(label='Номер задачи', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Номер задачи', 'aria-labe': 'Номер задачи'}))


class AddTaskForm(forms.ModelForm):

    class Meta:
        model = Tasks
        fields = ['title', 'text', 'date_of_completion']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_of_completion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class StatusTaskForm(forms.ModelForm):
    id = forms.IntegerField(label='Номер задачи', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Номер задачи', 'aria-labe': 'Номер задачи'}))

    class Meta:
        model = Tasks
        fields = ['status', ]