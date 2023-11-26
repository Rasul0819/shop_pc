from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from .models import User ,Product , Category,Review
from .forms import UserCreationFormByMe,ReviewForm
from django.contrib import messages
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

def loginuser(request):
    # return render(request,'users/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:product_list')
        else:
            # Обработка неправильных учетных данных
            return render(request, 'users/login.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'users/login.html')

def logoutuser(request):
    logout(request)
    return redirect('shop:product_list')




def register(request):
    if request.method == 'GET':
        form  = UserCreationFormByMe()
        context = {'form': form}
        return render(request, 'users/register.html', context)
    if request.method == 'POST':
        form  = UserCreationFormByMe(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('shop:product_list')
    else:
        print('Form is not valid')
        messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'users/register.html', context)
    return render(request, 'users/register.html', {})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })




def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    reviews = Review.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', {'product': product,'cart_product_form':cart_product_form,'reviews': reviews,})
    

@login_required  
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', id=product.id, slug=product.slug)
    else:
        form = ReviewForm()

    return render(request, 'shop/add_review.html', {'form': form, 'product': product})


