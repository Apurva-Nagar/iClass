from django import template
from classroom.models import Notes

register = template.Library()

@register.filter
def filter_notes_items(self):
    return Notes.objects.filter(classroom=self.id)