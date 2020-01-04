from django.forms import ModelForm
from .models import Notes, Classroom, Assignment


class UploadNotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['classroom', 'notes_heading', 'notes_file']

    def __init__(self, *args, **kwargs):
        teacher_id = kwargs.pop('teacher_id')
        super(UploadNotesForm, self).__init__(*args, **kwargs)
        self.fields['classroom'].queryset = Classroom.objects.filter(teacher=teacher_id)


class UploadAssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['classroom', 'assignment_question', 'assignment_heading', 'deadline']

    def __init__(self, *args, **kwargs):
        teacher_id = kwargs.pop('teacher_id')
        super(UploadAssignmentForm, self).__init__(*args, **kwargs)
        self.fields['classroom'].queryset = Classroom.objects.filter(teacher=teacher_id)