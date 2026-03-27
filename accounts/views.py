from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Avg, Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import CreateView, DetailView

from .forms import RegisterForm, StudentForm
from .models import Student


@method_decorator(never_cache, name="dispatch")
class AppLoginView(LoginView):
    template_name = "accounts/login.html"


@method_decorator(never_cache, name="dispatch")
class AppLogoutView(LogoutView):
    pass


@login_required
def dashboard(request):
    return render(
        request,
        "accounts/dashboard.html",
        {
            "student_count": Student.objects.count(),
            "user_count": User.objects.count(),
            "avg_age": Student.objects.aggregate(avg_age=Avg("age")).get("avg_age"),
        },
    )


@login_required
def student_list(request):
    query = request.GET.get("q", "").strip()
    branch = request.GET.get("branch", "").strip()
    order = request.GET.get("order", "username")

    students = Student.objects.all()

    if query:
        students = students.filter(Q(username__icontains=query) | Q(email__icontains=query))
    if branch:
        students = students.filter(branch=branch)

    allowed_orders = {"username", "-username", "age", "-age"}
    if order not in allowed_orders:
        order = "username"
    students = students.order_by(order)

    branch_summary = Student.objects.values("branch").annotate(total=Count("id")).order_by("-total")
    stats = Student.objects.aggregate(total_students=Count("id"), average_age=Avg("age"))

    return render(
        request,
        "accounts/student_list.html",
        {
            "students": students,
            "query": query,
            "branch": branch,
            "order": order,
            "branch_summary": branch_summary,
            "stats": stats,
            "branches": Student._meta.get_field("branch").choices,
        },
    )


@login_required
@permission_required("accounts.add_student", raise_exception=True)
def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student created successfully.")
        return redirect("student_list")
    return render(request, "accounts/add_student.html", {"form": form, "view_type": "FBV"})


@login_required
@permission_required("accounts.delete_student", raise_exception=True)
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted.")
    return redirect("student_list")


class StudentCreateCBV(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "accounts/add_student.html"
    success_url = "/accounts/students/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        if not request.user.has_perm("accounts.add_student"):
            messages.error(request, "You don't have permission to add students.")
            return redirect("student_list")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "CBV"
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = "accounts/student_detail.html"
    context_object_name = "student"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Account created and logged in.")
        return redirect("dashboard")
    return render(request, "accounts/register.html", {"form": form})


@login_required
def user_list(request):
    users = User.objects.all().order_by("username")
    return render(request, "accounts/user_list.html", {"users": users})