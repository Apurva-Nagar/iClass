from django.urls import path, re_path
from classroom.views import TeacherDashboard, StudentDashboard, CreateClassroom, AllClassrooms, DetailClassroom, EditClassroom, DeleteClassroom, JoinClassroom, AllClassroomsStudent, UploadNotes, DetailClassroomStudent, UploadAssignment, UploadAssignmentAnswer, AssignmentSubmissions



urlpatterns = [
	path('teacher/', TeacherDashboard.as_view(), name='teacher_dashboard'),
    path('student/', StudentDashboard.as_view(), name='student_dashboard'),
    path('create/', CreateClassroom.as_view(), name='create_classroom'),
    path('teacher/all_classrooms/', AllClassrooms.as_view(), name='classroom_list'),
    re_path(r'teacher/view_class/(?P<classroom_code>[0-9a-f-]+)/(?P<pk>\d+)/$', DetailClassroom.as_view(), name='classroom_detail'),
    re_path(r'teacher/delete_class/(?P<classroom_code>[0-9a-f-]+)/(?P<pk>\d+)/$', DeleteClassroom.as_view(), name='classroom_delete'),
    re_path(r'teacher/edit_class/(?P<classroom_code>[0-9a-f-]+)/(?P<pk>\d+)/$', EditClassroom.as_view(), name='classroom_edit'),
    re_path(r'student/join_class/(?P<classroom_code>[0-9a-f-]+)/(?P<pk>\d+)/$', JoinClassroom.as_view(), name='classroom_join'),
    path('student/all_classrooms/', AllClassroomsStudent.as_view(), name='classroom_list_student'),
    path('teacher/upload_notes/', UploadNotes.as_view(), name='upload_notes'),
    re_path(r'student/view_class/(?P<classroom_code>[0-9a-f-]+)/(?P<pk>\d+)/$', DetailClassroomStudent.as_view(), name='classroom_detail_student'),
    path('teacher/upload_assignment/', UploadAssignment.as_view(), name='upload_assignment'),
    re_path(r'student/upload_assignment_answer/(?P<assignment_pk>\d+)/$', UploadAssignmentAnswer.as_view(), name='upload_assignment_answer'),
    re_path(r'teacher/assignment/submissions/(?P<pk>\d+)/$', AssignmentSubmissions.as_view(), name='assignment_submissions')

]










