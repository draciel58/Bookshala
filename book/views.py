from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Book,Wishlist
from .form import BookForm

def home(request):
	return render(request, "book/home.html");

def authpage(request):
	return render(request, "book/authpage.html")

def signup(request):
	if request.POST['password']==request.POST['confirm_password']:
		try:
			if len(request.POST['password'])<8:
				return render(request, 'book/signup.html', {'error':'weak password! Try again'})
			else:	
				user = User.objects.create_user(username=request.POST['username'], password=request.POST['password']) 
				user.save()
				login(request,user)
				return redirect('main')
		except IntegrityError:
			return render(request, 'book/authpage.html', {'error':'Username already taken. Try again'})				
	else:
		return render(request, 'todo/authpage.html', {'error':'Password did not match'})


def loginuser(request):
	user = authenticate(request, username=request.POST['un'], password=request.POST['pwd'])		
	if user is None:
		return render(request, 'book/authpage.html', {'error':'username and password did not match'})
	else:
		login(request, user)
		return redirect('main')


@login_required
def logoutuser(request):
	if request.method=='POST':
		logout(request)
		return redirect('authpage')


@login_required
def main(request):
	books = Book.objects.all()
	return render(request, 'book/main.html', {'books':books})

@login_required
def viewbook(request, book_pk):
	book = get_object_or_404(Book, pk=book_pk)
	return render(request, 'book/viewbook.html',{'b':book})


@login_required
def addbook(request):
	if request.method=='GET':
		return render(request, 'book/addbook.html', {'form':BookForm()})
	else:
		try:
			form = BookForm(request.POST,request.FILES)
			newbook = form.save(commit=False)
			newbook.user = request.user
			newbook.save()
			return redirect('main')
		except ValueError:
			return render(request, 'book/addbook.html', {'form':BookForm(), 'error':'Bad data passed in! Try again'})


@login_required
def wishlist(request):
	if(request.method=="GET"):
		items = Wishlist.objects.filter(user=request.user)
		return render(request, 'book/wishlist.html', {'items':items})
	else:
		num = request.POST['id'];
		b = Wishlist.objects.filter(user=request.user,numid=num)
		print(b)
		if b.exists():
			return redirect('main')
		item = get_object_or_404(Book,pk=num)
		a = Wishlist.objects.create(user=request.user,numid=num,name=item.name,posted=item.posted,price=item.price,seller_name=item.seller_name,contact_number=item.contact_number,book_template=item.book_template)
		a.save();
		return redirect('main')

@login_required
def yourbooks(request):
	book = Book.objects.filter(user=request.user)
	return render(request, 'book/yourbooks.html',{'book':book})

@login_required
def deletebook(request, book_pk):
	book = Book.objects.get(user=request.user,pk=book_pk)
	inlist = Wishlist.objects.filter(numid=book.id)
	if inlist.exists():
		getbook = Wishlist.objects.get(numid=book.id)
		getbook.delete()
	book.delete()
	return redirect('main')

