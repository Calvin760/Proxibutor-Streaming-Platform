from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Music, Artist
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate


def handle_error_message(request, message):
    messages.error(request, message)
    return redirect(request.META.get('HTTP_REFERER', 'index'))

@login_required(login_url='login')
def index(request):


    releases = Music.objects.filter(user=request.user).order_by('-release_date')
    
    return render(request, 'index.html', {'releases': releases})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use") 
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                auth.login(request, user)
                messages.success(request, "User registered successfully!")
                return redirect('index')
        else:
            messages.error(request, "Passwords do not match") 
            return redirect('register')

    return render(request, 'register.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('login')

@login_required(login_url='login')
def release(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        stage_name = request.POST.get('stage_name')
        featured_artists = request.POST.get('featured_artists', '')
        release_date = request.POST.get('release_date')
        cover_art = request.FILES.get('cover_art')
        song = request.FILES.get('song')
        credits = request.POST.get('credits', '')
        genre = request.POST.get('genre')

        if not all([title, release_date, cover_art, song, genre]):
            return handle_error_message(request, "Please fill in all fields.")

        artist = get_object_or_404(Artist, stage_name=stage_name)  # Find artist by stage name

        Music.objects.create(
            user=request.user,
            title=title,
            artist=artist,
            featured_artists=featured_artists,
            release_date=release_date,
            cover_art=cover_art,
            song=song,
            credits=credits,
            genre=genre,
        )
        messages.success(request, "Release added successfully!")
        return redirect('index')

    return render(request, 'release.html')


@login_required(login_url='login')
def music_collection(request):

    music_list = Music.objects.order_by('title')


    search_query = request.GET.get('search', '')
    if search_query:
        music_list = music_list.filter(
            Q(title__icontains=search_query) | Q(stage_name__icontains=search_query)
        )

    return render(request, 'music.html', {'music_list': music_list, 'search_query': search_query})

def about(request):

    return render(request, 'about.html')

def account(request):

    return render(request, 'account.html')

@login_required(login_url='login')
def update_account(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        if User.objects.filter(username=new_username).exists():
            messages.error(request, "Username already taken.")
            return redirect('account')  # Redirect back to account page
        else:
            request.user.username = new_username
            request.user.save()
            messages.success(request, "Username updated successfully!")
            return redirect('account')

    return render(request, 'account.html')

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')


        user = authenticate(username=request.user.username, password=current_password)
        if user is not None:

            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Password changed successfully!")
            return redirect('account')
        else:
            messages.error(request, "Current password is incorrect.")
            return redirect('account')
        
    return render(request, 'account.html')

@login_required(login_url='login')
def artist_detail(request):
    return render(request, 'streaming.html')

@login_required(login_url='login')
def profile(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    music_list = Music.objects.filter(artist=artist)  # Fetch music related to this artist

    return render(request, 'profile.html', {'artist': artist, 'music_list': music_list})

def music2(request):
    return render(request, 'music2.html')

def index2(request):
    return render(request, 'index2.html')

def artist_profiles(request):
    artists = Artist.objects.all()  # Query all artists from the database
    return render(request, 'artistprofiles.html', {'artists': artists})

@login_required(login_url='login')
def create_artist_profile(request):
    if request.method == 'POST':
        stage_name = request.POST.get('stage_name')
        header_image = request.FILES.get('header_image')
        profile_picture = request.FILES.get('profile_picture')
        bio = request.POST.get('bio')

        if not stage_name or not header_image or not profile_picture or not bio:
            messages.error(request, "Please fill in all fields.")
            return redirect('createArtist')

        # Check for existing stage name
        if Artist.objects.filter(stage_name=stage_name).exists():
            messages.error(request, "This stage name is already taken.")
            return redirect('createArtist')

        # Create and save the artist profile
        artist = Artist(
            stage_name=stage_name,
            header_image=header_image,
            profile_picture=profile_picture,
            bio=bio
        )
        artist.save()
        messages.success(request, "Artist profile created successfully!")
        return redirect('index')  # Redirect to an appropriate page

    return render(request, 'createArtist.html')