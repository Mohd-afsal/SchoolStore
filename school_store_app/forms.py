from django import forms

from school_store_app.models import Courses, Detail, Departments, Materials


class DetailCreationForm(forms.ModelForm):
    MATERIALS_CHOICES = [
        ('Pen', 'Pen'),
        ('Exam papers', 'Exam papers'),
        ('Debit notebook', 'Debit notebook'),
    ]
    materials = forms.MultipleChoiceField(choices=MATERIALS_CHOICES, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Detail
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Name'}),
            'dob': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.widgets.RadioSelect(attrs={'type': 'radio', 'name': 'gender', 'class': 'from-control'}),
            'phone_number': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Phone Number'}),
            'mail': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'E-mail'}),
            'address': forms.Textarea(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Enter your full address'}),
        }

        labels = {
            'name': "",
            "dob": "Date of birth",
            "age": "",
            "gender": "Gender",
            "phone_number": "",
            "mail": "",
            "address": "",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Courses.objects.none()
        # self.fields['materials'] = forms.ModelMultipleChoiceField(
        #     queryset=Materials.objects.values_list('name', flat=True),
        #     widget=forms.CheckboxSelectMultiple
        # )
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Courses.objects.filter(department_id=department_id).all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
