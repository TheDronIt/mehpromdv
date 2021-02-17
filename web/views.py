from django.shortcuts import render, redirect
from .models import News, Product
from .forms import MessageForm

def index(request):
	return render(request, 'index.html') 

def news(request):
	news = News.objects.all()
	#paginator  = paginator(post_list, 8)
	return render(request, 'news.html', locals())

def newspage(request, id):
	newspage = News.objects.get(id=id)
	return render(request, 'newspage.html', {'newspage':newspage})

def contact(request):
	error = ''
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Ошибка заполнения формы'

	form = MessageForm()
	data = {
		'form': form,
		'error': error
	}
	return render(request, 'contact.html', data) 

def metal(request):
	return render(request, 'metal.html')

def windlass(request):
	cat11 = Product.objects.filter(category=11)
	cat12 = Product.objects.filter(category=12)
	cat13 = Product.objects.filter(category=13)
	cat14 = Product.objects.filter(category=14)
	cat15 = Product.objects.filter(category=15)
	cat16 = Product.objects.filter(category=16)
	cat21 = Product.objects.filter(category=21)
	cat22 = Product.objects.filter(category=22)
	cat23 = Product.objects.filter(category=23)
	cat24 = Product.objects.filter(category=24)
	cat25 = Product.objects.filter(category=25)
	cat26 = Product.objects.filter(category=26)
	cat27 = Product.objects.filter(category=27)
	cat28 = Product.objects.filter(category=28)
	cat29 = Product.objects.filter(category=29)
	cat210 = Product.objects.filter(category=210)
	cat211 = Product.objects.filter(category=211)
	cat212 = Product.objects.filter(category=212)
	cat217 = Product.objects.filter(category=213)
	cat218 = Product.objects.filter(category=218)
	cat219 = Product.objects.filter(category=219)
	return render(request, 'windlass.html', locals())


def ejector(request):
	cat31 = Product.objects.filter(category=31)
	cat32 = Product.objects.filter(category=32)
	return render(request, 'ejector.html', locals())


def productpage(request, id):
	productpage = Product.objects.get(id=id)
	return render(request, 'productpage.html', {'productpage':productpage})


def search(request):
	search_query = request.GET.get('search','')
	error = ""
	searchpost = ""
	if len(search_query) > 1:
		error = ""
		searchpost = Product.objects.filter(name__icontains=search_query)
		return render(request, 'search.html', {'searchpost':searchpost, 'error':error})
	else:
		earchpost = ""
		error = "Упс.<br>Произошла ошибк <br><br>Укажите название услуги, которую вы хотити найти, или перейдите в раздел 'Услуги' для поиска нужной вам информации."
		return render(request, 'search.html', {'searchpost':searchpost, 'error':error})
	if(len(searchpost) < 1):
		earchpost = ""
		error = "Упс.<br>Ничего не найдено.<br><br>Укажите название услуги, которую вы хотити найти, или перейдите в раздел 'Услуги' для поиска нужной вам информации."
	return render(request, 'search.html', {'searchpost':searchpost, 'error':error})
