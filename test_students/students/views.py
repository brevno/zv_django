from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Student, Course, Rating
from .forms import StudentRatesEditForm


class IndexViewWithAverage(generic.ListView):
    def get_context_data(self, **kwargs):
        data = super(IndexViewWithAverage, self).get_context_data(**kwargs)
        data['total_average'] = Rating.average_rate()
        return data


class ViewWithCancelButtonMixin(object):
    def post(self, request, *args, **kwargs):
        if 'cancel' in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(ViewWithCancelButtonMixin, self).post(request, *args, **kwargs)


class IndexView(IndexViewWithAverage):
    template_name = 'students/students.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all()


class CoursesView(IndexViewWithAverage):
    template_name = 'students/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

class AddStudentView(ViewWithCancelButtonMixin, generic.CreateView):
    template_name = 'students/add_student.html'
    model = Student
    success_url = reverse_lazy('students')
    fields = ['name']


class DeleteStudentView(generic.DeleteView):
    model = Student
    success_url = reverse_lazy('students')


class AddCourseView(ViewWithCancelButtonMixin, generic.CreateView):
    template_name = 'students/add_course.html'
    model = Course
    success_url = reverse_lazy('courses')
    fields = ['name']


class DeleteCourseView(generic.DeleteView):
    model = Course
    success_url = reverse_lazy('courses')


class EditRatesView(ViewWithCancelButtonMixin, generic.FormView):
    template_name = 'students/edit_rates.html'
    form_class = StudentRatesEditForm
    success_url = reverse_lazy('students')

    def get_initial(self):
        return {'student': self.kwargs['student_id']}

    def form_valid(self, form):
        student = Student.objects.get(id=form.cleaned_data['student'])
        course = form.cleaned_data['course']
        rating, _ = Rating.objects.get_or_create(student=student, course=course)
        rating.rate = form.cleaned_data['rate']
        rating.save()

        return super(EditRatesView, self).form_valid(form)
