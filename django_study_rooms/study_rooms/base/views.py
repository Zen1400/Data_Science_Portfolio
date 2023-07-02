from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic, Message
from .forms import RoomForm, TopicForm, MessageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm  #Used in register to create a model to sign up

# Create your views here.



def loginpage(request):
    # page variable is used to determine which part to show in 'login_register.html'
    page = 'login'

    # To prevent the user from going manually to login once logged in
    if request.user.is_authenticated :
        return redirect('home')

    if request.method == 'POST' :
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # check if the user exists and raise a message if not
        try :
            # Querying the User (built-in) model that I imported to verify if user exists
            user = User.objects.get(username=username)
        except :
            # If user doesn't exist I'm throwing a message
            messages.error(request, 'Username doesnt exist')

        user = authenticate(request, username=username, password = password)

        if user is not None :
            # login will create a session in the database and the browser
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, 'Username or Password is not correct!')

    context = {'page' : page}
    return render(request, 'base/login_register.html', context)



def logoutUser(request) :
    logout(request)
    return redirect('home')

def registeruser(request) :
    form = UserCreationForm()
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save(commit=False)  # commit = False because we want to modify before save in the DB
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, 'An error occurred during registration')
    context = {'form':form}
    return render(request, 'base/login_register.html', context)


def home(request) :
    """
    Here I'm getting q from the home.html (q = topic.name) if it's given
    then I'm using it to query Room model
    """
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(           #  Q allows to query with & | (and or)
        Q(topic__name__icontains = q) |
        Q(name__icontains = q)

        )
    room_count = rooms.count()
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(
        Q(room__topic__name__icontains=q)
        )
    context =  {'rooms' : rooms, 'topics':topics, 'room_count' : room_count,
                'room_messages':room_messages}
    return render(request, 'base/home.html',context)

def room(request, n) :

    room = Room.objects.get(id=n)
    # One to Many relation we access with _set.all()
    room_messages = room.message_set.all().order_by('-created')
    # .all() to access Many to Many relation
    participants = room.participants.all()
    if request.method == 'POST' :
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')    # get it from room.html which is the name of the input in the forum
        )
        # Add the user who wrote the message to participants of the room.
        room.participants.add(request.user)
        # I'm redirecting (Get request) because it's a POSt request and it's going to mess some fuctionalities
        return redirect('room', n = room.id)
    context = {'room':room, 'r_messages':room_messages,
               'participants':participants}
    return render(request, 'base/room.html', context)

# This will allow only logged in users to create a room, if not logged it will redirect them to login URL
# Done by importing login_required from decorators


def userprofile(request, id):
    user = User.objects.get(id = id)
    rooms = user.room_set.all()        # _set    allows me to access a child model
    topics = Topic.objects.all()
    room_messages = user.message_set.all()
    context = {'user':user, 'rooms': rooms, 'room_messages':room_messages, 'topics':topics}

    return render(request, 'base/profile.html', context)




@login_required(login_url= 'login')
def createroom(request) :
    form = RoomForm()
    if request.method == 'POST' :
        form = RoomForm(request.POST)            # RoomForm class will extract data
        if form.is_valid() :
            room = form.save(commit=False) # Delay saving to the database to be able to assign a host because Iremoved it from the Forum so the user can't choose it(it should be automatic)
            room.host = request.user
            room.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url= 'login')
def createtopic(request):
    form = TopicForm()
    if request.method == 'POST' :
        form = TopicForm(request.POST)            # RoomForm class will extract data
        if form.is_valid() :
            form.save()         # save data in the database
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url= 'login')
def updateroom(request, n) :
    room = Room.objects.get(id = n)            # Query the Room model
    form = RoomForm(instance=room)
    # Only the room creater can update it
    if request.user != room.host :
        return HttpResponse('You are not the owner of this room!')

    if request.method == 'POST' :
        # instance to tell which room to update, without instance =, it will add a new room
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url= 'login')
def deleteroom(request, n) :
    room = Room.objects.get(id = n)
    if request.user != room.host :
        return HttpResponse('You are not the owner of this room!')
    if request.method == 'POST' :
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})


@login_required(login_url= 'login')
def deletemessage(request, n) :
    message = Message.objects.get(id = n)
    if request.user != message.user :
        return HttpResponse('You are not the owner of this room!')
    if request.method == 'POST' :
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':message})



@login_required(login_url='login')
def editmessage(request,n):
    message = Message.objects.get(id=n)
    form = MessageForm(instance=message)
    if request.method =='POST' :
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/edit.html', {'form':form})
