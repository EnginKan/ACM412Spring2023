from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Review,Publisher
# Create your views here.

def home(request):
    return render(request,'home.html',{'name': 'ACM412'})

def getAllBooks(request):
    all_books=Book.objects.all()    
    return  render(request,"allbooks.html",{'all_books': all_books})

def getBookByID(request, id):
    book=Book.objects.get(id=id)
    reviews=Review.objects.filter(book_id=id)
    item={}
    if book:
        item['book_title']=book.title
        item['book_publisher']=book.publisher.name
        item['book_isbn']=book.isbn

    return render(request,'bookDetails.html',{'item': item})
            

