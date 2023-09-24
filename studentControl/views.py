from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Importing all necessary models 
from studentControl.models import Discipline
from studentControl.models import Student
from studentControl.models import Task

# Importing all necessary serializers
from studentControl.serializers import DisciplineSerializer
from studentControl.serializers import StudentSerializer
from studentControl.serializers import TaskSerializer



# STUDENT VIEWS
class StudentView(APIView):

    # List of Students
    def get(self, request):
        try:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)

        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Creating Student
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
class StudentDetailView(APIView):

    # Student details
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)

        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Modifying a Student
    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student,data=request.data)

        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deleting a Student
    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()

        except:
            return Response(status[status.HTTP_400_BAD_REQUEST])
        
        return Response(status=status.HTTP_204_NO_CONTENT)





# DISCIPLINE VIEWS
class DisciplineView(APIView):

    # List of Disciplines
    def get(self, request):
        try:
            disciplines = Discipline.objects.all()
            serializer = DisciplineSerializer(disciplines, many=True)

        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Creating Discipline
    def post(self, request):
        serializer = DisciplineSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DisciplineDetailView(APIView):

    # Discipline details
    def get(self, request, pk):
        try:
            discipline = Discipline.objects.get(pk=pk)
            serializer = DisciplineSerializer(discipline)
        
        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Modifying a Discipline
    def put(self, request, pk):
        try:
            discipline = Discipline.objects.get(pk=pk)
            serializer = DisciplineSerializer(discipline,data=request.data)
        
        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)    
        
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deleting a Discipline
    def delete(self, request, pk):
        try:
            discipline = Discipline.objects.get(pk=pk)
            discipline.delete()
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)





# TASK VIEWS
class TaskView(APIView):

    # List Tasks
    def get(self, request):
        try:
            task = Task.objects.all()
            serializer = TaskSerializer(task, many=True)
        
        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Add Task
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):

    # Task details
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)

        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Modifying Task
    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task,data=request.data)
        
        except:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deleting Task
    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    




# STUDENTTASK VIEW
class StudentTasksView(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            tasks = Task.objects.filter(student=student)
            
            student_serializer = StudentSerializer(student)
            task_serializer = TaskSerializer(tasks, many=True)
            
            data = {
                "student": student_serializer.data,
                "tasks": task_serializer.data
            }
            
            return Response(data, status=status.HTTP_200_OK)
        except Student.DoesNotExist:

            return Response(status=status.HTTP_400_BAD_REQUEST)