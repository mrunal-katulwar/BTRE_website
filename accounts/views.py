from django.shortcuts import render, redirect
from django.contrib import messages, auth # bring in auth for login
from django.contrib.auth.models import User
from contacts.models import Contact 
# Create your views here.

def login(requests):
	if requests.method == 'POST':
		username = requests.POST['username']
		password = requests.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(requests, user)
			messages.success(requests, 'Logged in successfully')
			return redirect('dashboard')
		else:
			messages.error(requests, 'Invalid username or password')
			return redirect('login')

	else:
		return render(requests, 'accounts/login.html')

def register(requests):
	if requests.method == 'POST':
		#get form values
		first_name = requests.POST['first_name']
		last_name = requests.POST['last_name']
		username = requests.POST['username']
		email = requests.POST['email']
		password = requests.POST['password']
		password2 = requests.POST['password2']
		# check if passwords match
		if password2 == password:
			#check username
			if User.objects.filter(username=username).exists():
				messages.error(requests, 'Username already exists')
				return redirect('register')
			else:
				if User.objects.filter(email=email).exists():
					messages.error(requests, 'Email is already in use')
					return redirect('register')
				else:
					user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
					# login after registration
					# auth.login(requests, user)
					# messages.success(requests, 'Welcome to BT- Real Estate')
					# return redirect('index')
					user.save();
					messages.success(requests, 'Registration Successful')
					return redirect('login')

		else:
			messages.error(requests, 'Password do not match')
			return redirect('register')
	else:
		return render(requests, 'accounts/register.html')

def dashboard(requests):
	user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = requests.user.id)
	context = {
		'contacts' : user_contacts
	}
	return render(requests, 'accounts/dashboard.html', context)

def logout(requests):
	if requests.method == 'POST':
		auth.logout(requests)
		messages.success(requests, 'logged out successfully')
		return redirect('index')