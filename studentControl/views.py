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
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

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
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Modifying a Student
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student,data=request.data)
        
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deleting a Student
    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)






# DISCIPLINE VIEWS
class DisciplineView(APIView):

    # List of Disciplines
    def get(self, request):
        disciplines = Discipline.objects.all()
        serializer = DisciplineSerializer(disciplines, many=True)

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
        discipline = Discipline.objects.get(pk=pk)
        serializer = DisciplineSerializer(discipline)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Modifying a Discipline
    def put(self, request, pk):
        discipline = Discipline.objects.get(pk=pk)
        serializer = DisciplineSerializer(discipline,data=request.data)
        
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deleting a Discipline
    def delete(self, request, pk):
        discipline = Discipline.objects.get(pk=pk)
        discipline.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)







# TASK VIEWS
class TaskView(APIView):

    def get(self, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



class TaskDetailView(APIView):

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task,data=request.data)
        
        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StudentTasksView(APIView):
    def get(self, request, student_id):
        try:
            student = Student.objects.get(pk=student_id)
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