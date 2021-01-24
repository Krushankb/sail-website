from django.shortcuts import render

def home(request):
    return render(request, 'public/home.html', {'display_footer':True})

def about(request):
    return render(request, 'public/about.html', {'title':'About', 'display_footer':True})

def staff(request):
    return render(request, 'public/staff.html', {'title':'Staff', 'display_footer':True})

def teachers(request):
    return render(request, 'public/teacher-info.html', {'title': 'Teacher Info', 'display_footer': True})