from django.db import models

class Library(models.Model):
    request_id = models.CharField(max_length=50, primary_key=True)
    library_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')

class Book(models.Model):
    book_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='available')

class UserProfile(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    request_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    history = models.TextField(default='None')

class LoanRequest(models.Model):
    request_id = models.CharField(max_length=50, primary_key=True)
    user_id = models.CharField(max_length=50)
    book_id = models.CharField(max_length=50)
    from_library = models.CharField(max_length=100)
    to_library = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Not Approved')

class TransactionTable(models.Model):
    transaction_id = models.CharField(max_length=50, primary_key=True)
    user_id = models.CharField(max_length=50)
    request_id = models.CharField(max_length=50)
    book_id = models.CharField(max_length=50)
    date_borrowed = models.IntegerField()
    date_returned = models.IntegerField()
    paid_status = models.CharField(max_length=10, default='No')
