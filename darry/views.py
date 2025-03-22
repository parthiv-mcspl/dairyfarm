from django.shortcuts import render, get_object_or_404, redirect
from .models import Info, Product, Book
from .models import Review
from .forms import ReviewForm

def combined_view(request):
    infos = Info.objects.all()
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'info.html', {'infos': infos, 'products': products})


def book_view(request):
    books = Book.objects.all()  # Fetch all book entries
    return render(request, 'book.html', {'books': books})



def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_page')  # Reload the page after submission
    else:
        form = ReviewForm()
    
    # Fetch all reviews and calculate stars
    reviews = Review.objects.all().order_by('-date')  # Show most recent reviews first
    for review in reviews:
        review.stars_filled = range(review.rating)  # Filled stars (gold)
        review.stars_empty = range(5 - review.rating)  # Empty stars (gray)
    
    return render(request, 'review_page.html', {'form': form, 'reviews': reviews})

def for_contact(request):
    return render(request,'contact.html')