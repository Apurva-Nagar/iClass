from django.db import models
from accounts.models import Teacher, Student
import uuid
from django.urls import reverse


class Classroom(models.Model):

    room_no = models.IntegerField()
    course = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.course + '-' + str(self.room_no)


class Notes(models.Model):

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    notes_file = models.FileField(upload_to='notes_file')
    notes_heading = models.CharField(max_length=200, default='Notes Topic')


class Assignment(models.Model):

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    assignment_question = models.FileField(upload_to='assignment_question')
    assignment_heading = models.CharField(max_length=200, default='Assignment Topic')
    deadline = models.DateTimeField()


class AssignmentAnswers(models.Model):

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignment')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    assignment_answer = models.FileField(upload_to='assignment_answer')
    is_submitted = models.BooleanField(default=False)




    
