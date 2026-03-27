from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=50, default="", help_text="Enter student's first name")
    last_name = models.CharField(max_length=50, default="", help_text="Enter student's last name")
    username = models.CharField(max_length=150, unique=True, help_text="Unique username for the student")
    email = models.EmailField(unique=True, help_text="Student's email address")
    phone = models.CharField(max_length=15, blank=True, null=True, help_text="Contact phone number")

    # Academic Information
    age = models.IntegerField(
        validators=[MinValueValidator(16), MaxValueValidator(100)],
        help_text="Age must be between 16 and 100"
    )
    branch = models.CharField(
        max_length=100,
        choices=[
            ('CSE', 'Computer Science and Engineering'),
            ('ECE', 'Electronics and Communication Engineering'),
            ('ME', 'Mechanical Engineering'),
            ('CE', 'Civil Engineering'),
            ('EE', 'Electrical Engineering'),
        ],
        help_text="Select the branch of study"
    )
    enrollment_year = models.IntegerField(
        default=2024,
        validators=[MinValueValidator(2000), MaxValueValidator(2030)],
        help_text="Year of enrollment"
    )
    gpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(4.0)],
        help_text="Grade Point Average (0.0 to 4.0)"
    )

    # Media
    image = models.ImageField(upload_to='student_images/', blank=True, null=True, help_text="Upload student photo")

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age_category(self):
        if self.age < 20:
            return "Undergraduate"
        elif self.age < 25:
            return "Graduate"
        else:
            return "Post-Graduate"

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Student"
        verbose_name_plural = "Students"
        unique_together = ['email', 'username']

   