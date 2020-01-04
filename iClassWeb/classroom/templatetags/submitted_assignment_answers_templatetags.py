from django import template
from classroom.models import AssignmentAnswers

register = template.Library()

@register.filter
def filter_submitted_assignment_answers(self):
    return AssignmentAnswers.objects.filter(assignment=self.id, is_submitted=True)