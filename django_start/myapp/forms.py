from django import forms

from myapp.models import Task, User


class userForm(forms.Form):
    
    contact=forms.IntegerField(max_value=9999999999, required=False, widget=forms.NumberInput(attrs={ 'class': 'form-control mb-3'}))


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status", "priority"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Prepare sprint report"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Add task details"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "work_update", "due_date", "status", "priority"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Prepare sprint report"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Add task details"}),
            "work_update": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Write what has been done so far"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "priority": forms.Select(attrs={"class": "form-select"}),
        }