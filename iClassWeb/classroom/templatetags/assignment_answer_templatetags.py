from django import template
from classroom.models import AssignmentAnswers

register = template.Library()

@register.filter
def filter_assignment_answer_items(self, current_student):
    return AssignmentAnswers.objects.filter(assignment=self.id, student=current_student)