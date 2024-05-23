from django.http import HttpResponseRedirect
from django.shortcuts import render
from  django.urls import reverse

from .forms import StudentForm
from .models import Student

from django.views import View

# Create your views here.

class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students,
        }

        return context

    def get(self, request):
        context = self.get_context()
        form = StudentForm()

        context.update(
            {
                'form': form
            }
        )
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # return render(request, self.template_name)
            return HttpResponseRedirect(reverse('index'))

        context = self.get_context()

        context.update(
            {
                'form': form
            }
        )

        return render(request, self.template_name, context=context)

def index(request):

    # students = Student.objects.all()
    students = Student.get_all()
    print('students:{}'.format(students))

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            # clean_data = form.cleaned_data
            # student = Student()
            # student.name = clean_data['name']
            # student.sex = clean_data['sex']
            # student.email = clean_data['email']
            # student.profession = clean_data['profession']
            #
            # student.qq = clean_data['qq']
            #
            # student.phone = clean_data['phone']
            #
            # student.save()
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }

    return render(request, 'index.html', context=context)