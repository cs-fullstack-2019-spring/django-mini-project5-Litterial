from django.shortcuts import render,redirect,get_object_or_404
from .forms import RecipieInfo,RecipieInfoForm,NewUser,NewUserForm,changeProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request): #goes to home page
    if request.user.is_authenticated: #if user is logged in
        current_user= NewUser.objects.get(username=request.user) #gets the username
        current_recipies=RecipieInfo.objects.filter(keytoNewUser=current_user) #filters all recipies with that user
        context={
            'currentRecipies':current_recipies,
        }
        return render(request,'recipeApp/index.html',context)  #renders to index with user
    else:   #otherwise
        current_recipies=''
        context={
            'currentRecipies':current_recipies,
        }
        return render(request,'recipeApp/index.html',context) #send this blank because the index is expecting this variable

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
    recipie_list=RecipieInfo.objects.all()

    return render(request,'recipeApp/allRecipies.html',{'list':recipie_list},)

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

def profilePage(request): #allows user to view profile page
    userProfile=NewUser.objects.filter(username=request.user) #filters users by username
    return render(request,'recipeApp/profilePage.html',{'userProfile':userProfile}) #renders on profile page with info

def editProfile(request,ID): #edit profile page
    oldProfile=get_object_or_404(NewUser,pk=ID) #gets the ID of the user
    newProfile = changeProfile(instance=oldProfile) #grabs saved information from NewUser
    if request.method=='POST':   # if post
        newProfile=changeProfile(request.POST)  #fills information in the form
        if newProfile.is_valid(): #if valid
            newProfile.save() #save info
            return redirect('profilePage')  #redirect to profile page
        else: #else
            print(newProfile.errors)
            print(newProfile.non_field_errors)
            newProfile2=changeProfile(request.POST)
            context={
                'newProfile':newProfile2,
                'errors':newProfile.errors,
            }

            return render(request,'recipeApp/editProfile.html',context) #returns back to page with errors
    context={
            'newProfile':newProfile,
        }
    return render(request,'recipeApp/editProfile.html',context) #rendets on edit profile page


def details(request,ID): #gets details of recipies
        recipieSteps=get_object_or_404(RecipieInfo,pk=ID) #grabs the id of the recipie
        print(recipieSteps)
        current_recipies=RecipieInfo.objects.filter(id=ID) #grabs the recipie that matches the id
        print(current_recipies)
        return render(request,'recipeApp/details.html',{'currentRecipies':current_recipies}) #renders to details

def editRecipie(request,ID): #edit recipie
    recipieSteps=get_object_or_404(RecipieInfo,pk=ID) #gets id of recipie
    differentRecipie=RecipieInfoForm(instance=recipieSteps) #grabs instance of recipie

    if request.method =="POST":
        differentRecipie=RecipieInfoForm(request.POST,instance=recipieSteps) #fills in info in form
        if differentRecipie.is_valid(): #if valid
            differentRecipie.save() #saves
            return redirect('index') #redirects to index
        else:
            differentRecipie=RecipieInfoForm(request.POST)
            context={
                    'form':differentRecipie,
                    'errors':differentRecipie.errors,
                }

            return render(request,'recipeApp/editRecipie.html',context) #list errors on page if there are issues
    context={
            'form':differentRecipie,
        }
    return render(request,'recipeApp/editRecipie.html',context)





