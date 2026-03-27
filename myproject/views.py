from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def handler400(request, exception):
    return render(request, "400.html", status=400)


def handler403(request, exception):
    return render(request, "403.html", status=403)


def handler404(request, exception):
    return render(request, "404.html", status=404)


def handler500(request):
    return render(request, "500.html", status=500)

    