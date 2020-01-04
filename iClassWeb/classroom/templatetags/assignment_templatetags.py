from django import template
from classroom.models import Assignment

register = template.Library()

@register.filter
def filter_assignment_items(self):
    return Assignment.objects.filter(classroom=self.id)