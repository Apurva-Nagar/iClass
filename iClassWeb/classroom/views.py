from django.shortcuts import render, redirect
from .models import Classroom, Notes, Assignment, AssignmentAnswers
from accounts.models import Teacher, Student
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import UploadNotesForm, UploadAssignmentForm
import datetime



class TeacherDashboard(TemplateView):
    template_name = 'classroom/teacher_dashboard.html'


class StudentDashboard(TemplateView):
    template_name = 'classroom/student_dashboard.html'


class CreateClassroom(CreateView):
    model = Classroom
    fields = ['room_no', 'course']
    template_name = 'classroom/create_classroom.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        classroom_teacher = Teacher.objects.get(user=self.request.user)
        obj.teacher = classroom_teacher
        obj.save()
        return redirect('classroom:teacher_dashboard')


class AllClassrooms(ListView):
    model = Classroom
    template_name = 'classroom/list_classroom.html'

    def get_queryset(self):
        teacher = self.request.user
        teacher_id = teacher.id
        return Classroom.objects.filter(teacher=teacher_id)


class DetailClassroom(DetailView):
    model = Classroom
    template_name = 'classroom/detail_classroom.html'


class EditClassroom(UpdateView):
    model = Classroom
    fields = ['room_no', 'course']
    template_name = 'classroom/edit_classroom.html'
    success_url = reverse_lazy('classroom:classroom_list')


class DeleteClassroom(DeleteView):
    model = Classroom
    template_name = 'classroom/delete_classroom.html'
    success_url = reverse_lazy('classroom:classroom_list')


class JoinClassroom(UpdateView):
    model = Classroom
    fields = []
    template_name = 'classroom/join_classroom.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        classroom_student = Student.objects.get(user=self.request.user)
        obj.student.add(classroom_student)
        obj.save()
        return redirect('classroom:student_dashboard')        


class AllClassroomsStudent(ListView):
    model = Classroom
    template_name = 'classroom/list_classroom_student.html'

    def get_queryset(self):
        student = self.request.user
        student_id = student.id
        return Classroom.objects.filter(student=student_id)

        
class DetailClassroomStudent(DetailView):
    model = Classroom
    template_name = 'classroom/detail_classroom_student.html'


class UploadNotes(CreateView):
    form_class = UploadNotesForm
    template_name = 'classroom/upload_notes.html'

    def get_form_kwargs(self):
        kwargs = super(UploadNotes, self).get_form_kwargs()
        teacher = self.request.user
        kwargs['teacher_id'] = teacher.id
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        classroom = self.request.POST['classroom']
        current_classroom = Classroom.objects.get(pk=classroom)
        obj.classroom = current_classroom
        obj.save()
        return redirect('classroom:teacher_dashboard')


class UploadAssignment(CreateView):
    form_class = UploadAssignmentForm
    template_name = 'classroom/upload_assignment.html'

    def get_form_kwargs(self):
        kwargs = super(UploadAssignment, self).get_form_kwargs()
        teacher = self.request.user
        kwargs['teacher_id'] = teacher.id
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        classroom = self.request.POST['classroom']
        current_classroom = Classroom.objects.get(pk=classroom)
        obj.classroom = current_classroom
        obj.save()
        return redirect('classroom:teacher_dashboard')


class UploadAssignmentAnswer(CreateView):
    model = AssignmentAnswers
    fields = ['assignment_answer']
    template_name = 'classroom/upload_assignment_answers.html'

    def form_valid(self, form, **kwargs):
        obj = form.save(commit=False)
        assignment_id = self.kwargs['assignment_pk']
        current_assignment = Assignment.objects.get(pk=assignment_id)
        obj.assignment = current_assignment

        current_student = Student.objects.get(user=self.request.user)
        obj.student = current_student
        
        obj.is_submitted = True
        obj.save()
        return redirect('classroom:student_dashboard') 


class AssignmentSubmissions(DetailView):
    model = Assignment
    template_name = 'classroom/assignment_submissions.html'




