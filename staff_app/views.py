from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Library, Book, UserProfile, LoanRequest, TransactionTable

@login_required(login_url='/accounts/login/')
def index(request):
    # Ambil data dari database
    libraries = Library.objects.all()
    books = Book.objects.all()
    users = UserProfile.objects.all()
    loans = LoanRequest.objects.all()
    transactions = TransactionTable.objects.all()

    # Logik kira denda
    for t in transactions:
        t.fine = max(0, (t.date_returned - t.date_borrowed) * 0.50)

    # Pastikan nama-nama ini tepat!
    context = {
        'libraries': libraries,
        'books': books,
        'users': users,
        'loans': loans,
        'transactions': transactions,
    }
    return render(request, 'index.html', context)