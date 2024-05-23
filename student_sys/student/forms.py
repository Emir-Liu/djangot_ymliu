from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    def clean_qq(self):
        # print('self.cleaned_data:{}'.format(self.cleaned_data))
        cleaned_data = self.cleaned_data['qq']

        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字')

        return int(cleaned_data)

    class Meta:
        model = Student

        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )