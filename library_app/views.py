from django.shortcuts import render, redirect
from . models import Book_table

def index(request):
    return render(request, 'index.html')

def addbooks(request):
    if request.method == 'POST':
        title = request.POST['title'] 
        authorname = request.POST['authorname'] 
        year = request.POST['year']
        genre = request.POST['genre']
        contact = request.POST['contact']
        obj = Book_table.objects.create(title=title, author=authorname, publication_year=year, genre=genre, contact=contact)
        obj.save()
        if obj:
            return redirect("/books")
        else:
            return render(request,'bookdetails.html')
    return render(request, "addbooks.html")

def bookdetails(request):
    if request.method == 'POST':
        search = request.POST['search']
        data = Book_table.objects.filter(author=search)
        if data:
            return render(request,'searchresult.html', {'data': data})
            # return redirect('/search', {'data': data})
    data = Book_table.objects.all()
    return render(request, 'bookdetails.html', {'data': data})

# def searchresult(request):
#     return render(request, 'searchresult.html')



# Create your views here.
