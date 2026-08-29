from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.apps import apps
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from users.models import Profile

def home(request):
    return render(request,"home.html")

def category(request):
    model = apps.get_model('law', 'lawtablelist')
    data = model.objects.values('category', 'description').distinct()
    # Deduplicate by category name
    seen = set()
    unique_data = []
    for item in data:
        if item['category'] not in seen:
            seen.add(item['category'])
            unique_data.append(item)
    return render(request, "categories.html", {'data': unique_data})

def acts(request, tname):
    model = apps.get_model('law','lawtablelist')
    data = model.objects.filter(category=tname)
    return render(request,"acts.html",{'data':data,'tname':tname})

def chapter(request, tname, act):
    model = apps.get_model('law',act)
    data = model.objects.values('chapter','name').distinct()
    mod = apps.get_model('law','lawtablelist')
    Aname = mod.objects.filter(tname=act)
    return render(request,"chapter.html",{'data':data,'Aname':Aname,'tname':tname,'act':act})

def section(request, tname, act, no):
    model = apps.get_model('law',act)
    data = model.objects.filter(chapter=no) 
    mod = apps.get_model('law','lawtablelist')
    Aname = mod.objects.filter(tname=act)
    return render(request, "section.html", {'data': data,'Aname':Aname, 'tname':tname,'act':act,'cno': no})

def law_detail(request, tname, act, cno, lno):
    model = apps.get_model('law',act)
    data = model.objects.filter(section=lno)
    return render(request, "lawdetails.html", {'data': data, 'tname': tname, 'act': act, 'chapter_number': cno})

def quick_law_redirect(request, act, section_id):
    try:
        # Get category from Lawtablelist where tname == act
        law_table = apps.get_model('law', 'lawtablelist').objects.get(tname=act)
        category = law_table.category
        
        # Get chapter from the specific act table
        model = apps.get_model('law', act)
        law_obj = model.objects.filter(section=section_id).first()
        if not law_obj:
            return redirect('home')
        
        chapter = law_obj.chapter
        
        # Build the exact URL for the detailed page
        url = reverse('lawdetails', kwargs={
            'tname': category,
            'act': act,
            'cno': chapter,
            'lno': section_id
        })
        return redirect(url)
    except Exception:
        return redirect('home')

def ocr_page_view(request):
    return render(request, "ocr.html")

@login_required(login_url='login')
def bookmarks_page_view(request):
    return render(request, "bookmarks.html")

@login_required(login_url='login')
def profile_page_view(request):
    return render(request, "profile.html")

@login_required(login_url='login')
def dashboard_page_view(request):
    return render(request, "dashboard.html")

@login_required(login_url='login')
def admin_dashboard_page_view(request):
    return render(request, "admin_dashboard.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    error_msg = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            error_msg = "Invalid username or password."
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error_msg': error_msg})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    error_msg = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a Profile for the user (Bug 18 fix)
            Profile.objects.get_or_create(user=user, defaults={'role': 'citizen'})
            login(request, user)
            return redirect('dashboard')
        else:
            error_msg = "Registration failed. Password might be too weak or mismatch."
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form, 'error_msg': error_msg})


