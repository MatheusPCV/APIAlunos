from django.urls import path

from studentControl.views import StudentDetailView
from studentControl.views import StudentView
from studentControl.views import DisciplineDetailView
from studentControl.views import DisciplineView
from studentControl.views import TaskDetailView
from studentControl.views import TaskView
from studentControl.views import StudentTasksView


urlpatterns = [
    path('student/', StudentView.as_view()),
    path('student/<int:pk>/', StudentDetailView.as_view()),
    path('discipline/', DisciplineView.as_view()),
    path('discipline/<int:pk>/', DisciplineDetailView.as_view()),
    path('task/', TaskView.as_view()),
    path('task/<int:pk>/', TaskDetailView.as_view()),
    path('student/<int:student_id>/tasks/', StudentTasksView.as_view())
]