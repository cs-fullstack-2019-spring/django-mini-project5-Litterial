from django.shortcuts import render,redirect,get_object_or_404
from .forms import RecipieInfo,RecipieInfoForm,NewUser,NewUserForm,changeProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request): #goes to home page
    if request.user.is_authenticated:
        current_user= NewUser.objects.get(username=request.user)
        current_recipies=RecipieInfo.objects.filter(keytoNewUser=current_user)
        # current_recipies = RecipieInfo.objects.all()
        print(current_recipies)
        context={
            'currentRecipies':current_recipies,
        }
        return render(request,'recipeApp/index.html',context)
    else:
        current_recipies=''
        context={
            'currentRecipies':current_recipies,
        }
        return render(request,'recipeApp/index.html',context)

def createUser(request):  #allows user to create account
    blankUser=NewUserForm(request.POST or None)   #get request
    if request.method=='POST':  #if the request is a post request
        if blankUser.is_valid():  #if the information is valid
            holdKey = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])  #create the user
            blankUser.userTableForeignKey = holdKey
            blankUser.save()
            return redirect('index')  #return to index
        else:    #otherwise
            blankUser=NewUserForm(request.POST)  #gets the information the user entered
            context={
                'errors':blankUser.errors, #errors on page
                'form':blankUser
            }
            return render(request,'recipeApp/createUser.html',context)  #allows user to make corrections
    context={
        'form':blankUser,
    }
    return render(request,'recipeApp/createUser.html',context) #sends back a blank form to the page

def allRecipies(request):
    return render(request,'recipeApp/allRecipies.html')

def newRecipies(request,): #allows user to create a recipe
    recipie=RecipieInfoForm(request.POST or None)   #get request
    owner=NewUser.objects.get(username=request.user) #grabs the current user logged in
    if request.method=='POST':  #if the request is a post request
        if recipie.is_valid():  #if the information is valid

            createdrecipie=RecipieInfo.objects.create(picture=request.POST['picture'],meal_name=request.POST['meal_name'],description=request.POST['description'], date_created=request.POST['date_created'],creator=request.POST['creator'],ingredients=request.POST['ingredients'],directions=request.POST['directions'],keytoNewUser=owner)  #create the recipe
            return redirect('index')  #return to index
        else:    #otherwise
            recipie=RecipieInfoForm(request.POST)  #gets the information the user entered
            context={
                'errors':recipie.errors, #errors on page
                'form':recipie,
            }
            return render(request,'recipeApp/newRecipies.html',context)  #allows user to make corrections
    context={
        'form':recipie,
    }
    return render(request,'recipeApp/newRecipies.html',context) #sends back a blank form to the page    return render(request,'recipeApp/newRecipies.html')
def profilePage(request):
    userProfile=NewUser.objects.filter(username=request.user)
    return render(request,'recipeApp/profilePage.html',{'userProfile':userProfile})

def editProfile(request,ID):
    oldProfile=get_object_or_404(NewUser,pk=ID)
    newProfile=changeProfile(request.POST,instance=oldProfile)
    if request.method=='POST':
        newProfile=NewUserForm(request.POST,instance=oldProfile)
        if newProfile.is_valid():
            newProfile.save()
            return redirect('profilePage')
        else:
            newProfile=NewUserForm(request.POST)
            context={
                'newProfile':newProfile,
                'errors':newProfile.errors,
            }
            return render(request,'recipeApp/editProfile.html',context)
    context={
            'newProfile':newProfile,
        }
    return render(request,'recipeApp/editProfile.html',context)


def details(request,ID):
        recipieSteps=get_object_or_404(RecipieInfo,pk=ID)
        current_recipies=RecipieInfo.objects.filter(id=ID)
        return render(request,'recipeApp/details.html',{'currentRecipies':current_recipies})
