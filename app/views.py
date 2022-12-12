from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    template = 'main/mainpage/index.html'
    message = "Order is successfully created" 

    form = OrderForm()

    about=About.objects.first()
    settings=Settings.objects.first()
    category=Category.objects.all()
    graphics = Service.objects.filter(category="Graphics")
    photography = Service.objects.filter(category="Photography")
    videography = Service.objects.filter(category="Videography").first()
    team = Team.objects.filter(position="Managing Director").first()
    hero = Hero.objects.first()
    testmony = Testmony.objects.all()
    facebook = SocialMedia.objects.filter(name="facebook")
    instagram = SocialMedia.objects.filter(name="instagram")
    twitter = SocialMedia.objects.filter(name="twitter")
    linkedin = SocialMedia.objects.filter(name="linkedin")
    tiktok = SocialMedia.objects.filter(name="tiktok")



     
    context = {
        'form':form,
        'about':about,
        'settings':settings,
        'category':category,
        'graphics':graphics,
        'photography':photography,
        'videography':videography,
        'hero':hero,
        'testmony':testmony,
        'facebook':facebook,
        'instagram':instagram,
        'twitter':twitter,
        'linkedin':linkedin,
        'tiktok':tiktok,
        'team':team
    }  
    return render(request, template, context)


@login_required
def dashboard(request):
    template = 'dashboard/index.html'
    designer = Team.objects.filter(position="Designer").count()
    photographer = Team.objects.filter(position="Photographer").count()
    videographer = Team.objects.filter(position="Videographer").count()
    order = Order.objects.all().count()
    settings=Settings.objects.first()
    context = {
        'settings':settings,
        'designer':designer,
        'photographer':photographer,
        'videographer':videographer,
        'order':order
    }
    return render(request, template, {})   


def get_about(request):
    template = 'main/mainpage/about.html'
    about=About.objects.first()
    settings=Settings.objects.first()
    context={
        'about':about,
        'settings':settings
    }
    return render(request, template, context)  


def get_product(request):
    template = 'main/mainpage/product.html'
    graphics = Service.objects.filter(category="Graphics")
    photography = Service.objects.filter(category="Photography")
    videography = Service.objects.filter(category="Videography")
    settings=Settings.objects.first()
    context={
        'graphics':graphics,
        'photography':photography,
        'videography':videography,
        'settings':settings
    }
    return render(request, template, context) 


def get_service(request):
    template = 'main/mainpage/service.html'
    graphics = Service.objects.filter(category="Graphics").first()
    photography = Service.objects.filter(category="Photography").first()
    videography = Service.objects.filter(category="Videography").first()
    context={
        'graphics':graphics,
        'photography':photography,
        'videography':videography
    }
    return render(request, template, {})     




#About us Crud Operation
@login_required
def  create_about(request):
    template = "about/add.html"
    title = "Create About us"  
    message = "About is successfully created" 

    form = AboutForm()

    if request.method == "POST":
        form = AboutForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:about")
        else:
            messages.error(request,"Sorry Something is wrong")
    about = About.objects.first()        
    context = {
        'title':title,
        'form':form,
        'about':about
    }  
    return render(request, template, context)

@login_required
def  edit_about(request):
    template = "about/edit.html"
    title = "Edit About us"  
    message = "About is successfully edited" 

    about_id = About.objects.first()

    about = get_object_or_404(About, id=about_id.id)

    form = AboutForm(request.POST or None, instance=about)

    if request.method == "POST":
        form = AboutForm(request.POST or None,instance=about)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:about")
        else:
            messages.error(request,"Sorry Something is wrong")
    context = {
        'title':title,
        'form':form,
    }  
    return render(request, template, context)    

@login_required
def delete_about(request, id):
    message = "About is successfully Deleted" 
    about = get_object_or_404(About, pk=id)
    about.delete()
    messages.success(request,message)
    return redirect('app:about') 


# Hero Crud Operations    
@login_required
def  create_hero(request):
    template = "category/list.html"
    title = "Create Hero"  
    message = "Hero is successfully created" 

    form = HeroForm()

    if request.method == "POST":
        form = CategoryForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:hero")
        else:
            messages.error(request,"Sorry Something is wrong")
    hero = Hero.objects.first()   
    form = HeroForm()     
    context = {
        'title':title,
        'form':form,
        'hero':hero,
    }  
    return render(request, template, context)

@login_required
def  edit_hero(request):
    template = "category/edit.html"
    title = "Edit hero"  
    message = "hero is successfully edited" 

    id=Hero.objects.first()

    hero = get_object_or_404(Hero, id=id.id)

    form = HeroForm(request.POST or None, request.FILES,instance=hero)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:hero")
        else:
            messages.error(request,"Sorry Something is wrong")
    context = {
        'title':title,
        'form':form,
    }  
    return render(request, template, context)    

@login_required
def delete_hero(request, id):
    message = "Hero is successfully Deleted" 
    hero = get_object_or_404(Hero, pk=id)
    hero.delete()
    messages.success(request,message)
    return redirect('app:hero') 



# Testmony Crud Operations    
@login_required
def  create_testmony(request):
    template = "testmony/list.html"
    title = "Create Testmony"  
    message = "Testmony is successfully created" 

    form = TestmonyForm()

    if request.method == "POST":
        form = TestmonyForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:testmony")
        else:
            messages.error(request,"Sorry Something is wrong")
    testmony = Testmony.objects.all()        
    context = {
        'title':title,
        'form':form,
        'testmony':testmony,
    }  
    return render(request, template, context)

@login_required
def  edit_testmony(request,id):
    template = "testmony/edit.html"
    title = "Edit testmony"  
    message = "testmony is successfully edited" 

    testmony = get_object_or_404(Testmony, id=id)

    form = TestmonyForm(request.POST or None, request.FILES,instance=testmony)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:testmony")
        else:
            messages.error(request,"Sorry Something is wrong")
    context = {
        'title':title,
        'form':form,
    }  
    return render(request, template, context)    

@login_required
def delete_testmony(request, id):
    message = "Testmony is successfully Deleted" 
    testmony = get_object_or_404(testmony, pk=id)
    testmony.delete()
    messages.success(request,message)
    return redirect('app:testmony') 



# service crud operation
@login_required
def  create_service(request):
    template = "service/list.html"
    title = "Create Service"  
    message = "Service is successfully created" 

    form = ServiceForm(request.POST or None)

    if request.method == "POST":
        form = ServiceForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:service")
        else:
            messages.error(request,"Sorry Something is wrong")
    service = Service.objects.all()        
    context = {
        'title':title,
        'form':form,
        'service':service,
    }  
    return render(request, template, context)

@login_required
def  edit_service(request,id):
    template = "service/edit.html"
    title = "Edit service"  
    message = "service is successfully edited" 

    service = get_object_or_404(Service,pk=id)

    form = ServiceForm(instance=service)

    if request.method == 'POST':
        form = ServiceForm(request.POST or None,request.FILES,instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:service")
        else:
            messages.error(request,"Sorry Something is wrong")
    context = {
        'title':title,
        'form':form,
        
    }  
    return render(request, template, context)    

   
@login_required
def delete_service(request, id):
    message = "Service is successfully Deleted" 
    service = get_object_or_404(Service, pk=id)
    service.delete()
    messages.success(request,message)
    return redirect('app:service') 


# Settings crud operation
@login_required
def  create_settings(request):
    template = "settings/company.html"
    title = "Create Settings"  
    message = "Settings is successfully created" 

    form = SettingsForm()

    if request.method == "POST":
        form = SettingsForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:settings")
        else:
            messages.error(request,"Sorry Something is wrong")
    setting = Settings.objects.first()  
    about = About.objects.first()      
    context = {
        'title':title,
        'form':form,
        'setting':setting,
        'about':about,
    }  
    return render(request, template, context)

@login_required
def  edit_settings(request):
    template = "settings/edit.html"
    title = "Edit settings"  
    message = "settings is successfully edited" 

    setting_id=Settings.objects.first()

    settings = get_object_or_404(Settings, id=setting_id.id)

    form = SettingsForm(instance=settings)

    if request.method == "POST":
        form = SettingsForm(request.POST or None,request.FILES,instance=settings)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:settings")
        else:
            messages.error(request,"Sorry Something is wrong")
    context = {
        'title':title,
        'form':form,
    }  
    return render(request, template, context)    

@login_required
def delete_settings(request, id):
    message = "Settings is successfully Deleted" 
    settings = get_object_or_404(Settings, id=id)
    settings.delete()
    messages.success(request,message)
    return redirect('app:settings') 


# Team crud Operation
@login_required
def  create_team(request):
    template = "team/list.html"
    title = "Create Team"  
    message = "Team is successfully created" 

    form = TeamForm(request.POST or None)

    if request.method == "POST":
        form = TeamForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:team")
        else:
            messages.error(request,"Sorry Something is wrong")
    team = Team.objects.all()      
    context = {
        'title':title,
        'form':form,
        'team':team,
    }  
    return render(request, template, context)

@login_required
def  edit_team(request,id):
    template = "team/edit.html"
    title = "Edit Team"  
    message = "Team is successfully edited" 

    team = get_object_or_404(Team, id=id)

    form = TeamForm(instance=team)

    if request.method == "POST":
        form = TeamForm(request.POST or None,request.FILES,instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:team")
        else:
            messages.error(request,"Sorry Something is wrong")
    context = {
        'title':title,
        'form':form,
    }  
    return render(request, template, context)    

@login_required
def delete_team(request, id):
    message = "Settings is successfully Deleted" 
    team = get_object_or_404(Team, pk=id)
    team.delete()
    messages.success(request,message)
    return redirect('app:team')   



def create_order(request):
    message = "Order is successfully created" 
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, message)
        else:
            messages.error(request,form.errors) 
            print(form.errors)
                  
    return redirect("app:index")



# order operations
@login_required
def list_order(request):
    template = "order/list.html"

    order = Order.objects.all()

    context = {
        'order':order,
    }

    return render(request, template, context)



# social Media crud operation
@login_required
def  create_link(request):
    template = "social/list.html"
    title = "Create Social Media Links"  
    message = "Links is successfully created" 

    form = SocialMediaForm(request.POST or None)

    if request.method == "POST":
        form = SocialMediaForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:social")
        else:
            messages.error(request,"Sorry Something is wrong")
    link = SocialMedia.objects.all()        
    context = {
        'title':title,
        'form':form,
        'link':link,
    }  
    return render(request, template, context)

@login_required
def  edit_link(request,id):
    template = "social/edit.html"
    title = "Edit social media link"  
    message = "link is successfully edited" 

    link = get_object_or_404(SocialMedia,pk=id)

    form = SocialMediaForm(instance=link)

    if request.method == 'POST':
        form = SocialMediaForm(request.POST or None,instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, message)
            return redirect("app:social")
        else:
            messages.error(request,"Sorry Something is wrong")
    context = {
        'title':title,
        'form':form,
        
    }  
    return render(request, template, context)    

   
@login_required
def delete_link(request, id):
    message = "Service is successfully Deleted" 
    link = get_object_or_404(SocialMedia, pk=id)
    link.delete()
    messages.success(request,message)
    return redirect('app:social') 
    
