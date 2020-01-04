from django import template
from classroom.models import AssignmentAnswers

register = template.Library()

@register.filter
def filter_assignment_answer_number_items(self):
    return AssignmentAnswers.objects.filter(assignment=self.id, is_submitted=True).count()