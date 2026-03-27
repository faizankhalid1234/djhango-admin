from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)
    branch = models.CharField(
        max_length=100,
        choices=[
            ('CSE', 'Computer Science and Engineering'),
            ('ECE', 'Electronics and Communication Engineering'),
            ('ME', 'Mechanical Engineering')
        ]
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username"]

   