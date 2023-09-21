from django.db import models

# Model for students
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
# Model for disciplines
class Discipline(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Model for tasks
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    dueDate = models.DateField()
    status = models.BooleanField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    discipline = models.ManyToManyField(Discipline)

    def __str__(self):
        return self.name
    